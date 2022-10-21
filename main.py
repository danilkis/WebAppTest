from telebot import types
import telebot

bot = telebot.TeleBot('5616139301:AAE-EBLqZVgYypdQhtJ9VfCSRhmahE996SQ')

def webAppKeyboard(): #�������� ���������� � webapp �������
   keyboard = types.ReplyKeyboardMarkup(row_width=1) #������� ����������
   webAppTest = types.WebAppInfo("https://telegram.mihailgok.ru") #������� webappinfo - ������ �������� url
   webAppGame = types.WebAppInfo("https://games.mihailgok.ru") #������� webappinfo - ������ �������� url
   one_butt = types.KeyboardButton(text="�������� ��������", web_app=webAppTest) #������� ������ ���� webapp
   two_butt = types.KeyboardButton(text="����", web_app=webAppGame) #������� ������ ���� webapp
   keyboard.add(one_butt, two_butt) #��������� ������ � ����������

   return keyboard #���������� ����������

def webAppKeyboardInline(): #�������� inline-���������� � webapp �������
   keyboard = types.InlineKeyboardMarkup(row_width=1) #������� ���������� inline
   webApp = types.WebAppInfo("https://telegram.mihailgok.ru") #������� webappinfo - ������ �������� url
   one = types.InlineKeyboardButton(text="��� ����������", web_app=webApp) #������� ������ ���� webapp
   keyboard.add(one) #��������� ������ � ����������

   return keyboard #���������� ����������


@bot.message_handler(commands=['start']) #������������ ������� �����
def start_fun(message):
   bot.send_message( message.chat.id, '������, � ��� ��� �������� ��������� webapps!)\n��������� �������� �������� ����� ����� �� ������.', parse_mode="Markdown", reply_markup=webAppKeyboard()) #���������� ��������� � ������ �����������


@bot.message_handler(content_types="text")
def new_mes(message):
   start_fun(message)


@bot.message_handler(content_types="web_app_data") #�������� ������������ ������ 
def answer(webAppMes):
   print(webAppMes) #��� ���������� � ���������
   print(webAppMes.web_app_data.data) #��������� �� ��� �� �������� � ����
   bot.send_message(webAppMes.chat.id, f"�������� ���������� �� ���-����������: {webAppMes.web_app_data.data}") 
   #���������� ��������� � ����� �� �������� ������ �� ���-���������� 

if __name__ == '__main__':
   bot.infinity_polling()
