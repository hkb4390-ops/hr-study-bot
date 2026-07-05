import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand

# ========================================================
# 1. BOT SETTINGS & LINKS (UPDATED FOR NEW BOT)
# ========================================================
# New token from BotFather as seen in 1000018816.jpg
BOT_TOKEN = "8858220246:AAEyh1HdH7X4G3Mxr7-pw_ZXrz5tNVNdrBs"
WEB_LINK = "https://bseb-registration-2.vercel.app/"
ADMIN_USERNAME = "@Yadav0001y4gh"  

bot = telebot.TeleBot(BOT_TOKEN)

# ========================================================
# 2. PREMIUM TEXT & MESSAGE TEMPLATES (PROFESSIONAL DESIGN)
# ========================================================
WELCOME_MESSAGE = """
✨ *WELCOME TO PREMIUM STUDENT PORTAL* ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━
Hello 👋 *{user_name}*!

🚀 *Bihar Board (BSEB) Class 10th* ke liye sabhi batches bilkul *FREE* hain! Ghar baithe kariye topper wali padhai.

🎯 **Apni seat confirm karne aur classes shuru karne ke liye niche diye gaye button par click karke registration poora karein.**

⚠️ *Important Instruction:* Link par click karne ke baad, page ko apne phone ke normal browser (Jaise **Chrome** ya **Safari**) mein hi open karein, taaki aapka data safe save ho sake.
━━━━━━━━━━━━━━━━━━━━━━━━━━
📢 *Updates ke liye niche diye gaye menu options ko check karein!*
"""

INFO_MESSAGE = """
ℹ️ *BATCH INFORMATION & DETAILS*
━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 *Course:* BSEB Class 10th (Hindi Medium)
💰 *Fees:* ₹0 (100% FREE Full Batch)
📝 *Syllabus:* Science, Math, Social Science, Hindi, English, Sanskrit.
⚙️ Live Classes, Premium Notes aur Mock Tests bhi shamil hain!

👇 *Abhi register karne ke liye niche button dabayein:*
"""

HELP_MESSAGE = """
🆘 *SUPPORT & HELP DESK*
━━━━━━━━━━━━━━━━━━━━━━━━━━
Registration karne mein koi dikkat aa rahi hai? Don't worry!

1️⃣ Niche diye gaye `🚀 Start Registration` button par click karein.
2️⃣ Agar website load na ho, toh check karein aapka internet on hai ya nahi.
3️⃣ Kisi bhi anya help ya shikayat ke liye seedhe hamare Admin se baat karein.

💬 *Contact Admin:* {admin}
🔄 *Restart Bot:* Try /start anytime.
━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

DISCRETION_MESSAGE = """
📢 *User Discretion & Disclaimer*
━━━━━━━━━━━━━━━━━━━━━━━━━━
*EN:* All content on HR STUDY PUBLISHED is for educational purposes only. We strive for accuracy, but students must verify details with official board guidelines before exams. User discretion is advised.

*HI:* इस चैनल पर उपलब्ध सामग्री केवल शैक्षणिक उद्देश्य के लिए है। हम सटीकता का प्रयास करते हैं, पर छात्र परीक्षा से पहले बोर्ड गाइडलाइंस से मिलान कर लें। अपने विवेक का उपयोग करें।
━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ========================================================
# 3. PREMIUM UI & BUTTONS (REALTIME BEST EXPERIENCE)
# ========================================================
def get_main_markup():
    """Main keyboard template with action, info, support and close button."""
    markup = InlineKeyboardMarkup(row_width=2)
    
    # Primary Call to Action Button (Full Width)
    btn_reg = InlineKeyboardButton(text="🚀 Start Registration", url=WEB_LINK)
    
    # Secondary Options (Row 2)
    btn_info = InlineKeyboardButton(text="📚 Batch Info", callback_data="view_info")
    btn_help = InlineKeyboardButton(text="🆘 Get Help", callback_data="view_help")
    
    # Discretion Button (Row 3)
    btn_disc = InlineKeyboardButton(text="📢 Disclaimer", callback_data="view_discretion")
    btn_close = InlineKeyboardButton(text="❌ Close", callback_data="delete_msg")
    
    # Layout Design
    markup.add(btn_reg)
    markup.add(btn_info, btn_help)
    markup.add(btn_disc, btn_close)
    return markup

def get_back_markup():
    """Back button to return to standard home UI."""
    markup = InlineKeyboardMarkup()
    btn_back = InlineKeyboardButton(text="🔙 Back to Main Menu", callback_data="back_home")
    markup.add(btn_back)
    return markup

def set_bot_menu_options(bot):
    """Sets professional permanent buttons directly in Telegram's interface menu."""
    commands = [
        BotCommand("start", "🚀 Main Menu / Registration"),
        BotCommand("info", "📚 Course Details & Batches"),
        BotCommand("help", "🆘 Customer Support / Admin"),
        BotCommand("disclaimer", "📢 User Discretion & Rules"),
        BotCommand("clear", "❌ Delete Bot Messages Context")
    ]
    bot.set_my_commands(commands)

# ========================================================
# 4. COMMAND HANDLERS
# ========================================================
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_name = message.from_user.first_name
    formatted_msg = WELCOME_MESSAGE.format(user_name=user_name)
    bot.send_message(
        message.chat.id, 
        formatted_msg, 
        parse_mode="Markdown", 
        reply_markup=get_main_markup()
    )

@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(
        message.chat.id, 
        INFO_MESSAGE, 
        parse_mode="Markdown", 
        reply_markup=get_main_markup()
    )

@bot.message_handler(commands=['help'])
def handle_help(message):
    formatted_help = HELP_MESSAGE.format(admin=ADMIN_USERNAME)
    bot.send_message(
        message.chat.id, 
        formatted_help, 
        parse_mode="Markdown", 
        reply_markup=get_back_markup()
    )

@bot.message_handler(commands=['disclaimer'])
def handle_disclaimer(message):
    bot.send_message(
        message.chat.id, 
        DISCRETION_MESSAGE, 
        parse_mode="Markdown", 
        reply_markup=get_back_markup()
    )

@bot.message_handler(commands=['clear'])
def handle_clear(message):
    """Instructional fallback to clear interface clutter manually if desired."""
    bot.send_message(
        message.chat.id, 
        "🧹 *Interface Cleaned!* Aap upar diye gaye kisi bhi message ke `❌ Close` button par click karke use chat se permanent delete kar sakte hain.",
        parse_mode="Markdown"
    )

# ========================================================
# 5. REALTIME CALLBACK QUERIES (CLICK ACTIONS WITHOUT REPOSTING)
# ========================================================
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_actions(call):
    user_name = call.from_user.first_name
    
    if call.data == "view_info":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=INFO_MESSAGE,
            parse_mode="Markdown",
            reply_markup=get_back_markup()
        )
        bot.answer_callback_query(call.id, text="📚 Showing Course Details")

    elif call.data == "view_help":
        formatted_help = HELP_MESSAGE.format(admin=ADMIN_USERNAME)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=formatted_help,
            parse_mode="Markdown",
            reply_markup=get_back_markup()
        )
        bot.answer_callback_query(call.id, text="🆘 Showing Support Desk")

    elif call.data == "view_discretion":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=DISCRETION_MESSAGE,
            parse_mode="Markdown",
            reply_markup=get_back_markup()
        )
        bot.answer_callback_query(call.id, text="📢 Showing Disclaimer")

    elif call.data == "back_home":
        formatted_msg = WELCOME_MESSAGE.format(user_name=user_name)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=formatted_msg,
            parse_mode="Markdown",
            reply_markup=get_main_markup()
        )
        bot.answer_callback_query(call.id, text="🔙 Returned to Home")

    elif call.data == "delete_msg":
        try:
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.answer_callback_query(call.id, text="🗑️ Message deleted successfully!")
        except Exception as e:
            bot.answer_callback_query(call.id, text="❌ Error deleting message.")

# ========================================================
# 6. RUN THE BOT ENGINE
# ========================================================
if __name__ == "__main__":
    print("[LOG] Starting premium engine...")
    try:
        set_bot_menu_options(bot)
        print("[LOG] Professional menu commands injected successfully.")
    except Exception as menu_error:
        print(f"[WARN] Could not sync navigation menu layout: {menu_error}")
        
    print("[SUCCESS] Your professional bot is live and waiting for real-time users!")
    bot.infinity_polling()
