from textblob import TextBlob

# Daftar contoh ulasan untuk dianalisis
ulasan_list = [
    "Pelayanan ini sangat memuaskan dan cepat!",
    "Barang rusak saat diterima, pengiriman sangat mengecewakan.",
    "Paket sudah diterima tadi siang jam 12.00."
]

print("=== HASIL ANALISIS SENTIMEN ===\n")

for i, teks in enumerate(ulasan_list, 1):
    blob = TextBlob(teks)
    
    # Menerjemahkan otomatis ke bahasa Inggris agar analisis TextBlob akurat
    try:
        teks_en = str(blob.translate(to='en'))
        polaritas = TextBlob(teks_en).sentiment.polarity
    except Exception:
        polaritas = blob.sentiment.polarity

    # Penentuan Kategori: Positif, Negatif, dan Netral
    if polaritas > 0.1:
        sentimen = "Positif 😊"
    elif polaritas < -0.1:
        sentimen = "Negatif 😡"
    else:
        sentimen = "Netral 😐"

    print(f"{i}. Ulasan: \"{teks}\"")
    print(f"   Skor Polaritas : {polaritas:.2f}")
    print(f"   Kategori       : {sentimen}\n")
