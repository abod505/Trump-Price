import os
import requests
import telebot
from flask import Flask

# تعريف التوكن الخاص بالبوت
TOKEN = "7674590436:AAFjTPd2v3zSn8lz267x_JTM7hu2ZXTuY-g"
bot = telebot.TeleBot(TOKEN)

# معرف القناة التي سيتم إرسال الرسائل إليها
CHANNEL_ID = "@eee0ee0waooqwk"

# إعداد التطبيق باستخدام Flask
app = Flask(__name__)

@app.route('/')
def home():
    price = get_price()
    if price:
        # إرسال السعر إلى القناة
        send_price_update(price)
        return f"The current price of Trump coin is: ${price}"
    else:
        return "Error retrieving the price."

def get_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=trump-coin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        
        # تأكد من وجود السعر في الاستجابة
        if 'trump-coin' in data and 'usd' in data['trump-coin']:
            return data['trump-coin']['usd']
        else:
            print("لم يتم العثور على السعر في الاستجابة")
            return None
    except Exception as e:
        print(f"حدث خطأ أثناء جلب السعر: {e}")
        return None

def send_price_update(price):
    try:
        # إرسال السعر المحدث إلى القناة
        bot.send_message(CHANNEL_ID, f"The current price of Trump coin is: ${price}")
    except Exception as e:
        print(f"حدث خطأ أثناء إرسال الرسالة إلى القناة: {e}")

if __name__ == "__main__":
    # تأكد من أن التطبيق يستمع إلى المنفذ الذي يحدده Heroku
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
