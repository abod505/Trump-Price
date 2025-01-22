import requests
import telebot
import time

# Token of your bot
TOKEN = '7674590436:AAFjTPd2v3zSn8lz267x_JTM7hu2ZXTuY-g'
# Channel username (should be in the format @channelusername)
CHANNEL_ID = '@eee0ee0waooqwk'

bot = telebot.TeleBot(TOKEN)

def get_price():
    try:
        url = 'https://api.binance.com/api/v3/ticker/price?symbol=TRUMPUSDT'
        response = requests.get(url)
        data = response.json()
        price = data.get('price')
        
        if price:
            return price
        else:
            print("Error: No price found in the response")
            return None
    except Exception as e:
        print(f"Error getting price: {e}")
        return None

def send_price_update():
    price = get_price()
    if price:
        message = f'{price}$'
        bot.send_message(CHANNEL_ID, message)
    else:
        print("Price is None, skipping the update")

while True:
    send_price_update()
    time.sleep(60)  # Update every minute
