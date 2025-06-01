# Algoritma Greedy 
Algoritma Greedy yang diimplementasikan dalam bot permainan Diamond berfokus pada pengambilan keputusan lokal terbaik di setiap langkah untuk mengoptimalkan pengumpulan diamond. Bot akan menilai setiap objek diamond berdasarkan kriteria tertentu, seperti jarak terdekat (Greedy Distance), nilai poin tertinggi (Greedy Value), atau kombinasi keduanya dengan menghitung rasio nilai terhadap jarak (Greedy Value Distance). Pada setiap iterasi, bot memilih diamond yang paling menguntungkan sesuai kriteria tersebut dan bergerak menuju target tersebut. Selain itu, bot juga memantau kapasitas inventori dan waktu yang tersisa, sehingga dapat kembali ke base untuk menyimpan diamond sebelum inventori penuh atau waktu habis. Pendekatan ini memungkinkan bot untuk membuat keputusan cepat dan efisien secara real-time dengan tujuan memaksimalkan poin yang diperoleh dalam batas waktu dan kapasitas yang tersedia.

# Requirements
Bot dan Game Engine dimuat terpisah. Bagian ini adalah bot starter yang akan digunakan untuk memberikan instruksi pergerakan bot saat permainan. Silahkan ikuti instruksi di bawah ini untuk menyiapkan dependencies yang diperlukan.

[Get Started with Diamond](https://docs.google.com/document/d/1L92Axb89yIkom0b24D350Z1QAr8rujvHof7-kXRAp7c/edit?tab=t.0)

# How to Run 
Sebelum menjalankan bot, pastikan bahwa game engine yang diperlukan pada bagian Get Started with Diamonds telah disiapkan dan dijalankan.
Selanjutnya pindah direktori ke folder src dengan command cd src. Lanjutkan dengan mengikuti instruksi di bawah ini.

1. Command yang dipakai untuk menjalankan bot

```python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team etimo```

2. Jalankan command di bawah ini untuk menjalankan beberapa bot sekaligus

Windows

./run-bots.bat
Linux / (possibly) macOS

./run-bots.sh
Sebelum menjalankan script, ingat untuk mengubah izin script shell agar dapat menjalankan script (linux/macOS)

chmod +x run-bots.sh
Note:
Jika beberapa bot dijalankan bersamaan, pastikan email dan nama unik
Email dapat berupa apapun asalkan masih sesuai dengan sintaks email yang benar
Nama dan password bot dibebaskan dan tanpa spasi
