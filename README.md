# SistemAnaliziFinalProjesi
Sistem Analizi Final Projesi
Bu projenin amacı, IT sertifikalarını ve bunlarla ilişkili maaş aralıklarını içeren bir veri kümesinde veri 
temizleme ve görselleştirmesini gerçekleştirmektir. 
Veri temizleme adımları, eksik değerler içeren satırların çıkarılmasını ve Maaş Aralığı sütunundaki verilerin uygun formata dönüştürülmesini içerir.
Bu, verileri analiz ve görselleştirme için daha uygun hale getirir. 
Veri görselleştirme adımı, veri setini görselleştirmek için Pandas ve Seaborn kütüphaneleri tarafından sağlanan araçları kullandım.
Çubuk grafikler ve bant grafikler gibi grafik türleri, sertifikaların kategoriye göre dağılımını ve maaş aralıklarının karşılaştırmasını gösterdim.
Özet olarak IT sertifikalarını ve maaşlarını daha iyi anlamanıza yardımcı olmak için verileri düzenledim ve görselleştirdim.

Kod Açıklaması İlk adımda, pandas ve seaborn kütüphanelerini import ettim.

Ardından, bir veri kümesi oluşturdum. Bu veri kümesi, 'Sertifika', 'Kategori' ve 'Maaş Aralığı (USD)' sütunlarından oluşuyor.
Sertifikaların isimleri, kategorileri ve ilgili maaş aralıkları bu veri kümesinde yer alıyor.

Oluşturduğum veri kümesini pd.DataFrame() fonksiyonuyla bir DataFrame'e dönüştürüdüm ve df değişkenine attım.

Veri temizleme adımında, dropna() fonksiyonunu kullanarak eksik değerleri içeren satırları kaldırdım.

Veri görselleştirme kısmında, sns.countplot() fonksiyonunu kullanarak kategorilere göre sertifikaların sayısını gösteren bir çubuk grafiği oluşturdum.
plt.title(), plt.xlabel() ve plt.ylabel() fonksiyonlarıyla grafiği başlıklandırdım ve eksen etiketlerini ekledim. 
Son olarak plt.show() ile grafiği görüntülüledim.

Ardından, sns.stripplot() fonksiyonunu kullanarak kategorilere göre maaş aralığını gösteren bir strip plotu oluşturdum.
plt.title(), plt.xlabel(), plt.ylabel() ve plt.xticks(rotation=45) fonksiyonlarıyla grafiği başlıklandırdım,
eksen etiketlerini ekledim ve x eksenindeki etiketleri 45 derece döndürdüm. Son olarak plt.show() ile grafiği görüntüledim.
