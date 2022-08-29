from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
from aiogram.utils import executor

import datetime
import os
import re

import config
import keyboards
import auth
import logs
import files

storage = MemoryStorage()
bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=storage)
now = datetime.datetime.now()


# состояния бота
class StateGroup(StatesGroup):
	menu = State()
	reg = State()

	d_category = State()
	d_date = State()
	d_words = State()
	d_current = State()

	u_file = State()
	u_description = State()
	u_backup = State()


# ошибка
async def error(text: str, message: types.Message, log: str):
	await bot.send_message(message.chat.id, text)
	await state.reset_data()
	await StateGroup.menu.set()


# старт
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	# проверка регистрации
	if auth.user_check(message.chat.id):
		await message.reply(config.start_message, reply_markup=keyboards.m_kb)
		await StateGroup.menu.set()
	else:
		await bot.send_message(message.chat.id, 'Введите код для присвоения вам статуса администратора/модератора/пользователя:')
		await StateGroup.reg.set()


# регистрация нового пользователя
@dp.message_handler(state=StateGroup.reg)
async def reg_user(message: types.Message):
	for c in config.codes.values():
			if message.text == str(c):
				for k, i in config.codes.items():
					if message.text == i:
						us_id = message.from_user.id
						us_name = message.from_user.first_name
						username = message.from_user.username

						auth.user_login(user_id=us_id, user_name=us_name, username=username, status=k)

						if k == 'Admin':
							await bot.send_message(message.chat.id, 'Вы назначены администратором серверной панели MG')
						elif k == 'Moder':
							await bot.send_message(message.chat.id, 'Вы назначены модератором серверной панели MG')
						elif k == 'User':
							await bot.send_message(message.chat.id, 'Вы назначены пользователем серверной панели MG')

						await message.reply(config.start_message, reply_markup=keyboards.m_kb)
						await StateGroup.menu.set()


# кнопка загрузки файлов
@dp.message_handler(lambda message: message.text == 'Загрузить данные', state=StateGroup.menu)
async def menu_answers(message: types.Message):
	await bot.send_message(message.chat.id, 'Отправьте файл без сжатия')
	await StateGroup.u_file.set()


# загрузка файлов в директорию бота
@dp.message_handler(content_types=['document', 'video', 'audio', 'media'], state=StateGroup.u_file)
async def upload_file(message: types.Message, state: FSMContext):
	try:
		if message.content_type == 'document':
			file_id = message.document.file_id
			file_name = message.document.file_name
		elif message.content_type == 'video':
			file_id = message.video.file_id
			file_name = message.video.file_name
		elif message.content_type == 'audio':
			file_id = message.audio.file_id
			file_name = message.audio.file_name

		src_path = r"D:/Desktop/MG Server Panel/Server/bot/files/"

		await state.update_data(path=src_path)
		await state.update_data(name=file_name)

		file = await bot.get_file(file_id)
		await bot.download_file(file.file_path, src_path + file_name)

		await bot.send_message(message.chat.id, 'Введите краткое описание файла')
		await StateGroup.u_description.set()
	except:
		error('Вы отправили неподдерживаемый тип файла!', message, None)


# обработчик описания
@dp.message_handler(state=StateGroup.u_description)
async def upload_description(message: types.Message, state: FSMContext):
	if len(message.text) < 10:
		await bot.send_message(message.chat.id, 'Описание файла слишком короткое!')
	else:
		await state.update_data(description=message.text)
		await bot.send_message(message.chat.id, 'Нужно ли создать резервную копию для этого файла?')
		await StateGroup.u_backup.set()


# проверка необходимости в резервной копии
@dp.message_handler(state=StateGroup.u_backup)
async def upload_backup(message: types.Message, state: FSMContext):
	try:
		u_date = now.strftime("%Y-%m-%d %H:%M")
		data = await state.get_data()

		name = data['name']
		src = data['path']
		desc = data['description']
		backup = message.text

		# добавление сведений о файле в бд
		files.upload_file(name, src, u_date, desc, backup)
		await bot.send_message(message.chat.id, 'Файл был успешно загружен на сервер')
		await state.reset_data()
		await StateGroup.menu.set()
	except:
		error('При загрузке файла произошла ошибка!', message, None)


# кнопка получения файлов
@dp.message_handler(lambda message: message.text == 'Получить данные', state=StateGroup.menu)
async def menu_answers(message: types.Message):
	await bot.send_message(message.chat.id, 'Выберете категорию файла', reply_markup=keyboards.cat_kb)
	await StateGroup.d_category.set()


# обработка ввода категории
@dp.callback_query_handler(text=['c_img', 'c_vid', 'c_txt', 'c_rar', 'c_exe', 'c_etc'], state=StateGroup.d_category)
async def category_callback(call: types.CallbackQuery, state: FSMContext):
	if call.data == 'c_img':
		file_type = 'Image'
	if call.data == 'c_vid':
		file_type = 'Video'
	if call.data == 'c_txt':
		file_type = 'Document'
	if call.data == 'c_rar':
		file_type = 'Archive'
	if call.data == 'c_exe':
		file_type = 'Exe'
	if call.data == 'c_etc':
		file_type = 'Other'

	await state.update_data(category=file_type)
	await call.message.answer('Введите месяц и год создания файла в формате (05-2020)')
	await StateGroup.d_date.set()


# ввод даты
@dp.message_handler(state=StateGroup.d_date)
async def upload_backup(message: types.Message, state: FSMContext):
	if re.match(r'^[0-1][1-9]-[2][0][1-2][0-9]$', message.text):
		await state.update_data(date=message.text)
		await bot.send_message(message.chat.id, 'Введите ключевые слова для поиска файла. Если вы не можете их подобрать, то отправьте N в чат.', parse_mode='html')
		await StateGroup.d_words.set()
	else:
		await bot.send_message(message.chat.id, 'Дата введена некорректно!')


# ввод ключевых слов
@dp.message_handler(state=StateGroup.d_words)
async def upload_backup(message: types.Message, state: FSMContext):
	if message.text != 'N':
		pass
	else:
		pass


executor.start_polling(dp)

