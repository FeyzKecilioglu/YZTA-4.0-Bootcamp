# 🧠 EpiCast - Bulaşcı Hastalık Analiz Aracı
# Versiyon: Final (14 gün tahminli, isteğe bağlı ülke seçimi ile)

import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="EpiCast", layout="wide")
st.title("🧠 EpiCast - Bulaşcı Hastalık Analiz Aracı")

# Kullanıcı Girişi ve Dosya Yükleme
st.sidebar.header("Hastalık Seçimi")
st.sidebar.markdown("Analiz etmek istediğiniz hastalığı seçin. Bu seçim, yorumları ve grafik başlıklarını etkiler.")
disease_type = st.sidebar.selectbox("Hastalık Seçimi", [
    "COVID-19", "Influenza (Grip)", "Dengue", "Zika", "Ebola", 
    "Tüberküloz (TB)", "Kızamık", "RSV"
])

uploaded_file = st.file_uploader("CSV veri dosyanızı yükleyin", type="csv")

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip()
    return df.fillna(0)

if not uploaded_file:
    st.warning("Lütfen bir CSV dosyası yükleyin.")
    st.stop()

with st.spinner("Veri işleniyor..."):
    df = load_data(uploaded_file)

    date_col = next((col for col in df.columns if "date" in col.lower()), None)
    if not date_col:
        st.error("Tarih sütunu bulunamadı.")
        st.stop()
    df['date'] = pd.to_datetime(df[date_col], errors='coerce')
    if df['date'].isna().all():
        st.error("Tarih sütunu geçersiz. Lütfen tarih formatını kontrol edin.")
        st.stop()

    possible_case_cols = ["cases", "new_cases", "confirmed", "total_cases"]
    case_col = next((col for col in df.columns if col.lower() in possible_case_cols), None)
    if not case_col:
        st.error("Vaka sütunu bulunamadı. Lütfen 'cases' gibi yaygın isimlendirme kullanın.")
        st.stop()

    country_col = next((col for col in df.columns if "country" in col.lower() or "region" in col.lower()), None)

    if country_col:
        countries = sorted(df[country_col].dropna().unique().tolist())
        countries.insert(0, "Tümü")
        selected_country = st.selectbox("Ülke Seçimi (isteğe bağlı)", countries)
        if selected_country != "Tümü":
            df = df[df[country_col] == selected_country]

    df = df[df['date'] >= df['date'].max() - pd.Timedelta(days=14)]

    st.subheader("Tanınan Sütunlar")
    st.markdown(f"""
    - Tarih sütunu: `{date_col}`  
    - Vaka sütunu: `{case_col}`  
    - Ülke sütunu: `{country_col if country_col else 'Yok'}`
    """)

    st.subheader("Veri Önizlemesi")
    st.write(df.head())

def predict_future(df, case_col, days=14):
    df = df.copy().sort_values("date")
    df['day_num'] = (df['date'] - df['date'].min()).dt.days
    X = df[['day_num']]
    y = df[case_col]
    if len(X) < 2 or X['day_num'].nunique() == 0:
        raise ValueError("Tahmin için yeterli veri yok.")
    model = LinearRegression()
    model.fit(X, y)
    future_days = np.array([[X['day_num'].max() + i] for i in range(1, days + 1)])
    predictions = model.predict(future_days)
    future_dates = [df['date'].max() + pd.Timedelta(days=i) for i in range(1, days + 1)]
    return pd.DataFrame({'date': future_dates, case_col: predictions})

st.subheader("Vaka Yoğunluğu Haritası")
if country_col:
    try:
        map_fig = px.choropleth(
            df,
            locations=country_col,
            locationmode="country names",
            color=case_col,
            hover_name=country_col,
            color_continuous_scale="Reds"
        )
        st.plotly_chart(map_fig)
    except Exception as e:
        st.error(f"Harita çizilemedi: {e}")
else:
    st.info("Ülke bilgisi bulunamadı, harita gösterilemiyor.")

st.subheader("Günlük Vaka Grafiği")
try:
    fig = px.line(df, x='date', y=case_col, title=f"{disease_type} - Günlük Vaka Sayısı ({selected_country})")
    st.plotly_chart(fig)
except Exception as e:
    st.error(f"Grafik çizilemedi: {e}")

st.subheader("Genel İstatistikler")
try:
    total = df[case_col].sum()
    peak = df.loc[df[case_col].idxmax()]
    mean = df[case_col].mean()
    last = df['date'].max()
    st.markdown(f"""
    - Toplam vaka: **{int(total):,}**  
    - En yüksek günlük vaka: **{int(peak[case_col]):,}** ({peak['date'].date()})  
    - Günlük ortalama: **{int(mean):,}**  
    - Son veri tarihi: **{last.date()}**
    """)
except Exception as e:
    st.error(f"Özet hesaplanamadı: {e}")

try:
    if df[case_col].is_monotonic_increasing:
        df[case_col] = df[case_col].diff().fillna(0)

    pred_df = predict_future(df, case_col, days=14)
    combined = pd.concat([df[['date', case_col]], pred_df])

    st.subheader("14 Günlük Tahmin")
    fig2 = px.line(combined, x='date', y=case_col, title=f"{disease_type} - Gerçek ve Tahmini Vaka Grafiği")
    st.plotly_chart(fig2)

    start_date = df['date'].max().date()
    st.caption(f"Not: Bu grafik, son veri tarihi olan **{start_date}**'den itibaren 14 günlük tahmini içermektedir.")

    first, last = pred_df[case_col].iloc[0], pred_df[case_col].iloc[-1]
    st.subheader("Tahmin Yorumu")
    if last > first * 1.1:
        st.markdown("Artış eğilimi bekleniyor.")
    elif last < first * 0.9:
        st.markdown("Düşüş eğilimi bekleniyor.")
    else:
        st.markdown("Sabit seyir bekleniyor.")
except Exception as e:
    st.error(f"Tahmin yapılamadı: {e}")

st.subheader("Hastalığa Özgü Bilgi")
comments = {
    "COVID-19": "Yeni varyantlar nedeniyle dalgalanmalar görülebilir.",
    "Influenza (Grip)": "Mevsimsel geçişlerde vaka artışı görülebilir.",
    "Dengue": "Sivrisinek kaynaklı, sıcak iklimlerde yaygındır.",
    "Zika": "Hamile bireyler için risk taşır.",
    "Ebola": "Yüksek ölüm oranlı, hızlı izolasyon gerekir.",
    "Tüberküloz (TB)": "Tedavi uzun sürer, direnç gelişebilir.",
    "Kızamık": "Aşı oranı düşükse salgın riski yüksektir.",
    "RSV": "Bebekler ve yaşlılar için tehlikeli olabilir."
}
st.markdown(comments.get(disease_type, ""))
