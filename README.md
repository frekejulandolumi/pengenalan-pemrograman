<br />
<div align="center">
  <a href="https://github.com/frekejulandolumi/pengenalan-pemrograman.git">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">PROGRAM KONVERSI SUHU</h3>

  <p align="center">
    Python Temperature Conversion App — User-Friendly & Interactive
    <br />
    <a href="https://github.com/frekejulandolumi/pengenalan-pemrograman.git"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/frekejulandolumi/pengenalan-pemrograman.git">Report Bug</a>
    &middot;
    <a href="https://github.com/frekejulandolumi/pengenalan-pemrograman.git">Request Feature</a>
  </p>
</div>

## Table of Contents
* [Pendahuluan](#pendahuluan)
* [Fitur Utama](#fitur-utama)
* [Panduan Instalasi](#panduan-instalasi)
* [Panduan Menjalankan Program](#panduan-menjalankan-program)
* [Dokumentasi Teknis](#dokumentasi-teknis)
* [Daftar Kontributor](#daftar-kontributor)

## Pendahuluan
Program Konversi Suhu ini merupakan aplikasi berbasis Python yang dirancang untuk melakukan konversi suhu antara empat skala utama, yaitu Celsius, Fahrenheit, Kelvin, dan Reamur. Program ini menyediakan antarmuka terminal yang interaktif, mudah digunakan, serta dilengkapi dengan tampilan visual berupa Heat-Level Bar yang menunjukkan intensitas panas pada skala 0–10.

Fitur ini membantu pengguna memahami gambaran tingkat panas secara lebih intuitif, tidak hanya melalui angka tetapi juga melalui representasi visual.

Empat skala yang didukung program ini:
* 🌡 Celsius
* ❄️ Fahrenheit
* 🔷 Kelvin
* 🟠 Reamur

Dengan validasi input, tampilan berwarna, dan sistem menu yang jelas, program ini dapat digunakan sebagai alat bantu pembelajaran maupun sebagai aplikasi sederhana untuk memahami konversi suhu.


## Fitur Utama

### Konversi Suhu Antar Skala
  - Dari Celsius ke Fahrenheit, Kelvin, dan Reamur.
  - Dari Fahrenheit ke Celsius, Kelvin, dan Reamur.
  - Dari Kelvin ke Celsius, Fahrenheit, dan Reamur.
  - Dari Reamur ke Celsius, Fahrenheit, dan Kelvin.

### Validasi Input
  - Menangani error jika pengguna memasukkan nilai bukan angka (ValueError).
  - Memberikan pesan khusus jika suhu Kelvin dimasukkan negatif (karena tidak valid).

### Fitur Tambahan Thermometer Skala 1–10
  - Menampilkan intensitas panas dalam bentuk bar visual.
  - Skala 0–10 berdasarkan suhu dalam Celsius.
  - Memberikan status deskriptif:
    - 0 → Sangat Dingin
    - 1–3 → Normal
    - 4–6 → Hangat
    - 7–9 → Panas
    - 10 → Ekstrem

### Menu Interaktif
  - Pengguna dapat memilih satuan suhu awal (Celsius, Fahrenheit, Kelvin, Reamur).
  - Opsi keluar dari program.
  - Program berjalan dalam loop sehingga bisa digunakan berulang kali.

### Fitur Lanjut/Tidak Lanjut
  - Setelah konversi, pengguna ditanya apakah ingin melanjutkan.
  - Jika memilih tidak, program berhenti dengan pesan terima kasih.
    
## Panduan Instalasi

Ikuti langkah-langkah berikut agar program *Konversi Suhu Python* siap dijalankan:

> *💡 Tips:* Pastikan Python versi 3.x sudah terinstal sebelum memulai.



### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/nama-repo.git
```
📌 Catatan: Pastikan koneksi internet stabil supaya clone berhasil.


### 2️⃣ Masuk ke Folder Project
```bash
cd nama-repo
```
✅ Pastikan berada di folder yang benar sebelum melanjutkan step berikutnya. 


### 3️⃣ Buat Virtual Environment (Opsional)
```bash
python -m venv venv
```
Aktifkan:
  - Windows:
    ```bash
    venv\Scripts\activate
    ```
  - Mac/Linux:
    ```bash
    source venv/bin/activate
    ```
📌 Catatan: Virtual environment membantu supaya library program tidak bentrok dengan library Python lain di komputer.

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
💡 Tips: Gunakan pip list untuk cek library sudah terpasang.

⚠️ Jika ada error, coba jalankan python -m pip install --upgrade pip dulu.

## Panduan Menjalankan







## Dokumentasi Teknis
```mermaid
graph TD;

A(start) ---> B[Pilih satuan suhu];

B --> C{Piliihan?};

C -->|1| D[Input suhu Celcius];
C -->|2| E[Input suhu Fahrenheit];
C -->|3| F[Input suhu Kelvin];
C -->|4| G[Input suhu Reamur];
C -->|5| ZA[KELUAR PROGRAM];

%%==== Celcius ====
D -->D1[Hitung Fahrenheit, Kelvin, Reamur];
D1 -->D2[Tampilkan Skala 1-10];
D2 -->D3{Lanjut?};
D3 -->|Ya| B;
D3 -->|Tidak| ZA;

%% ==== Fahrenheit ====
E -->E1[Hitung Celsius , Kevin, Reamur];
E1 -->E2[Tampilkan skala 1-10];
E2 --> E3{Lanjut?};
E3 -->|Ya| B;
F4 -->|Tidak| ZA;

%% ==== Reamur ====
G -->G1[Hitung Celcius, Fahrenheit, Kelvin];
G1 -->G2[Tampilkan Skala 1-10];
G2 -->G3{Lanjut?};
G3 -->|Ya| B;
G3 -->|Tidak| ZA;

ZA --> ZB[Program Selesai]
```






## Daftar Kontributor 👥 

| No|            Nama                |      NIM     |                   GitHub                     |
|---|   ------                       |   --------   |     -----------------------                  |
| 1 |Freke Julando Cristen Lumi      | 250211060081 | https://github.com/frekejulandolumi          |
| 2 |Kharis Evangel Mantiri          | 250211060086 | https://github.com/nimeightysix-86           |
| 3 |Mentari Kristen Rachaelea Toreh | 250211060087 | https://github.com/mentarirachaelea          |
| 4 |Mirecle Zefanya Kapoh           | 250211060088 | https://github.com/mireclezefanyakapoh06-afk |
