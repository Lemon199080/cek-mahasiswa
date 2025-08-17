# 🔎 Cari data mahasiswa

Telegram bot sederhana ini memungkinkan pengguna untuk mencari data mahasiswa berdasarkan nama melalui integrasi dengan API eksternal.

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

Buka file `bot.py`, lalu ganti variabel berikut:

```python
TOKEN = "TOKEN_BOT_TELEGRAM_KAMU"
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

## 📌 Respons

* 🏷️ Nama
* 🔢 NIM
* 🏛️ Universitas
* 🎓 Program Studi

---


