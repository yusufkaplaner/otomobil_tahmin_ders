not : html arayüzünde csv dosyasindan yararlanilmadi # otomobil_tahmin_ders
# 🚗 Otomobil Fiyat Tahmin Analizi & RegresyonDashboard
**YUSUF KAPLANER | Makine Öğrenmesi Projesi**

Bu repository, otomobil teknik özellikleri ile satış fiyatları arasındaki ilişkiyi analiz etmek için 4 farklı regresyon modelini kıyaslayan kapsamlı bir çalışmayı içermektedir. Proje, model performanslarını (MSE, R²) değerlendirirken, aynı zamanda veriyi interactive (etkileşimli) bir dashboard üzerinden de sunmaktadır.

## 📊 Performans Sonuçları (Tabloyu Doldurun)

Analizler sonucunda elde edilen metrikler, modeller arasındaki başarı farkını net bir şekilde göstermektedir.
"Multiple Linear" ve "Ridge" modellerinin, sadece beygir gücü değil, motor hacmi ve araç ağırlığını da hesaba kattığı için daha başarılı olduğu gözlemlenmiştir.

Model Türü           | MSE        | R-Squared
---------------------------------------------
Simple Linear        | 60.70      | 0.7025
Multiple Linear      | 53.60      | 0.7373
Polynomial (Deg:3)   | 54.96      | 0.7307
Ridge Regression     | 53.61      | 0.7373
---

## 📈 Model Görselleştirmeleri

Proje kapsamında elde edilen grafikler ve analizleri aşağıdadır. Bu grafikleri hocanıza sunarken kullanabilirsiniz.

### 1. Basit ve Çoklu Regresyon Kıyaslaması
| A. Basit Doğrusal Regresyon | B. Çoklu Doğrusal Regresyon (Tahmin Düzlemi) |
| :---: | :---: |
| <img src="./images/graph_simple.png" width="400" alt="Basit Regresyon Grafiği"> | <img src="./images/graph_3d_multiple.png" width="400" alt="3D Çoklu Regresyon Düzlemi"> |
| **Analiz:** Fiyat ile HP arasındaki temel pozitif ilişki. | **Analiz:** 3D düzlemde HP ve Engine Size'ın fiyata birleşik etkisi. |

### 2. Polinomiyal Regresyon (Degree=3)
<img src="./images/graph_polynomial.png" width="600" alt="Polinomiyal Regresyon Grafiği">

**Analiz:** Verideki doğrusal olmayan (non-linear) yapıyı yakalamak için HP'nin 3. dereceden polinomu kullanılmıştır. Yüksek beygirli araçlardaki fiyat artış trendini en iyi açıklayan modeldir.

---

## 🛠️ Kullanılan Teknolojiler & Proje Yapısı

### Proje Dosyaları
* `car_prices.py`: Tüm regresyon analizlerini yapan Python kodu.
* `CarSales.xlsx`: Analizde kullanılan otomobil veri seti.
* `regression_dashboard.html`: İnteraktif sonuç dashboard'u.
* `Lab01YusufKaplaner.docx`: Detaylı laboratuvar raporu.

### Teknolojiler
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"> <img src="https://img.shields.io/badge/Matplotlib-ffffff?style=for-the-badge&logo=matplotlib&logoColor=black" alt="Matplotlib"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML">

---

## 🖥️ İnteraktif Dashboard (Nasıl Çalıştırılır?)

Proje, sonuçları web tabanlı bir dashboard üzerinden interaktif olarak sunmaktadır.
1. `regression_dashboard.html` dosyasını bilgisayarınıza indirin.
2. Tarayıcınızda (Chrome, Edge vb.) çift tıklayarak açın.
3. Modelleri seçip, tahminleri ve performans grafiklerini canlı olarak inceleyebilirsiniz.

> **GitHub Pages İpucu:** Eğer bu HTML'i repository ayarlarından "GitHub Pages" olarak etkinleştirirseniz, buraya tıklanabilir canlı bir link ekleyebiliriz!

---

## 🏁 Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için:

1. Repository'yi klonlayın:
```bash
git clone [https://github.com/yusufkaplaner/otomobil_tahmin_ders.git](https://github.com/yusufkaplaner/otomobil_tahmin_ders.git)
cd otomobil_tahmin_ders
