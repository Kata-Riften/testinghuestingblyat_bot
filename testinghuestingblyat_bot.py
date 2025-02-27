from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your group chat ID
GROUP_CHAT_ID = -1002495391665  # <-- Your group chat ID

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    start_message = (
        "✍️ Как это работает:\n"
        "Выбираете из списка команд категорию контента, которым хотите поделиться.\n"
        "Чтобы поделиться артом - /suggestArt,\n"
        "Чтобы поделиться мемом - /suggestMeme,\n"
        "Чтобы поделиться фанфиком - /suggestFanfiction,\n"
        "Чтобы поделиться косплеем - /suggestCosplay.\n"
        "Перепутать не страшно, но усложнит задачу модераторам😅 Если вы не уверены, к какой категории относится ваше творчество - специально для вас ✨ /suggestOther - предложить другое✨. "
        "Также по вашему желанию, мы можем указать ваше авторство в посте, или сохранить вашу анонимность😌\n\n"
        "✍️ Правила про контент:\n"
        "1. Контент должен соответствовать тематике сообщества.\n"
        "2. Контент должен быть оригинальным. Плагиат и копирование чужих работ запрещены.\n"
        "3. Запрещено размещение материалов, нарушающих законы РФ или права других пользователей.\n"
        "4. Модераторы оставляют за собой право отклонять контент без объяснения причин.\n\n"
        "✍️ Важно:\n"
        "Любые сообщения, не относящиеся к предложению контента, считаются спамом. За одно спам-сообщение мы выносим предупреждение, за второе - баним в этом боте, канале 'Русы не против Ящерок' и группе 'Русы не против Ящерок chat'. "
        "Просим отнестись с пониманием, мы хотим публиковать качественный контент, и делать это быстро.\n\n"
        "Если у вас остались вопросы, воспользуйтесь командой /faq.\n\n"
        "Благодарим за интерес к игре и ваше творчество!❤️"
    )
    await update.message.reply_text(start_message)

# Command: /suggestArt
async def suggest_art(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    art_message = (
        "Чтобы отправить нам свой арт:\n"
        "1. Прикрепите файл (JPEG, PNG) как документ.\n"
        "2. В сообщении укажите:\n"
        "   - Хотите ли вы, чтобы вас отметили как автора (укажите @юзернейм, если да).\n"
        "   - Любые комментарии или вопросы, относящиеся к контенту и публикации."
    )
    await update.message.reply_text(art_message)

# Command: /suggestMeme
async def suggest_meme(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    meme_message = (
        "Чтобы отправить нам свой мем:\n"
        "1. Прикрепите файл (JPEG, PNG) как документ.\n"
        "2. В сообщении укажите:\n"
        "   - Хотите ли вы, чтобы вас отметили как автора (укажите @юзернейм, если да).\n"
        "   - Любые комментарии или вопросы, относящиеся к контенту и публикации."
    )
    await update.message.reply_text(meme_message)

# Command: /suggestFanfiction
async def suggest_fanfiction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    fanfiction_message = (
        "Чтобы отправить нам свой фанфик:\n"
        "1. Прикрепите текстовый документ или ссылку на опубликованную работу.\n"
        "2. Укажите:\n"
        "   - Хотите ли вы, чтобы вас отметили как автора (укажите @юзернейм, если да).\n"
        "   - Любые комментарии или вопросы, относящиеся к контенту и публикации."
    )
    await update.message.reply_text(fanfiction_message)

# Command: /suggestCosplay
async def suggest_cosplay(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cosplay_message = (
        "Чтобы отправить нам свой косплей:\n"
        "1. Прикрепите файл (JPEG, PNG) как документ.\n"
        "2. В сообщении укажите:\n"
        "   - Хотите ли вы, чтобы вас отметили как автора (укажите @юзернейм, если да).\n"
        "   - Любые комментарии или вопросы, относящиеся к контенту и публикации."
    )
    await update.message.reply_text(cosplay_message)

# Command: /suggestOther
async def suggest_other(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    other_message = (
        "Чтобы отправить нам другое:\n"
        "1. Прикрепите файл: Фото (JPEG, PNG) / Видео (MP4, MOV) / Текстовые файлы (DOC, TXT) / Аудио (MP3).\n"
        "2. Убедитесь, что файлы не превышают ограничения по размеру в Telegram (обычно до 2 ГБ).\n"
        "3. В сообщении укажите:\n"
        "   - Хотите ли вы, чтобы вас отметили как автора (укажите @юзернейм, если да).\n"
        "   - Любые комментарии или вопросы, относящиеся к контенту и публикации."
    )
    await update.message.reply_text(other_message)

# Command: /faq
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    faq_message = (
        "✍️ Часто задаваемые вопросы:\n\n"
        "1. Как отправить контент? — Используйте команду /suggestArt, /suggestMeme, /suggestFanfiction, /suggestCosplay или /suggestOther.\n"
        "2. Какие форматы принимаются? — Фото (JPEG, PNG), видео (MP4, MOV), текст (DOC, TXT), аудио (MP3).\n"
        "3. Как указать авторство? — Укажите @юзернейм в сообщении.\n"
        "4. Что делать, если я не уверен в категории? — Выберите /suggestOther.\n"
        "5. Сколько времени занимает модерация? — Обычно 1-2 дня.\n\n"
        "Если у вас остались вопросы, свяжитесь с модераторами."
    )
    await update.message.reply_text(faq_message)

# Forward all user messages (text, photos, videos, documents, etc.) to the group chat
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Ignore messages from the group chat
        if update.message.chat_id == GROUP_CHAT_ID:
            print("Ignoring message from the group chat.")
            return

        # Get the user's message details
        user_id = update.message.from_user.id
        user_name = update.message.from_user.username or update.message.from_user.first_name
        chat_id = update.message.chat_id

        # Log the message details
        print(f"Received message from user {user_name} (ID: {user_id})")

        # Forward the message to the group chat
        await context.bot.forward_message(chat_id=GROUP_CHAT_ID, from_chat_id=chat_id, message_id=update.message.message_id)
        print(f"Message forwarded to group chat {GROUP_CHAT_ID}")

        # Optionally, reply to the user
        await update.message.reply_text("Ваше сообщение было отправлено модераторам. Спасибо!")
    except Exception as e:
        print(f"Error forwarding message: {e}")

# Main function to start the bot
def main() -> None:
    # Replace 'YOUR_TOKEN' with your actual bot token
    application = Application.builder().token("7750798747:AAGRI0HkCWYaK5tNh64EO3lDBOnnJXDbhb8").build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("suggestArt", suggest_art))
    application.add_handler(CommandHandler("suggestMeme", suggest_meme))
    application.add_handler(CommandHandler("suggestFanfiction", suggest_fanfiction))
    application.add_handler(CommandHandler("suggestCosplay", suggest_cosplay))
    application.add_handler(CommandHandler("suggestOther", suggest_other))
    application.add_handler(CommandHandler("faq", faq))

    # Register a message handler to forward ALL messages (text, photos, videos, documents, etc.)
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, forward_message))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()