# import requests
# import time

# BOT_TOKEN = "8565181976:AAEkmidgHitCp0ZQBAkI1TFGenrIEZf_-nA"
# CHAT_ID = "5756718752"

# URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# def send(msg):
#     requests.post(URL, json={"chat_id": CHAT_ID, "text": msg})

# def ict_observation():
#     return (
#         "🧠 ICT PRACTICE OBSERVATION\n\n"
#         "• Smooth equal lows detected\n"
#         "• Internal liquidity likely resting below\n"
#         "• Watch for displacement & MSS\n\n"
#         "Observation only — manual validation"
#     )

# if __name__ == "_main_":
#     send("✅ ICT Learning Bot started.")
#     while True:
#         send(ict_observation())
#         time.sleep(300)  # every 5 minutes

# import requests
# import time

# BOT_TOKEN = "8565181976:AAEkmidgHitCp0ZQBAkI1TFGenrIEZf_-nA"
# CHAT_ID = "5756718752"

# URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# def send(msg):
#     try:
#         r = requests.post(URL, json={"chat_id": CHAT_ID, "text": msg})
#         print("Message sent:", msg)
#         print("Telegram response:", r.status_code, r.text)
#     except Exception as e:
#         print("Error sending message:", e)

# def ict_observation():
#     return (
#         "🧠 ICT PRACTICE OBSERVATION\n\n"
#         "• Smooth equal lows detected\n"
#         "• Internal liquidity likely resting below\n"
#         "• Watch for displacement & MSS\n\n"
#         "Observation only — manual validation"
#     )

# if __name__ == "__main__":
#     print("🚀 Bot Engine Started")
#     send("✅ ICT Learning Bot started.")

#     while True:
#         send(ict_observation())
#         time.sleep(300)  # every 5 minutes

# import requests
# import time
# from datetime import datetime

# BOT_TOKEN = "8565181976:AAEkmidgHitCp0ZQBAkI1TFGenrIEZf_-nA"
# CHAT_ID = "5756718752"

# URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# def send(msg):
#     requests.post(URL, json={"chat_id": CHAT_ID, "text": msg})

# def wait_for_m5_close():
#     while True:
#         now = datetime.now()
#         if now.minute % 5 == 0 and now.second == 0:
#             return
#         time.sleep(1)

# def ict_observation():
#     return (
#         "🧠 ICT OBSERVATION (M5 Close)\n\n"
#         "• Watch for liquidity sweeps\n"
#         "• Is structure shifting?\n"
#         "• Where is price likely drawn?\n\n"
#         "Observation only"
#     )

# if __name__ == "__main__":
#     send("✅ ICT Learning Bot running.\nWaiting for M5 close...")
#     while True:
#         wait_for_m5_close()
#         send(ict_observation())
#         time.sleep(1)  # avoid duplicate alerts


# import requests
# import time
# from datetime import datetime

# BOT_TOKEN = "8565181976:AAEkmidgHitCp0ZQBAkI1TFGenrIEZf_-nA"
# CHAT_ID = "5756718752"


# TG_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
# BINANCE_URL = "https://api.binance.com/api/v3/klines"

# SYMBOL = "BTCUSDT"
# INTERVAL = "5m"

# last_close_time = None

# def send(msg):
#     requests.post(TG_URL, json={"chat_id": CHAT_ID, "text": msg})

# def get_last_closed_m5():
#     params = {
#         "symbol": SYMBOL,
#         "interval": INTERVAL,
#         "limit": 2
#     }
#     data = requests.get(BINANCE_URL, params=params).json()

#     candle = data[-2]  # last CLOSED candle
#     return {
#         "open_time": candle[0],
#         "close_time": candle[6],
#         "open": float(candle[1]),
#         "high": float(candle[2]),
#         "low": float(candle[3]),
#         "close": float(candle[4])
#     }

# def build_message(c):
#     close_time = datetime.fromtimestamp(c["close_time"] / 1000).strftime("%H:%M")

#     return (
#         "🕯️ M5 Candle Closed (Binance)\n\n"
#         f"⏰ Time: {close_time}\n"
#         f"📈 Open: {c['open']}\n"
#         f"📊 High: {c['high']}\n"
#         f"📉 Low: {c['low']}\n"
#         f"📌 Close: {c['close']}"
#     )

# if __name__ == "__main__":
#     send("✅ Binance M5 Live Engine Started")

#     while True:
#         try:
#             candle = get_last_closed_m5()

#             if candle["close_time"] != last_close_time:
#                 last_close_time = candle["close_time"]
#                 send(build_message(candle))
#                 print("M5 candle closed & sent")

#         except Exception as e:
#             print("Error:", e)

#         time.sleep(10)  # poll every 10 sec


# # ict_bot.py (webhook version)
# from flask import Flask, request, jsonify
# import requests


# BOT_TOKEN = "8565181976:AAEkmidgHitCp0ZQBAkI1TFGenrIEZf_-nA"
# CHAT_ID = "5756718752"
# URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# def send(msg):
#     requests.post(URL, json={"chat_id": CHAT_ID, "text": msg})

# app = Flask(__name__)

# # Last 2 candles memory
# @app.route("/webhook", methods=["POST"])
# def webhook():
#     data = request.json
#     symbol = data.get("symbol")
#     timeframe = data.get("timeframe")
#     low = data.get("low")
#     high = data.get("high")
#     close = data.get("close")

#     if not hasattr(webhook, "candles"):
#         webhook.candles = []
#     webhook.candles.append([low, high, close])
#     if len(webhook.candles) > 2:
#         webhook.candles = webhook.candles[-2:]

#     smooth_low = webhook.candles[-2][0] == webhook.candles[-1][0]
#     smooth_high = webhook.candles[-2][1] == webhook.candles[-1][1]

#     message = f"🧠 ICT OBSERVATION (M5)\nMarket: {symbol}\nTimeframe: {timeframe}\n\n"
#     if smooth_low:
#         message += "• Smooth low detected ✅\n• Liquidity likely resting below\n"
#     if smooth_high:
#         message += "• Smooth high detected ✅\n• Liquidity likely resting above\n"
#     if not smooth_low and not smooth_high:
#         message += "• No smooth highs/lows detected\n"
#     message += "Observation only — manual validation"

#     send(message)
#     return jsonify({"status": "ok"})

# if __name__ == "__main__":
#     send("✅ ICT Learning Bot Phase 2 (real NIFTY) running.")
#     app.run(port=5000)


from flask import Flask, request, jsonify
import requests
import os

# Use environment variables (Railway Variables)
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send(msg):
    requests.post(URL, json={"chat_id": CHAT_ID, "text": msg})

app = Flask(__name__)

# ✅ ROOT ROUTE (THIS FIXES "Not Found")
@app.route("/", methods=["GET"])
def root():
    return jsonify({"status": "server running"})

# Last 2 candles memory
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}

    symbol = data.get("symbol")
    timeframe = data.get("timeframe")
    low = data.get("low")
    high = data.get("high")
    close = data.get("close")

    if not hasattr(webhook, "candles"):
        webhook.candles = []

    webhook.candles.append([low, high, close])
    if len(webhook.candles) > 2:
        webhook.candles = webhook.candles[-2:]

    if len(webhook.candles) < 2:
        return jsonify({"status": "waiting for more candles"})

    smooth_low = webhook.candles[-2][0] == webhook.candles[-1][0]
    smooth_high = webhook.candles[-2][1] == webhook.candles[-1][1]

    message = (
        f"🧠 ICT OBSERVATION (M5)\n"
        f"Market: {symbol}\n"
        f"Timeframe: {timeframe}\n\n"
    )

    if smooth_low:
        message += "• Smooth low detected ✅\n• Liquidity likely resting below\n"
    if smooth_high:
        message += "• Smooth high detected ✅\n• Liquidity likely resting above\n"
    if not smooth_low and not smooth_high:
        message += "• No smooth highs/lows detected\n"

    message += "\nObservation only — manual validation"

    send(message)
    return jsonify({"status": "ok"})

# ❌ DO NOT USE app.run() ON RAILWAY
