bot.py
import telebot

BOT_TOKEN = "8228790952:AAG8sU2vOgKSw7r4O50wVNil9Cx1efa1PQo"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥 *Welcome to the Service Bot!* 🔥\n\n"
        "Choose a service:\n"
        "1️⃣ KRA Nil Returns\n"
        "2️⃣ KRA Normal Returns\n"
        "3️⃣ KRA Debt Forgiveness\n"
        "4️⃣ Website Creation\n"
        "5️⃣ Telegram Bot Creation\n"
        "6️⃣ Netflix Account\n"
        "7️⃣ Virtual Visa Payment Card\n"
        "8️⃣ Cybersecurity / Phishing Info\n\n"
        "Reply with the *number* to continue.",
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda m: True)
def menu_handler(message):
    text = message.text.strip()

    if text == "1":
        bot.send_message(message.chat.id, "✅ KRA Nil Returns — *Price: KSh 150*")
    elif text == "2":
        bot.send_message(message.chat.id, "✅ KRA Normal Returns — *Price depends on complexity*")
    elif text == "3":
        bot.send_message(message.chat.id, "⚖️ KRA Debt Forgiveness — Consultation based")
    elif text == "4":
        bot.send_message(message.chat.id, "🌐 Website creation starts from *KSh 3,000*")
    elif text == "5":
        bot.send_message(message.chat.id, "🤖 Telegram bot creation — *KSh 500*+")
    elif text == "6":
        bot.send_message(message.chat.id, "🎬 Netflix Shared Account — *KSh 50.00/week*")
    elif text == "7":
        bot.send_message(message.chat.id, "💳 Virtual Visa Payment Card — *KSh 50 setup*")
    elif text == "8":
        bot.send_message(message.chat.id, "🛡️ Phishing & Cybersecurity Tools — I’ll guide you *privately* 😶‍🌫️")
    else:
        bot.send_message(message.chat.id, "❗ Unknown option. Send a number 1-8.")

print("Bot is running...")
bot.infinity_polling()
