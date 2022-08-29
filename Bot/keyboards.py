from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
import config


con_kb = InlineKeyboardMarkup(row_width=2).add(config.cf_yes, config.cf_no)
m_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(config.m_download, config.m_upload,
													 config.m_delete, config.m_settings,
													 config.m_faq)
cat_kb = InlineKeyboardMarkup(row_width=2).add(config.c_photo, config.c_video, config.c_text,
											   config.c_rar, config.c_exe, config.c_etc)
