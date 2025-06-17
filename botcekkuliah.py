import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "1956151616:AAETHsAQ-ex20nYqnroUopl8hiSKBagWtJ0"
API = "https://api.ryzendesu.vip/api/search/mahasiswa"

async def cek_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not context.args:
            await update.message.reply_text("❌ Format: /cek <nama mahasiswa>")
            return
            
        query = " ".join(context.args)
        response = requests.get(f"{API}?query={query}")
        
        if response.status_code != 200:
            await update.message.reply_text("🔧 Sedang ada gangguan pada server API")
            return
            
        data = response.json()
        
        if not data:
            await update.message.reply_text("🔍 Data tidak ditemukan")
            return
            
        # Format response
        result_message = f"🔍 Hasil pencarian untuk '{query}':\n\n"
        for idx, mahasiswa in enumerate(data, 1):
            result_message += (
                f"🏷️ **Nama**: {mahasiswa['nama']}\n"
                f"🔢 **NIM**: {mahasiswa['nim']}\n"
                f"🏛️ **Universitas**: {mahasiswa['nama_pt']}\n"
                f"🎓 **Prodi**: {mahasiswa['nama_prodi']}\n"
                f"────────────────────\n"
            )
            
            # Split message every 10 results untuk menghindari limit panjang pesan
            if idx % 10 == 0:
                await update.message.reply_text(result_message, parse_mode="Markdown")
                result_message = ""  # Reset message
        
        # Kirim sisa hasil yang belum terkirim
        if result_message:
            await update.message.reply_text(result_message, parse_mode="Markdown")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text("⚠️ Terjadi kesalahan saat memproses permintaan")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("cek", cek_handler))
    
    logger.info("📡 Bot successfully connected and running.")
    app.run_polling()

if __name__ == "__main__":
    main()