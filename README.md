# ==================================================== #
#               PROGRAM KONVERSI SUHU                  #
# ==================================================== #



# **Fitur Utama**

1. Konversi Suhu Antar Skala
  - Dari Celsius ke Fahrenheit, Kelvin, dan Reamur.
  - Dari Fahrenheit ke Celsius, Kelvin, dan Reamur.
  - Dari Kelvin ke Celsius, Fahrenheit, dan Reamur.
  - Dari Reamur ke Celsius, Fahrenheit, dan Kelvin.

2. Validasi Input
  - Menangani error jika pengguna memasukkan nilai bukan angka (ValueError).
  - Memberikan pesan khusus jika suhu Kelvin dimasukkan negatif (karena tidak valid).

3. Fitur Tambahan Thermometer Skala 1–10
  - Menampilkan intensitas panas dalam bentuk bar visual.
  - Skala 0–10 berdasarkan suhu dalam Celsius.
  - Memberikan status deskriptif:
    - 0 → Sangat Dingin
    - 1–3 → Normal
    - 4–6 → Hangat
    - 7–9 → Panas
    - 10 → Ekstrem

4. Menu Interaktif
  - Pengguna dapat memilih satuan suhu awal (Celsius, Fahrenheit, Kelvin, Reamur).
  - Opsi keluar dari program.
  - Program berjalan dalam loop sehingga bisa digunakan berulang kali.

6. Fitur Lanjut/Tidak Lanjut
  - Setelah konversi, pengguna ditanya apakah ingin melanjutkan.
  - Jika memilih tidak, program berhenti dengan pesan terima kasih.
