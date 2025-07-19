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

### Toplantı Günleri:

- 28 Haziran 2025 — Proje yapısı, temel arayüz  
- 29 Haziran 2025 — Veri önizleme ve sütun tanıma  
- 30 Haziran 2025 — Grafik çizimi ve hata yönetimi

### Toplantı Süresi:
- Ortalama 15-20 dakika

### Toplantı Konuları:

- Günlük görevlerin paylaşılması  
- Karşılaşılan teknik veya organizasyonel sorunların aktarılması  
- Bir sonraki adımda yapılacak işlerin netleştirilmesi  
- Notion Sprint panosu üzerinden durum güncellemeleri yapılması

---

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
- Takım içi iletişim verimli bulundu, Notion + WhatsApp + GitHub üçlüsü başarılı çalıştı.

---

