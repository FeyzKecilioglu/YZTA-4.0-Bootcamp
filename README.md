
## <img width="500" height="500" alt="Logo" src="https://github.com/user-attachments/assets/291bf40a-c326-4cf9-bbf8-141cf08831c7" />
## Proje Açıklaması

EpiCast, bulaşıcı hastalık verilerinin analizini, görselleştirmesini ve kısa vadeli öngörülerini yapabilen, kullanıcı dostu ve açık veriye dayalı bir web uygulamasıdır.  
Kullanıcıların kendi verilerini sisteme yükleyerek analiz yapabildiği bu platform; özellikle sağlık, veri bilimi ve eğitim alanlarında çalışan bireyler için hızlı ve anlamlı içgörüler sunmayı hedeflemektedir.

Geliştirilen bu sistemin temel motivasyonu, COVID-19 pandemisiyle birlikte ortaya çıkan veri ihtiyacıdır. Bireylerin ve kurumların, sağlık verilerini yorumlamak için teknik bilgiye sahip olmadan da sezgisel araçlara erişebilmesini amaçladık. EpiCast, bu ihtiyaca cevap vermek için tasarlanmıştır.

Kullanıcı uygulamayı kullanırken:

- **Kendi CSV dosyasını** yükleyebilir ve verisini doğrudan görselleştirebilir.  
- Tarih ve vaka bilgilerine göre **zaman serisi grafiği** oluşturabilir.  
- Sistem tarafından otomatik tanımlanan sütunlar sayesinde **veri ön işleme** zahmetiyle uğraşmaz.  
- 7 günlük **lineer regresyon tabanlı tahmin** alarak kısa vadeli eğilimleri görebilir.  
- **Vaka sayısındaki artış ya da düşüş eğilimleri** sistem tarafından yorumlanarak kullanıcıya sunulur.  
- Seçilen hastalık türüne göre **bağlama özgü açıklamalar** ekrana yansıtılır (örneğin: Zika virüsü hamile bireyler için özel risk içerir).  
- Eğer veri uygun yapıda ise, ülke bazlı yoğunluklar **harita üzerinde görselleştirilir**.

Uygulama sadece teknik kullanıcıları değil, aynı zamanda **veri ile yeni tanışan bireyleri** de desteklemektedir.  
Arayüzün sade ve rehberli yapısı sayesinde kullanıcı, karşısına çıkan tüm sonuçları doğrudan anlayabilir, karar verme süreçlerine veri destekli yaklaşabilir.  
Ayrıca, sistemin ölçeklenebilirliği sayesinde ilerleyen sürümlerde tahmin algoritmaları geliştirilebilir, ek veri kaynakları entegre edilebilir ve kullanıcı rollerine göre modüller tanımlanabilir.

EpiCast'in temel felsefesi şudur:  
**“Herkes analiz yapabilmeli. Herkes veriye dayalı karar verebilmeli.”**

## Ürün Özellikleri (Product Features)

1. **Dosya Yükleme ve Tanıma**
   - Kullanıcılar kendi .csv uzantılı veri dosyalarını sisteme kolayca yükleyebilir.
   - Sistem, tarih (`date`), vaka (`cases`, `new_cases`, `confirmed`) ve ülke (`country`, `region`, `location`) sütunlarını otomatik olarak tanır.
   - Sütun adlarındaki boşluklar, büyük/küçük harf farklılıkları veya varyasyonlar normalize edilir.

2. **Zaman Serisi Grafiği**
   - Pandas ve Plotly kullanılarak tarih-vaka ilişkisine dayalı interaktif bir çizgi grafik oluşturulur.
   - Bu grafik, vaka sayısının zaman içindeki değişimini net biçimde görselleştirir.
   - Kullanıcı bu grafik üzerinden dalgalanmaları, zirve noktaları ve genel eğilimleri hızlıca analiz edebilir.

3. **İleriye Dönük Tahmin Özelliği**
   - Linear Regression modeli ile geçmiş verilere dayalı olarak ileriye dönük vaka tahminleri yapılır.
   - Tahmin sonuçları, mevcut verilerle birleştirilerek aynı çizgi grafik üzerinde gösterilir.
   - Model, zaman serisini `day_num` formatına çevirerek makine öğrenmesi algoritmasına uygun hale getirir.

4. **Otomatik Eğilim Yorumu**
   - Tahminin ilk ve son günü arasındaki yüzde fark hesaplanır.
   - Eğer belirgin bir artış/düşüş varsa, sistem kullanıcıyı buna dair bilgilendirir.
   - Bu yorumlar, veriye dayalı ama herkesin anlayabileceği şekilde sade biçimde sunulur.

5. **Harita Üzerinde Vaka Yoğunluğu**
   - Choropleth harita ile ülke bazlı vaka dağılımı görselleştirilir.
   - Kullanıcının veri setinde ülke bilgisi varsa, bu sütun üzerinden dünya haritası çizilir.
   - Yoğunluk renk skalasına göre bölgesel farklar sezgisel biçimde analiz edilebilir.

6. **Hastalığa Özgü Açıklamalar**
   - Kullanıcı, analiz yapmak istediği hastalığı (COVID-19, RSV, Kızamık, Ebola vb.) sol panelden seçer.
   - Uygulama, hastalığa özgü açıklamaları dinamik olarak ekranda gösterir.
   - Bu açıklamalar, hem bilgilendirici hem de risk farkındalığı sağlayıcı niteliktedir.

7. **Hata Yönetimi ve Esnek Girdi Desteği**
   - Sistem, tarih formatı bozuksa, vaka sütunu eksikse veya tüm değerler `NaT` geliyorsa kullanıcıyı uyarır ve işlemi durdurur.
   - Eksik veriler otomatik olarak sıfırla (`fillna(0)`) tamamlanır.
   - Kod, farklı ülkelerden ve kurum formatlarından gelen çeşitli veri yapılarına karşı toleranslı olacak şekilde tasarlanmıştır.

## Hedef Kitle (Target Audience)

- **Veri Bilimiyle İlgilenenler**
  - Kendi verileriyle veri temizleme, görselleştirme ve basit makine öğrenmesi uygulamak isteyen bireyler.
  - Python, pandas, plotly ve sklearn gibi teknolojileri gerçek bir proje üzerinde denemek isteyen öğrenciler.

- **Sağlık Profesyonelleri**
  - Bölgesel vaka sayılarını analiz etmek isteyen hekimler, hastane yöneticileri, sağlık politikası uzmanları.
  - Kendi ellerindeki verileri hızlıca analiz edip görselleştirmek isteyen kamu/özel sektör çalışanları.

- **Araştırmacılar ve Akademisyenler**
  - Kendi epidemiyolojik araştırmalarında veriyi ön analiz aşamasında hızlıca değerlendirmek isteyen bilim insanları.
  - Düşük teknik giriş engeliyle prototip analitik uygulamaları test etmek isteyen yüksek lisans/doktora öğrencileri.

- **Öğrenciler ve Yeni Başlayanlar**
  - Veri analizi, Python ve Streamlit ile pratik yapmak isteyen giriş seviyesindeki öğreniciler.
  - Kaggle gibi platformlara hazırlık yapmak veya portföy oluşturmak isteyen öğrenciler.


## <img width="500" height="500" alt="Sprints" src="https://github.com/user-attachments/assets/5e8fcaef-d49e-4465-899f-93a0f86924d5" />


# Sprint Notları (Sprint 1 - MVP)
Proje yönetimi için Notion kullanılmış ve sprint panosu Kanban yapısıyla oluşturulmuştur.  
Uygulama arayüzü Streamlit kullanılarak oluşturulmuştur.  
Projenin temel amacı olan veri yükleme, analiz etme ve ilk grafik oluşturma işlevleri Sprint 1 içerisinde tamamlanmıştır.  
Kullanıcıdan veri alabilen, sütunları tanıyabilen ve zaman serisi grafiği çizebilen ilk prototip başarıyla geliştirilmiştir.  
Klasör yapısı, gereksinim dosyaları ve ilk veri temizleme süreçleri bu sprintte tamamlanmıştır.

---

## Sprint Amacı

Bu sprintte EpiCast projesinin temel yapı taşları atıldı.  
Uygulamanın klasör yapısı kuruldu, kullanıcıdan CSV dosyası alma ve önizleme işlevi geliştirildi.  
Tarih ve vaka sütunlarının tanınması, zaman grafiği çizimi ve veri özetlerinin çıkarılması başarıyla gerçekleştirildi.  
Ayrıca, temel hata yönetimi yapısı da ilk kez entegre edildi.

---

## Tahmin Edilen Tamamlanacak Puan: 100 puan

Sprint 1 için toplam hedef puan 100 puan olarak belirlenmiştir.  
Bu değer, sprint başlangıcında takımın kapasitesi ve haftalık çalışma temposuna göre sabitlenmiş ve görevler bu puan üzerinden orantılı olarak puanlandırılmıştır.  
Görevler, zorluk derecesi, kapsamı ve tamamlanma süresine göre 5 ile 15 puan arasında değerlendirilmiştir.

| Görev Adı                                          | Puan |
|----------------------------------------------------|------|
| Proje klasör yapısının oluşturulması               | 10   |
| Streamlit kurulumu ve ilk test                     | 10   |
| Dosya yükleme arayüzünün geliştirilmesi            | 15   |
| Pandas ile veri okuma ve sütun adlarının temizlenmesi | 10 |
| Tarih ve vaka sütununun otomatik tanımlanması      | 10   |
| Zaman serisi grafiğinin çizilmesi (Plotly)         | 15   |
| Temel veri özetlerinin hesaplanması ve yazılması   | 10   |
| Hata yönetimi ve kullanıcı uyarı sistemlerinin eklenmesi | 10 |
| Notion Kanban panosunun oluşturulması              | 5    |
| README.md dosyasının başlatılması ve açıklama eklenmesi | 5 |

**Toplam: 100 puan**

---

## Product Backlog ve Sprint Takibi

EpiCast projesinde klasik anlamda yapılandırılmış bir backlog yerine, çevik (agile) metodolojilere daha uygun, dinamik ve pratik bir görev yönetimi yaklaşımı benimsenmiştir.  
Bu sistem sayesinde ekip, değişen ihtiyaçlara anında adapte olmuş ve gereksiz bürokrasiye takılmadan ilerlemiştir.

---

## Görev Yönetimi Yapısı

Görevler, Notion tabanlı bir Kanban Panosu üzerinde üç ana sütun altında takip edilmiştir:

- **To Do** → Başlamaya hazır, tanımı netleştirilmiş görevler  
- **In Progress** → Üzerinde aktif olarak çalışılan görevler  
- **Done** → Tamamlanarak kapanan görevler  

Bu yapı sayesinde:

- Süreç her an gözlemlenebilir hale gelmiş,  
- Takım içi sorumluluklar şeffaf bir biçimde dağılmış,  
- Her ekip üyesi, güncel durumu anlık olarak takip edebilmiştir.  

---

## Takım İçi İşleyiş

Görev dağılımı, ekip üyelerinin uzmanlık alanlarına ve sprint önceliklerine göre yapılmıştır.  
Veri işleme, arayüz tasarımı, hata yönetimi ve dosya yapısı tek pano üzerinde takip edilmiştir.  
Görevler günlük olarak gözden geçirilmiş, “In Progress” sütununda yığılmaların önüne geçilmiştir.

---

## Sprint Bazlı Yol Haritası

- **Sprint 1** – Temel Altyapı & İlk Arayüzler  
  Projenin teknik ve yapısal altyapısı oluşturuldu.  
  CSV yükleme, veri önizleme, tarih/vaka sütunu tanıma ve zaman grafiği çizimi başarıyla entegre edildi.

- **Sprint 2** – Tahmin Motoru & Harita & Otomatik Yorum  
  Kullanıcının yüklediği verilere göre 7 günlük vaka tahmini yapıldı.  
  Choropleth harita, AI yorumlama sistemi ve hastalık bazlı açıklamalar eklendi.

- **Sprint 3** – Gelişmiş Tahmin ve Özelleştirme  
  Tahmin süresi kullanıcının belirleyeceği şekilde esnetilecek.  
  UI/UX sadeleştirilecek, yeni kullanıcı testleri yapılacak ve ileri seviye modeller (Prophet vb.) için hazırlık yapılacak.

---

## Daily Scrum (Günlük Scrum Toplantıları)

EpiCast projesi kapsamında ekip içi iletişim ve senkronizasyonu sağlamak amacıyla günlük kısa toplantılar gerçekleştirilmiştir.

### Toplantı Yöntemi:

- WhatsApp grup konuşmaları  
- Google Meet üzerinden teknik görüşmeler

## <img width="1918" height="898" alt="7 temmuz toplantı Ekran görüntüsü 2025-07-07 184238" src="https://github.com/user-attachments/assets/ca47de1d-0d5c-4538-8880-a4a13fae4533" />
## ![Toplantı ss1](https://github.com/user-attachments/assets/85d6e7e8-f93b-4559-a56a-e9479693559f)
## ![toplantı ss2](https://github.com/user-attachments/assets/4e9e59f4-7eca-4cbf-90bf-a74d1db9632b)

### Toplantı Süresi:
- Ortalama 15-20 dakika

### Toplantı Konuları:

- Günlük görevlerin paylaşılması  
- Karşılaşılan teknik veya organizasyonel sorunların aktarılması  
- Bir sonraki adımda yapılacak işlerin netleştirilmesi  
- Notion Sprint panosu üzerinden durum güncellemeleri yapılması

## Sprint 1 Review

Sprint 1 sonunda projenin temel taşları başarıyla atılmıştır.  
Veri yükleme, arayüz oluşturma, sütun tanıma ve zaman grafiği işlevleri tamamlanmıştır.  
Kod yapısı sade, okunabilir ve yeniden kullanılabilir şekilde organize edilmiştir.  
Uygulamanın ilk versiyonu çalışır durumdadır ve MVP koşullarını karşılamaktadır.

---

## Sprint Retrospective

- Görevler daha küçük, yönetilebilir parçalara bölündü.  
- Sütun adlarının farklı varyasyonlarını tanıyacak şekilde kod esnekleştirildi.  
- Hata yönetimi ile kullanıcı deneyimi artırıldı.  
- UI şimdilik temel tutuldu, ilerleyen sprintlerde sadeleştirilecek.  
---


# Sprint Notları (Sprint 2)

Sprint 2, EpiCast projesinde fonksiyonel derinliğin arttığı ve uygulamanın gerçek değer önerisini kullanıcıya sunmaya başladığı sprint olmuştur.  
Bu aşamada sadece veri görüntüleme değil, veriye dayalı içgörü üretme ve öngörü sağlama odaklı modüller geliştirilmiştir.

## Sprint Amacı

Bu sprintte temel işlevlerin ötesine geçilerek:

- 7 günlük tahmin motorunun entegre edilmesi,  
- Otomatik eğilim analizlerinin kullanıcıya sunulması,  
- Seçilen hastalığa özel açıklamaların verilmesi,  
- Dünya haritası üzerinden vaka yoğunluğunun görselleştirilmesi,  
- Farklı formatlardan gelen verilerin uyarlanabilir hâle getirilmesi hedeflenmiştir.

Uygulamanın artık sadece “gösteren” değil, aynı zamanda “yorumlayan” bir analitik araca dönüşmesi Sprint 2’nin odak noktası olmuştur.

---

## Tahmin Edilen Tamamlanacak Puan: 120 puan

| Görev Adı                                                       | Puan |
|------------------------------------------------------------------|------|
| Linear Regression ile tahmin fonksiyonunun yazılması             | 15   |
| Tahmin sonuçlarının grafikle gösterilmesi                        | 15   |
| Otomatik yorum çıkarım motorunun geliştirilmesi                  | 15   |
| Hastalık seçimi için arayüz ve dinamik açıklama entegrasyonu     | 15   |
| Plotly Choropleth ile harita modülünün geliştirilmesi            | 15   |
| CSV veri uyumluluğunun artırılması (sütun adlarının normalize edilmesi) | 10   |
| Hatalı veri yüklemeye karşı uyarı sisteminin detaylandırılması   | 10   |
| Kod yapısının daha modüler hale getirilmesi                      | 10   |
| README güncellemeleri ve örnek veri dokümantasyonu               | 10   |
| Notion sprint tablosunun güncellenmesi ve günlük iş takibi       | 5    |

**Toplam: 120 puan**

---

## Sprint Board Güncellemeleri

Sprint 2 görevleri Notion panosunda 3 sütun altında takip edildi:

- **To Do**  
  Tahmin modülü tasarımı, ülke sütunu tanıma geliştirmesi, UI güncellemeleri

- **In Progress**  
  Plotly harita testleri, AI yorumlama sistemi, hata kontrolleri

- **Done**  
  Tahmin grafiği, veri sütun uyarlaması, hastalık açıklamaları, testler

##  <img width="1197" height="802" alt="Sprint 2 Notion Kanban Tablosu" src="https://github.com/user-attachments/assets/66bccec6-4a09-404e-ad62-cace630bca6d" />

## Daily Scrum

Toplantılar günlük olarak WhatsApp üzerinden yazılı olarak yapıldı.

## Screenshot

- Tahminli vaka grafiği: Gerçek ve tahmini veriler aynı çizgide.
## ![SS](https://github.com/user-attachments/assets/57e6b0fa-0634-4b3b-b1e6-f79cdfe6ef51)

- Harita ekranı: Ülkelere göre yoğunluk renk skalası.
## ![SS2](https://github.com/user-attachments/assets/b2534c88-34c0-4636-8f3b-f69515b122fc)

- UI: Hastalık seçimi ve açıklama kutusu ekran görüntüsü.
## ![SS3](https://github.com/user-attachments/assets/34c61942-28e2-49ea-8d09-50d6592248dd)


## Sprint 2 Review

Sprint 2 sonunda EpiCast uygulaması aşağıdaki kazanımlara ulaşmıştır:

- Kullanıcı artık sadece geçmişi değil, geleceği de görebiliyor.
- 7 günlük tahmin algoritması çalışır ve yorumlayabilir durumdadır.
- Uygulama hastalığa özgü davranıyor: COVID-19 için varyant uyarısı, Zika için hamile birey uyarısı gibi açıklamalar dinamik olarak sunuluyor.
- Veriye göre otomatik eğilim çıkarılıyor: artış, düşüş, sabitlik gibi özetler anında veriliyor.
- Harita özelliğiyle vaka dağılımı coğrafi olarak incelenebilir hale geldi.
- CSV’lerin farklı biçimlerde gelmesi sorun olmaktan çıktı, sistem adaptif hale getirildi.
- Kullanıcıya hata vermeden, doğru bilgi sunan, sağlam bir temel oturtuldu.

## Sprint Retrospective

- Tahmin süreci ayrı fonksiyon olarak yazıldı, kod daha okunabilir hale getirildi.
- Harita modülü sayesinde uygulamanın görsel gücü ciddi şekilde arttı.
- Yorumlama dili sade ve anlaşılır hale getirildi (teknik terimlerden kaçınıldı).
- Kod genel CSV formatları için esnekleştirildi, test dosyalarıyla uyumlu hale geldi.
- Kullanıcı deneyimi açısından rehberli akış güçlendirildi.
- UI sade tutuldu, ancak içeriksel olarak ciddi bir atılım yapıldı.

##  Sprint Notları (Sprint 3)

###  Sprint Tanımı  
Sprint 3, EpiCast uygulamasının teknik açıdan kararlılığını artmıştır. Model doğruluğunu korumak amacıyla yeniden optimize edilen bir geliştirme süreci olmuştur. Ayrıca bu sprint, uygulamanın ilk kez yayınlandığı ve kullanıcıya sunulduğu sprinttir.
---
###  Sprint Amacı  
Bu sprintte, uygulamanın üretime hazır hale getirilmesi hedeflenmiştir. Özellikle:

- Mevcut 7 günlük tahmin sisteminin **14 güne çıkarılması**,  
- Veri eksikliklerinden etkilenmeden çalışan **hata toleranslı bir tahmin akışı**,  
- Otomatik sütun tanıma (tarih, vaka sayısı) yeteneği,  
- Uygulamanın **Render** üzerinde yayınlanması ve test edilmesi,  
- Harita yorumlarının sabitlenmesi ve UI düzenlemeleri,

hedeflenmiştir.

---

### Tahmin Edilen Tamamlanacak Puan: 130 puan

| Görev Adı                                                                 | Puan |
|---------------------------------------------------------------------------|------|
| 14 günlük tahmin modelinin geliştirilmesi (Linear Regression ile)        | 20   |
| Eksik veri senaryoları için toleranslı giriş yapısının oluşturulması     | 15   |
| Uygulamanın Render üzerinden yayına alınması                              | 20   |
| requirements.txt dosyasının oluşturulması ve deploy testlerinin yapılması| 10   |
| Sütun adlarının otomatik tespiti (datetime, vaka vs.)                     | 15   |
| UI güncellemeleri: boş ekran yönetimi, sadeleştirme                       | 10   |
| Harita modülünün yorumlarla sabitlenmesi                                  | 15   |
| Proje dökümantasyonu, örnek veri ve README düzenlemeleri                  | 15   |
| Sprint sürecinin Notion üzerinden günlük olarak takip edilmesi           | 10   |

**Toplam Puan: 130**

---

### Sprint Board Güncellemeleri

Sprint 3 tüm görevler başarıyla tamamlanmıştır.  
“To Do” veya “In Progress” sütununda **hiçbir açık görev kalmamıştır.**

| Durum     | Görevler                                                                 |
|-----------|--------------------------------------------------------------------------|
| Done   | 14 günlük tahmin, eksik veri desteği, otomatik sütun algılama, UI sadeleştirme, harita yorumları, Render yayını, deploy testi, README |

---

### 🗓Daily Scrum  
Toplantılar saat WhatsApp üzerinden gerçekleştirilmiştir.  
Temel gündem başlıkları:

- 60 günlük tahminlerde ortaya çıkan hata eğilimlerinin analizi  
- LinearRegression modeline veri hazırlık optimizasyonları  
- Yayın öncesi test planı ve kontroller  
- requirements.txt kurulabilirliği  
- Kullanıcı dosyalarında tarih-sütun adı farklılıklarına karşı çözüm

---

### 🖼️ Screenshot Açıklamaları  

- **SS1:** 14 günlük tahmin grafiği – Gerçek ve öngörülen değerler  
- **SS2:** Harita görselleştirmesi – Ülkelere göre yoğunluk ve açıklama  
- **SS3:** Yayın öncesi boş ekran kontrolü ve yükleme sonrası grafik oluşumu

---

### Sprint Review

Sprint sonunda EpiCast uygulaması:

- 14 günlük tahmin yapabilen kararlı bir modele sahip hale gelmiştir.  
- Eksik veri içeren CSV dosyalarında çalışabilirlik kazanmıştır.  
- Otomatik sütun tespitiyle kullanıcı etkileşimi kolaylaştırılmıştır.  
- UI sadeleştirilmiş, hata mesajları daha kullanıcı dostu hale getirilmiştir.  
- Uygulama Render.com üzerinden ilk kez yayına alınmış ve test edilmiştir.  
- Belgeler, örnek veri ve görsellerle desteklenmiş bir sürüm teslim edilmiştir.

---

### ♻️ Sprint Retrospective  

**İyi Gidenler:**
- Yayın süreci ilk denemede sorunsuz tamamlandı  
- Tahmin çıktısı düzgün ve anlaşılır grafiklerle sunuldu  
- Kodlar okunabilir ve modüler yapıda geliştirildi  
- Tüm görevler sprint sonunda eksiksiz tamamlandı

**Geliştirilecekler:**
- Gelecekte farklı modellerle (Prophet, ARIMA, LSTM) uzun vadeli tahmin doğruluğu artırılmalı  
- Harita modülü etkileşimli hale getirilmeli (filtreleme, hover, zoom)  
- Mobil kullanıcı deneyimi detaylı test edilmeli  
- İleri seviyede kullanıcılar için veri export (CSV, JSON) gibi fonksiyonlar eklenmeli

---

### 🌍 Yayın Adresi
🔗 [https://epicast.onrender.com](https://epicast.onrender.com)


