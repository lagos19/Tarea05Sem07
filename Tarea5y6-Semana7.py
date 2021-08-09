import time

import telebot
from telebot import types

TOKEN = '1914921841:AAE-42JHzeq5VGQW0R8LC1GFJsxYOfo3JE0'

knownUsers = [] 
userStep = {} 

commands = {

    'start'       : '▶️\nIniciar bot\n\n',
    
    'help'        : '🆘\nMuestra todos los comandos disponibles\n\n',
    
    'paises'      : '🌎\nMuestra un teclado personalizado donde usted puede gestionar la informaciones de cada pais'
}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
imageSelect.add('Belice','Guatemala', 'El Salvador', 'Honduras', 'Nicaragua', 'Costa Rica', 'Panama')

hideBoard = types.ReplyKeyboardRemove()  
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("He detectado a un nuevo usuario mas sin envargo no ha usado el comando \"/start\"")
        return 0



def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:
        knownUsers.append(cid)
        userStep[cid] = 0
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡Hola!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Es un gusto ayudarte")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Conmigo puedes gestionar toda la información de todos los paises de Centro America")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "🇧🇿 🇬🇹 🇸🇻 🇭🇳 🇳🇮 🇨🇷 🇵🇦")
        command_help(m)
    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ya usaste el comando /start, usa otro comando, por favor")


@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    help_text = "Por favor, elije un comando o escríbelo\n\n\nEstos son los comandos que estan disponibles:\n\n\n"
    bot.send_chat_action(cid, 'typing')
    time.sleep(5)
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text) 



@bot.message_handler(commands=['paises'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Selecciona una opcion:", reply_markup=imageSelect) 
    userStep[cid] = 1 



@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text

    bot.send_chat_action(cid, 'typing')

    if text == 'Belice': 
        bot.send_message(cid, "🇧🇿")
        bot.send_chat_action(cid, 'record_audio')
        time.sleep(3)
        bot.send_audio(cid, open('Audios\Belice.ogg', 'rb'),
        reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es su bandera:")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('Banderas\Bandera de Belice.png', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ahora te enviare un pequeño documento sobre Belice")
        bot.send_chat_action(cid, 'upload_document')
        time.sleep(3)
        bot.send_document(cid, open('Documentos\Historia de Belice.pdf', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Esta es su ubicación")
        bot.send_chat_action(cid, 'find_location')
        time.sleep(5)
        bot.send_location(cid, 17.250000 , -88.767500)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Este es un pequeño video sobre Belice"),
        bot.send_chat_action(cid, 'upload_video')
        time.sleep(3)
        bot.send_video(cid, "BAACAgEAAxkBAAMaYRCeurIJkp_KsqE8sFGMOOEjfWcAAnIBAAKqArlHVyh2-34CA5cgBA" , 'rb')

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /paises para consultar la información de otro país")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "😎")
        
        userStep[cid] = 0  
    elif text == 'Guatemala':
        bot.send_message(cid, "🇬🇹")
        bot.send_chat_action(cid, 'record_audio')
        time.sleep(3)
        bot.send_audio(cid, open('Audios\Guatemala.ogg', 'rb'),
        reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es su bandera:")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('Banderas\Bandera de Guatemala.png', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ahora te enviare un pequeño documento sobre Guatemala")
        bot.send_chat_action(cid, 'upload_document')
        time.sleep(3)
        bot.send_document(cid, open('Documentos\Historia de Guatemela.pdf', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Esta es su ubicación")
        bot.send_chat_action(cid, 'find_location')
        time.sleep(5)
        bot.send_location(cid, 14.609861 , -90.525250)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Este es un pequeño video sobre Guatemala"),
        bot.send_chat_action(cid, 'upload_video')
        time.sleep(3)
        bot.send_video(cid, "BAACAgEAAxkBAAMcYRCeulZTtkrWPeaSptKlvrIqfi8AAosBAAKqArlH5bZx3UHmQrMgBA" , 'rb')

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /paises para consultar la información de otro país")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "😎")
        
        userStep[cid] = 0  
    elif text == 'El Salvador':
        bot.send_message(cid, "🇸🇻")
        bot.send_chat_action(cid, 'record_audio')
        time.sleep(3)
        bot.send_audio(cid, open('Audios\El-Salvador.ogg', 'rb'),
        reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es su bandera:")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('Banderas\Bandera de El Salvador.png', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ahora te enviare un pequeño documento sobre El Salvador")
        bot.send_chat_action(cid, 'upload_document')
        time.sleep(3)
        bot.send_document(cid, open('Documentos\Historia de El Salvador.pdf', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Esta es su ubicación")
        bot.send_chat_action(cid, 'find_location')
        time.sleep(5)
        bot.send_location(cid, 13.698889 , -89.191389)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Este es un pequeño video sobre El Salvador"),
        bot.send_chat_action(cid, 'upload_video')
        time.sleep(3)
        bot.send_video(cid, "BAACAgEAAxkBAAMZYRCeug6mdMMsRw0DeA5mPa6OxlgAAnQBAAKqArlH9WkcCx2N8jkgBA-2LLDusyPIAQ" , 'rb')

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /paises para consultar la información de otro país")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "😎")
        
        userStep[cid] = 0  
    elif text == 'Honduras':
        bot.send_message(cid, "🇭🇳")
        bot.send_chat_action(cid, 'record_audio')
        time.sleep(3)
        bot.send_audio(cid, open('Audios\Honduras.ogg', 'rb'),
        reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es su bandera:")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('Banderas\Bandera de Honduras.png', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ahora te enviare un pequeño documento sobre Honduras")
        bot.send_chat_action(cid, 'upload_document')
        time.sleep(3)
        bot.send_document(cid, open('Documentos\Historia de Honduras.pdf', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Esta es su ubicación")
        bot.send_chat_action(cid, 'find_location')
        time.sleep(5)
        bot.send_location(cid, 14.094167 , -87.206667)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Este es un pequeño video sobre Honduras"),
        bot.send_chat_action(cid, 'upload_video')
        time.sleep(3)
        bot.send_video(cid, "BAACAgEAAxkBAAMYYRCeuj9OLkgl1M2bcn46U0wChLIAAm4BAAKqArlHGehWHR1wbBEgBA" , 'rb')

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /paises para consultar la información de otro país")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "😎")
        
        userStep[cid] = 0       
    elif text == 'Nicaragua':
        bot.send_message(cid, "🇳🇮")
        bot.send_chat_action(cid, 'record_audio')
        time.sleep(3)
        bot.send_audio(cid, open('Audios\icaragua.ogg' , 'rb' ),
        reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es su bandera:")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('Banderas\Bandera de Nicaragua.png', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ahora te enviare un pequeño documento sobre Nicaragua")
        bot.send_chat_action(cid, 'upload_document')
        time.sleep(3)
        bot.send_document(cid, open('Documentos\Historia de Nicaragua.pdf', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Esta es su ubicación")
        bot.send_chat_action(cid, 'find_location')
        time.sleep(5)
        bot.send_location(cid, 12.150000 , -86.266667)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Este es un pequeño video sobre Nicaragua"),
        bot.send_chat_action(cid, 'upload_video')
        time.sleep(3)
        bot.send_video(cid, "BAACAgEAAxkBAAMWYRCeugAB8rz6KD_QPD9tQ69xXkGiAAJwAQACqgK5R6FY3Lc7qzyxIAQ" , 'rb')

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /paises para consultar la información de otro país")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "😎")
        
        userStep[cid] = 0       
    elif text == 'Costa Rica':
        bot.send_message(cid, "🇨🇷")
        bot.send_chat_action(cid, 'record_audio')
        time.sleep(3)
        bot.send_audio(cid, open('Audios\Costa-Rica.ogg', 'rb'),
        reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es su bandera:")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('Banderas\Bandera de Costa Rica.png', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ahora te enviare un pequeño documento sobre Costa Rica")
        bot.send_chat_action(cid, 'upload_document')
        time.sleep(3)
        bot.send_document(cid, open('Documentos\Historia de Costa Rica.pdf', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Esta es su ubicación")
        bot.send_chat_action(cid, 'find_location')
        time.sleep(5)
        bot.send_location(cid, 10.000000, -84.000000)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Este es un pequeño video sobre Costa Rica"),
        bot.send_chat_action(cid, 'upload_video')
        time.sleep(3)
        bot.send_video(cid, "BAACAgEAAxkBAAMXYRCeumrljDlXEhc34U0EKBr7L2QAAnMBAAKqArlH9ce2ZdnAREUgBA" , 'rb')

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /paises para consultar la información de otro país")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "😎")
        
        userStep[cid] = 0   
    elif text == 'Panama':
        bot.send_message(cid, "🇵🇦")
        bot.send_chat_action(cid, 'record_audio')
        time.sleep(3)
        bot.send_audio(cid, open('Audios\Panamá.ogg', 'rb'),
        reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es su bandera:")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('Banderas\Bandera de Panama.png', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ahora te enviare un pequeño documento sobre Panamá")
        bot.send_chat_action(cid, 'upload_document')
        time.sleep(3)
        bot.send_document(cid, open('Documentos\Historia de Panama.pdf', 'rb'), 
        reply_markup=hideBoard)

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Esta es su ubicación")
        bot.send_chat_action(cid, 'find_location')
        time.sleep(5)
        bot.send_location(cid, 9.000000, -79.500000)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Este es un pequeño video sobre Panamá"),
        bot.send_chat_action(cid, 'upload_video')
        time.sleep(3)
        bot.send_video(cid, "BAACAgEAAxkBAAMbYRCeutqQnRqd5aAAAcRjQBEWllLSAAJxAQACqgK5R-a35PzVdDs4IAQ" , 'rb')

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /paises para consultar la información de otro país")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "😎")
        
        userStep[cid] = 0 
      
    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Por favor usa el teclado predefinido")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Vamos, intentalo de nuevo, sólo selecciona una opción")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "👍")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    bot.send_message(m.chat.id, "No entiendo la palabra \"" + m.text + "\"\n Usa el comando /start para reiniciar el bot, el comando /paises si necesitas realizar una consulta sobre algún país ó puedes usar el comando /help si necesitas ayuda.")


bot.infinity_polling()