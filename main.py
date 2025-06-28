import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN     = os.getenv("8032451598:AAFSODE1uHJrYxe4EdDgatub3z8I4D5yJw8")
AMAZON_TAG    = os.getenv("abhijit015-21")
FLIPKART_TAG  = os.getenv("growthte&affExtParam1=ENKR20250602A1471186402&affExtParam2=3288520
‎")

def convert_amazon(link):
    if "tag=" in link:
        return link
    return f"{link}{'&' if '?' in link else '?'}tag={AMAZON_TAG}"

def convert_flipkart(link):
    if "affid=" in link:
        return link
    return f"{link}{'&' if '?' in link else '?'}affid={FLIPKART_TAG}"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text.strip()
    if "amazon." in txt and "http" in txt:
        out = convert_amazon(txt)
    elif "flipkart." in txt and "http" in txt:
        out = convert_flipkart(txt)
    else:
        out = "❌ Please send a valid Amazon or Flipkart product link."
    await update.message.reply_text(f"🔗  Your affiliate link:\n{out}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    print("✅ Bot is running …")
    app.run_polling()
