import time
import requests
import telebot

# إعدادات البوت
TOKEN = "7674590436:AAFjTPd2v3zSn8lz267x_JTM7hu2ZXTuY-g"  # توكن البوت
CHANNEL_ID = "@Trump_Price_1"  # معرف القناة
SYMBOL = "TRUMPUSDT"  # رمز العملة على Binance

bot = telebot.TeleBot(TOKEN)

# دالة لجلب سعر العملة
def fetch_trump_price():
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={SYMBOL}"
    try:
        response = requests.get(url)
        data = response.json()
        price = float(data['price'])
        return f"{price:.2f}$"
    except Exception as e:
        return f"خطأ: {e}"

# دالة لإرسال السعر إلى القناة
def send_price_update():
    while True:
        price = fetch_trump_price()
        bot.send_message(CHANNEL_ID, price)
        time.sleep(60)  # تحديث كل دقيقة

if __name__ == "__main__":
    send_price_update()