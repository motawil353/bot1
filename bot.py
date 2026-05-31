import logging
import random
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("8937677235:AAHHHs8OFxl3sZx5Ya2O3zlxBjQL-UM2DfE")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

responses = {
    "قحبتي": ["طيزا", "كسا", "قلبا", "عيونا", "اههه", "اي ياعمري"],
    "لوسي": ["طيزا", "كسا", "قلبا", "عيونا", "اههه", "اي ياعمري"],
    "كيفك": ["ممحونة👅", "هايجة", "هلق صرت تمام"],
    "بدي نيكك": ["جاهزة😍🥰", "كسي ناطرك ياعمري تركبو🥰", "حميانة كتير اجيت بوقتك👄🥰", "بدي مصلك اول 👅😌", "دخيل زبو الحميان انا 😍"],
    "كسمك": ["اححح روح قلبي الذل🥺", "سبني اي 🥺", "ياعمري انا🥺"],
    "كسختك": ["اححح روح قلبي الذل🥺", "سبني اي 🥺", "ياعمري انا🥺"],
    "شو عم تعملي": ["عم اجلخ عصورتك🥺", "عم اتمنى تنيكني👄🥺", "حمياانةةة"],
    "بترضعيلي؟": ["اي اي امانة هلق 🥺🥺🥺"],
    "ايري فيكي": ["من فوق ولا تحت😁", "ياريت"],
    "انتي شو": ["عاهرتك", "شرموطتك", "قحبتك"],
    "شدي حالك": ["اهههه ياعمري مافيني🥺", "لك مافيني مافيني اتحمل👄🥺"],
    "يلعن طيزك": ["بستاهل عاقبني بزبك اذا بتريد👈🏻👉🏻"],
    "بحبك": ["بموت فيك ياعمري 💋"]
}

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip().lower()
    for key, reply_list in responses.items():
        if key in user_message:
            reply_text = random.choice(reply_list)
            await update.message.reply_text(reply_text)
            return

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    print("✅ البوت شغال...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
