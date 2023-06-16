import pandas as pd
import seaborn as sns

# Veri kümesini oluştur
veri = {
    'Sertifika': [
        'Microsoft Certified: Azure Administrator Associate',
        'CompTIA Security+',
        'AWS Certified Solutions Architect - Associate',
        'Cisco Certified Network Associate (CCNA)',
        'Certified Ethical Hacker (CEH)',
        'Project Management Professional (PMP)',
        'ITIL Foundation',
        'Google Certified Professional Cloud Architect',
        'Certified Data Professional (CDP)',
        'Oracle Certified Professional (OCP)'
    ],
    'Kategori': [
        'Bulut Bilişim',
        'Bilgi Güvenliği',
        'Bulut Bilişim',
        'Ağ Yönetimi',
        'Bilgi Güvenliği',
        'Proje Yönetimi',
        'IT Hizmet Yönetimi',
        'Bulut Bilişim',
        'Veri Yönetimi',
        'Veritabanı Yönetimi'
    ],
    'Maaş Aralığı (USD)': [
        '80000-120000',
        '60000-90000',
        '90000-130000',
        '70000-110000',
        '80000-120000',
        '100000-150000',
        '60000-90000',
        '95000-140000',
        '85000-130000',
        '90000-130000'
    ]
}

df = pd.DataFrame(veri)

# Veri temizleme
df.dropna(inplace=True)

# Veri görselleştirme
sns.countplot(data=df, x='Kategori')
plt.title('Kategorilere Göre Sertifikaların Sayısı')
plt.xlabel('Kategori')
plt.ylabel('Sayı')
plt.show()

sns.stripplot(data=df, x='Kategori', y='Maaş Aralığı (USD)')
plt.title('Kategorilere Göre Maaş Aralığı')
plt.xlabel('Kategori')
plt.ylabel('Maaş Aralığı (USD)')
plt.xticks(rotation=45)
plt.show()
