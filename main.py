from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("6145869798:AAG8ZjKpWwvmPiJlOykb7Ii7JZL6JgF91c4").build()

app.add_handler(CommandHandler("hello", hello_comand))

app.add_handler(CommandHandler("time", time_comand))

app.add_handler(CommandHandler("help", help_comand))

print ("server start")
app.run_polling()