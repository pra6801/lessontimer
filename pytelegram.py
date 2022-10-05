import telebot 
from telebot import types 
from requests.models import Response 
import requests
import datetime
 
 
bot = telebot.TeleBot("5700440786:AAEGGEEZbxhqaV3YFfH4yeJ3rFFzn7ChXfQ") 
url:str = 'https://gogoanime.herokuapp.com/recent-release' 
animeTitle:list = [] 
episodeId:list = [] 
episodeNum:list = [] 
episodeUrl:list = [] 
 
  
r:Response = requests.get(url) 
data = r.json() 
for i in data: 
    animeTitle.append(i.get("animeTitle")) 
    episodeNum.append(i.get("episodeNum")) 
    episodeUrl.append(i.get("episodeUrl"))    
    print(i.get("animeTitles")) 
 
 
 
 
 
 
@bot.message_handler(commands=['start'])  
def helping(message):  
    bot.send_message(message.chat.id, f"/Anime - список аниме\n/help - как работает бот")  
 
@bot.message_handler(commands=['help'])  
def helping(message):  
    bot.send_message(message.chat.id, f"После команды /Anime вам выводиться список аниме отправляете цифру и  все приятнго просмотра))")  
 
 
@bot.message_handler(commands=['Anime'])  
def butonanime(message):  
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        butanime = types.KeyboardButton("Anime")  
        markup.add(butanime) 
        bot.send_message(message.chat.id,f"Нажмите на кнопку для показа",reply_markup=markup) 
    except:
        bot.send_message(message.chat.id, ' Такого аниме нету в нашем списке')
        print(str(message.text), '- не найден')

animeTitle_result = ''     
for i in range(len(animeTitle)): 
    animeTitle_result += f"{i+1}){animeTitle[i]} \n" 
 
    
 
@bot.message_handler(content_types=['text'])  
def anime_name(message): 
  try:
    for i in range(len(animeTitle)):  
        if message.text == 'Anime' or message.text == 'anime': 
            bot.send_message(message.chat.id, animeTitle_result) 
            break 
        elif message.text == str(i): 
            print('user - ',i) 
            print('animeTitle - ',i-1, animeTitle[i-1]) 
            print(animeTitle, len(animeTitle)) 
            bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[i-1]},\nКоличество серий - {episodeNum[i-1]},\nСсылка для просмотра - {episodeUrl[i-1]}")
        elif message.text == '20':
          bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[-1]},\nКоличество серий - {episodeNum[-1]},\nСсылка для просмотра - {episodeUrl[-1]}")
          break
  except:
    bot.send_message(message.chat.id, 'Такого аниме нету в нашем списке')
    print(str(message.text), '- не найден')


  
     
   
 
 
 
 
 
 
 
 

 
bot.polling(none_stop=True, interval=0)
#elif message.text == '3':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[2]},Количество серий - {episodeNum[2]},Ссылка для просмотра - {episodeUrl[2]}") 
# elif message.text == '4':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[3]},Количество серий - {episodeNum[3]},Ссылка для просмотра - {episodeUrl[3]}") 
# elif message.text == '5':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[4]},Количество серий - {episodeNum[4]},Ссылка для просмотра - {episodeUrl[4]}") 
# elif message.text == '6':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[5]},Количество серий - {episodeNum[5]},Ссылка для просмотра - {episodeUrl[5]}") 
# elif message.text == '7':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[6]},Количество серий - {episodeNum[6]},Ссылка для просмотра - {episodeUrl[6]}") 
# elif message.text == '8':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[7]},Количество серий - {episodeNum[7]},Ссылка для просмотра - {episodeUrl[7]}") 
# elif message.text == '9':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[8]},Количество серий - {episodeNum[8]},Ссылка для просмотра - {episodeUrl[8]}") 
# elif message.text == '10':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[9]},Количество серий - {episodeNum[9]},Ссылка для просмотра - {episodeUrl[9]}") 
# elif message.text == '11':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[10]},Количество серий - {episodeNum[10]},Ссылка для просмотра - {episodeUrl[10]}") 
# elif message.text == '12':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[11]},Количество серий - {episodeNum[11]},Ссылка для просмотра - {episodeUrl[11]}") 
# elif message.text == '13':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[12]},Количество серий - {episodeNum[12]},Ссылка для просмотра - {episodeUrl[12]}") 
# elif message.text == '14':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[13]},Количество серий - {episodeNum[13]},Ссылка для просмотра - {episodeUrl[13]}") 
# elif message.text == '15':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[14]},Количество серий - {episodeNum[14]},Ссылка для просмотра - {episodeUrl[14]}") 
# elif message.text == '16':
# bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[15]},Количество серий - {episodeNum[15]},Ссылка для просмотра - {episodeUrl[15]}") 
# elif message.text == '17':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[16]},Количество серий - {episodeNum[16]},Ссылка для просмотра - {episodeUrl[16]}") 
# elif message.text == '18':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[17]},Количество серий - {episodeNum[17]},Ссылка для просмотра - {episodeUrl[17]}") 
# elif message.text == '19':   
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[18]},Количество серий - {episodeNum[18]},Ссылка для просмотра - {episodeUrl[18]}") 
# elif message.text == '20': 
#     bot.send_message(message.chat.id,f"Названия аниме - {animeTitle[19]},Количество серий - {episodeNum[19]},Ссылка для просмотра - {episodeUrl[19]}") 
 
# //@bot.message_handler(commands=['resultgame']) 
# //def game_result(message): 
# //        res = mapkl[0] - results[0]-results[1]-results[2] 
# //        bot.send_message(message.chat.id,f' Клеток на карте осталось - {res}') 
# //        if res == 0: 
# //            bot.send_message(message.chat.id,"Вы выйграли поздравляю") 
# //        else: 
# //            bot.send_message(message.chat.id,"Вы проиграли попробуйте еще раз") 
# // 
# // 
# // 
# //     
# // 
# //#Игра кости состоит в том что вы бросаете кубик на поле которое имееет определенное количество клеток и кубик показывает на сколько клеток вы прошли,вы можете кинуть кубик максимум 3 раза 
# // 
# // 
# // 
# //@bot.message_handler(commands=['start']) 
# //def helping(message): 
# //    bot.send_message(message.chat.id, f'/gude - (Начать с этого)Как играть?\n/genmap - Генерация карты\n/game - бросить кубик\n/win - Как выйграть?\n/lose - Как засчитываеться проигрыш\n/resultgame - Вводите после окончания игры') 
# // 
# // 
# //@bot.message_handler(commands=['gude']) 
# //def gude(message): 
# //    bot.send_message(message.chat.id,'Кидать можно только 3 раза') 
# // 
# // 
# //@bot.message_handler(commands=['resultgame']) 
# //def helpingus(message): 
# //    bot.send_message(message.chat.id,'После того как вы кинули кости 3 раза вводите эту команду и она покажет выйграли вы или проиграли') 
# // 
# // 
# //@bot.message_handler(commands=['genmap']) 
# //def gen_map(message): 
# //    a = random.randint(10, 36) 
# //    mapkl.append(a) 
# //    bot.send_message(message.chat.id, f'Карта состоит из - {a} клеток') 
# // 
# // 
# //@bot.message_handler(commands=['win']) 
# //def win(message): 
# //   bot.send_message(message.chat.id, f'Выйгрыш засчитаеться в том случае если сумма сторон ваших кубиков при броске совпадет с клетками карты') 
# // 
# //@bot.message_handler(commands=['lose']) 
# //def gen_maping(message): 
# //    bot.send_message(message.chat.id, f'Проигрыш засчитываеться в том случае если сумма сторон ваших кубиков при броске не совпадает с клетками карты') 
# // 
# // 
# //@bot.message_handler(commands=['game']) 
# //def set_prv(message): 
# //    markup = types.ReplyKeyboardMarkup(row_width=2) 
# //    itembtn1 = types.KeyboardButton('Бросить кости 🎲') 
# //    markup.add(itembtn1) 
# //    bot.send_message(message.chat.id, "Кидаем?", reply_markup=markup) 
# // 
# // 
# // 
# //@bot.message_handler(content_types=['text']) 
# //def blalalal(message): 
# //    if message.text == 'Бросить кости 🎲': 
# //        br1 = (random.randint(1, 6)) 
# //        br2 = (random.randint(1, 6)) 
# //        bot.send_message(message.chat.id,f'первая сторона кубика - {br1}') 
# //        bot.send_message(message.chat.id,f'вторая сторона кубика - {br2}') 
# //        sumbr = br1 + br2 
# //        results.append(sumbr) 
# //        bot.send_message(message.chat.id,f'сумма этого броска состовляет - {sumbr}') 
# //         
# //         
# //         
# //         
# // 
# // 
# // 
# // 
# // 
# // 
# // 
# // 
# // 
# // 
# // 
# // 
# // 
# //@bot.message_handler(commands=['start']) 
# //def starting(message): 
# //    bot.send_message(message.chat.id, f'/genmap - Генерация карты\n/game - бросить кубик')