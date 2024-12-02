import json
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from config import TELEGRAM_TOKEN

with open("verdades_y_retos.json", "r", encoding="utf-8") as file:
    verdades_y_retos = json.load(file)
    

# Estados para el ConversationHandler
ESPERANDO_NOMBRE, JUGANDO = range(2)

# Diccionario para almacenar los jugadores por chat_id
jugadores_por_chat = {}

# Lista de verdades y retos
verdades = verdades_y_retos["verdades"]

retos = verdades_y_retos["retos"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Juego iniciado por", update.effective_user.first_name)
    chat_id = update.effective_chat.id
    jugadores_por_chat[chat_id] = []
    await update.message.reply_text(
        "¡Bienvenido al juego de Verdad o Reto! 🎮\n"
        "Para comenzar, escribe el nombre del primer jugador.\n"
        "Cuando termines de agregar jugadores, escribe /listo."
    )
    return ESPERANDO_NOMBRE


async def agregar_jugador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    nombre = update.message.text.strip()

    if chat_id not in jugadores_por_chat:
        jugadores_por_chat[chat_id] = []
        print("Jugadores por chat:", jugadores_por_chat)
    if nombre in jugadores_por_chat[chat_id]:
        await update.message.reply_text("Ese nombre ya está en la lista. Por favor, elige otro.")
    else:
        jugadores_por_chat[chat_id].append(nombre)
        await update.message.reply_text(
            f"Jugador {nombre} agregado. 🎉\n"
            "Ingresa el nombre del siguiente jugador o escribe /listo."
        )
    return ESPERANDO_NOMBRE


async def listo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if len(jugadores_por_chat.get(chat_id, [])) < 2:
        await update.message.reply_text(
            "Se necesitan al menos 2 jugadores para empezar. Ingresa más nombres."
        )
        return ESPERANDO_NOMBRE

    jugadores = ", ".join(jugadores_por_chat[chat_id])
    keyboard = [[InlineKeyboardButton("¡Elegir jugador! 🎲", callback_data="elegir_jugador")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"¡Comienza el juego! Los jugadores son: {jugadores}\n"
        "Pulsa el botón para elegir un jugador al azar.",
        reply_markup=reply_markup,
    )
    return JUGANDO


async def elegir_jugador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id
    jugador_elegido = random.choice(jugadores_por_chat[chat_id])

    keyboard = [
        [
            InlineKeyboardButton("Verdad 🤔", callback_data=f"verdad_{jugador_elegido}"),
            InlineKeyboardButton("Reto 🎯", callback_data=f"reto_{jugador_elegido}"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        f"¡{jugador_elegido} ha sido elegido! 🎲\nElige una opción:",
        reply_markup=reply_markup,
    )


async def manejar_eleccion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data.split("_")
    tipo, jugador = data[0], data[1]

    if tipo == "verdad":
        mensaje = f"🤔 {jugador}, tu pregunta es:\n\n{random.choice(verdades)}"
    else:
        mensaje = f"🎯 {jugador}, tu reto es:\n\n{random.choice(retos)}"

    keyboard = [[InlineKeyboardButton("Siguiente jugador 🎲", callback_data="elegir_jugador")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(mensaje, reply_markup=reply_markup)


def main():
    """Punto de entrada del bot."""
    if not TELEGRAM_TOKEN:
        print("Error: TELEGRAM_TOKEN no configurado.")
        return

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ESPERANDO_NOMBRE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, agregar_jugador),
                CommandHandler("listo", listo),
            ],
            JUGANDO: [
                CallbackQueryHandler(elegir_jugador, pattern="^elegir_jugador$"),
                CallbackQueryHandler(manejar_eleccion, pattern="^(verdad|reto)_"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)

    print("Bot iniciado.")
    application.run_polling()


if __name__ == "__main__":
    main()
