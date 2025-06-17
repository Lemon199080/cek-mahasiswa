# 🔎 Cari data mahasiswa

Telegram bot sederhana ini memungkinkan pengguna untuk mencari data mahasiswa berdasarkan nama melalui integrasi dengan API eksternal. Dibangun menggunakan Python dan library python-telegram-bot.

---

## 🛠️ Requirements

* Python 3.x
* python-telegram-bot
* requests

---

## 🚀 Instalasi dan Penggunaan

### 1. Clone Repository

```sh
git clone https://github.com/username/repository-bot-mahasiswa.git
cd repository-bot-mahasiswa
```

### 2. Install Dependencies

```sh
pip install python-telegram-bot requests
```

### 3. Konfigurasi

Buka file `bot.py`, lalu pastikan mengganti variabel berikut:

```python
TOKEN = "TOKEN_BOT_TELEGRAM_KAMU"
API = "https://api.ryzendesu.vip/api/search/mahasiswa"  # API endpoint
```

### 4. Jalankan Bot

Jalankan bot menggunakan perintah berikut:

```sh
python bot.py
```

---

## 📖 Cara Menggunakan

Kirimkan text berikut pada bot Telegram:

```
/cek <nama mahasiswa>
```

Contoh:

```
/cek Adjie
```

Bot akan membalas dengan data mahasiswa terkait.

---

## 📌 Struktur Respons

Bot akan mengembalikan informasi:

* 🏷️ Nama
* 🔢 NIM
* 🏛️ Universitas
* 🎓 Program Studi

---


