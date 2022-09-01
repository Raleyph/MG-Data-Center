from aiogram.types import KeyboardButton, InlineKeyboardButton

token = ''

codes = {
	"Admin": 'b8g867rpauu2hc45g42b',
	"Moder": '5d2tr2xbpofi2vo5sk9y',
	"User": 'yujfvhz7scktiz884wu6'
}

start_message = f'Вас приветствует Telegram клиент основоной серверной панели дата-центра MG'

# кнопки основной клавиатуры
m_download = KeyboardButton("Получить данные")
m_upload = KeyboardButton("Загрузить данные")
m_delete = KeyboardButton("Удалить данные")
m_settings = KeyboardButton("Прочее")
m_faq = KeyboardButton("FAQ")


# кнопки подтверждения
cf_yes = InlineKeyboardButton('Да', callback_data='yes')
cf_no = InlineKeyboardButton('Нет', callback_data='no')


# категории файлов
c_photo = InlineKeyboardButton('Изображение', callback_data='c_img')
c_video = InlineKeyboardButton('Видео', callback_data='c_vid')
c_text = InlineKeyboardButton('Текстовый документ', callback_data='c_txt')
c_rar = InlineKeyboardButton('Архив', callback_data='c_rar')
c_exe = InlineKeyboardButton('Установщик', callback_data='c_exe')
c_etc = InlineKeyboardButton('Прочее', callback_data='c_etc')
