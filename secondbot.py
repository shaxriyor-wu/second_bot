import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import BOT2TOKEN

bot_token = Bot(token=BOT2TOKEN)

dp = Dispatcher()

@dp.message(CommandStart()) #1
async def Start_handler(message: Message):
    await message.answer(f"Assalomu alaykum hurmatli {(message.from_user.full_name)}, Botimizga hush kelibsiz")

@dp.message(F.text.lower() == "malumot") #2
async def bot_haqida(message: Message):
    await message.answer(f"Bizning 'All about football' botimiz siz yozgan Jamoa malumotlarini berishga qodir")

@dp.message(F.text.capitalize() == "Barcelona") #3
async def Barca(message: Message):
    await message.reply(f"Barcelona jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1899-yil 29-noyabr\n"
                         f"Shior: 'Mes que un club' (Klubdanda muhimroq)\n"
                         f"Stadion: 'Cam Nou'\n "
                         f"Hozirgi Murabbiyi: Flick\n"
                         f"Hozirgi Prezidenti: J.Laporta\n"
                         f"Yutuqlari: 5x UCL,  28x  Laliga, 32x CopaDelRey\n")

@dp.message(F.text.capitalize() == "Real madrid") #4
async def Real(message: Message):
    await message.reply(f"Real Madrid jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1902-yil 6-mart\n"
                         f"Shior: 'Hala Madrid'\n"
                         f"Stadion: 'Santiago Bernabeu'\n"
                         f"Yutuqlari: 15x UCL, 36x LaLiga, 20x CopaDelRey\n")

@dp.message(F.text.capitalize() == "Yuventus" or "Juventus") #5
async def Juve(message: Message):
    await message.reply(f"Juventus jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1897-yil\n"
                         f"Shior: 'The Old Lady' \n"
                         f"Stadion: 'Allianz stadium'\n"
                         f"Yutuqlari: 2x UCL, 36x Seria A, 15x Coppa Italia, 9x SupperCopa Italiana\n")

@dp.message(F.text.capitalize() == "Milan") #6
async def Milan(message: Message):
    await message.reply(f"Milan jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1899-yil 16-dekabr\n"
                         f"Shior: 'We will be a team of devils' \n"
                         f"Stadion: 'San Siro'\n"
                         f"Yutuqlari: 6x UCL, 19x Seria A, 14x Coppa Italia, 5x SupperCopa Italiana\n")

@dp.message(F.text.upper() == "PSG" or "Paris Saint-Germain") #7
async def psg(message: Message):
    await message.reply(f"PSG jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1970-yil 12-avgust\n"
                         f"Shior: 'Paris est magique' \n"
                         f"Stadion: 'Parc de Princes'\n"
                         f"Yutuqlari: 1x UCL, 13x Leauge 1, 16x Coupe de Frence, 13x Trophe des Chempions\n")

@dp.message(F.text.capitalize() == "Bavariya") #8
async def Bavariya(message: Message):
    await message.reply(f" Bavariya jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1900-yil 27-fevral\n"
                         f"Shior: 'Mia San Mia' \n"
                         f"Stadion: 'Allianz Arena'\n"
                         f"Yutuqlari: 6x UCL, 34x Bundesliga, 20x DFB-Pokal, 19x DFL superCup\n")

@dp.message(F.text.capitalize() == "Manchester united" or "Manchester yunaytet") #9
async def Mnu(message: Message):
    await message.reply(f" Man united jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1878-yil\n"
                         f"Shior: 'Concilio et Labore' \n"
                         f"Stadion: 'Old Traffort'\n"
                         f"Yutuqlari: 3x UCL, 20x APL, 12x Fa Cup, 9x Community Shield\n")

@dp.message(F.text.title() == "Manchester city") #10
async def mci(message: Message):
    await message.reply(f" Man City jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1880-yil\n"
                         f"Shior: rasman mavjud emas \n"
                         f"Stadion: 'Etihad Stadium'\n"
                         f"Yutuqlari: 0x UCL, 8x APL,7x Fa-Cup, 9x Community shield\n")

@dp.message(F.text.title() == "Arsenal") #11
async def ars(message: Message):
    await message.reply(f" Arsenal jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1886-yil\n"
                         f"Shior: 'Victoria Concordia Crescit' \n"
                         f"Stadion: 'Emirates Stadium'\n"
                         f"Yutuqlari: 0x UCL, 7x APL,14x Fa-Cup, 8x Community shield\n")

@dp.message(F.text.title() == "Chelsea") #12
async def chel(message: Message):
    await message.reply(f" Chelsea jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1905-yil\n"
                         f"Shior: 'Nisi Dominus Frustra' \n"
                         f"Stadion: 'Stamford Bridge'\n"
                         f"Yutuqlari: 2x UCL, 9x APL,10x Fa-Cup, 5x Community shield\n")

@dp.message(F.text.title() == "Tottenham hotspur" or "Tottenham" or "Totenham" or "Totenhem") #13
async def tot(message: Message):
    await message.reply(f" Tottenham jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1882-yil\n"
                         f"Shior: 'Audera est Facera' \n"
                         f"Stadion: 'Totenham Hotspur Stadium'\n"
                         f"Yutuqlari: 0x UCL, 1x APL,4x Fa-Cup, 3x Community shield\n")

@dp.message( F.text.title() == "Liverpool") #14
async def liv(message: Message):
    await message.reply(f"Liverool jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1892-yil\n"
                         f"Shior: 'You will never walk alone' \n"
                         f"Stadion: 'Anfield Stadium'\n"
                         f"Yutuqlari: 6x UCL, 13x APL,11x Fa-Cup, 9x Community shield\n")

@dp.message(F.text.title() == "Inter") #15
async def inter(message: Message):
    await message.reply(f"Inter Milan jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1908-yil\n"
                         f"Ikkinchi nomi: Nerazzurri (Qora-ko‘klar), Il Biscione\n"
                         f"Stadion: San Siro (Giuseppe Meazza)\n"
                         f"Yutuqlari: 3× UCL, 19× Serie A, 7× Coppa Italia, 5× Supercoppa Italiana\n")

@dp.message(F.text.title() == "As Roma" or "As Roma") #16
async def roma(message: Message):
    await message.reply(f"AS Roma jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1927-yil\n"
                         f"Ikkinchi nom: I Lupi va La Magica\n"
                         f"Stadion: Stadio Olimpico\n"
                         f"Yutuqlari: 0× UCL, 3× Serie A, 9× Coppa Italia, 2× Supercoppa Italiana\n")

@dp.message(F.text.title() == "Lazio" or "Latsio" or "Latsiyo") #17
async def lazio(message: Message):
    await message.reply(f"SS Lazio jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1900-yil\n"
                         f"ikkinchi nom: I Biancocelesti (Oq-osmonranglar)\n"
                         f"Stadion: Stadio Olimpico\n"
                         f"Yutuqlari: 0× UCL, 2× Serie A, 7× Coppa Italia, 5× Supercoppa Italiana\n")

@dp.message(F.text.title() == "Napoli") #18
async def napoli(message: Message):
    await message.reply(f"Napoli jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1926-yil\n"
                         f"Shiori: mavjud emas\n"
                         f"Stadion: 'Stadio Diego Armando Maradona' \n"
                         f"Yutuqlari: 0× UCL, 3× Serie A, 3× Coppa Italia, 1× Supercoppa Italiana\n")

@dp.message(F.text.title() == "Torino" or "Tarino") #19
async def torino(message: Message):
    await message.reply(f"Torino jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1906-yil\n"
                         f"SHiori: Il Toro , Grande Torino\n"
                         f"Stadion: aniq topilmadi\n"
                         f"Yutuqlari: 0× UCL, 7× Serie A, (aniq Coppa Italia soni yo‘q), 0× Supercoppa Italiana\n")

@dp.message(F.text.title() == "Fiorentina") #20
async def fiorentina(message: Message):
    await message.reply(f"Fiorentina jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1926-yil\n"
                         f"Shiori: La Viola \n"
                         f"Stadion: Malumot yoq\n"
                         f"Yutuqlari: 0× UCL, 2× Serie A, (aniq Coppa/ Superkoppa soni yo‘q)\n")

@dp.message(F.text.title() == "Bologna" or "Balonya") #21
async def bologna(message: Message):
    await message.reply(f"Bologna jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1909-yil\n"
                         f"Nomi: Mavjud emas\n"
                         f"Stadion: Malumot yoq\n"
                         f"Yutuqlari: 0× UCL, 7× Serie A, (aniq milliy kubok/superkubok yo‘q)\n")

@dp.message(F.text.title() == "Genoa" or "Jenoa") #22
async def genoa(message: Message):
    await message.reply(f"Genoa jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1893-yil\n"
                         f"Shior: 'I Rossoblù (Qizil-ko‘klar)'\n"
                         f"Stadion: Stadio Luigi Ferraris\n"
                         f"Yutuqlari: 0× UCL, 9× Serie A (eng qadimgi chempionlar), 1× Coppa Italia, 0× Supercoppa Italiana\n")
@dp.message(F.text.title() == "Paxtakor") #23
async def pakhtakor(message: Message):
    await message.reply(f"Paxtakor jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1956-yil\n"
                         f"Shiori: - \n"
                         f"Stadion: Paxtakor Markaziy Stadion\n"
                         f"Yutuqlari: 16× Oliy Liga chempionligi, 11× O‘zbekiston Kubogi, (Superkubok ma’lum emas aniq raqam), AFC Champions League – yarim final (2003, 2004)\n")

@dp.message(F.text.title() == "Bunyodkor") #24
async def bunyodkor(message: Message):
    await message.reply(f"Bunyodkor jamoasi haqida:\n"
                         f"Tashkil topgan yili: 2005-yil\n"
                         f"Shior: -\n"
                         f"Stadion: Milliy Stadion \n"
                         f"Yutuqlari: 3x Oliy Liga chempionligi , 4x O‘zbekiston Kubogi , AFC Champions League ishtiroki (2008 semifinal)\n")

@dp.message(F.text.title() == "Lokomotiv") #25
async def lokomotiv(message: Message):
    await message.reply(f"Lokomotiv Tashkent jamoasi haqida:\n"
                         f"Tashkil topgan yili: 2002-yil\n"
                         f"SHior: - \n"
                         f"Stadion: Malumot yoq\n"
                         f"Yutuqlari: 5x Oliy Liga, 3x O'zbekiston Kubogi AFC Champions League ishtiroki — 2013ga chiqqan\n")

@dp.message(F.text.title() == "Xorazm") #26
async def xorazm(message: Message):
    await message.reply(f"Xorazm FK Urganch jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1972-yil\n"
                         f"Shior: - \n"
                         f"Stadion: Xorazm Stadion \n"
                         f"Yutuqlari: O‘zbekiston Kubogi ishtiroki, lekin jiddiy sovrinlar mavjud emas (yaqin yutuqlari–32 final bosqichlari)\n")
@dp.message(F.text.title() == "Navbahor")
async def navbahor(message: Message): #27
    await message.reply(f"Navbahor Namangan jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1978-yil\n"
                         f"Shiori: -\n"
                         f"Stadion: Markaziy Stadium\n"
                         f"Yutuqlari: 1× Superliga (1996), 3× O‘zbekiston Kubogi (1992, 1995, 1998), 1× Superkubok (1999)\n")

@dp.message(F.text.title() == "Nasaf") #28
async def nasaf(message: Message):
    await message.reply(f"Nasaf Qarshi jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1986-yil\n"
                         f"Shiori: -\n"
                         f"Stadion: Markaziy Stadium\n"
                         f"Yutuqlari: (aniq raqamlar yoʻq — ammo Superliga va Kubok sovrinlari mavjud)\n")

@dp.message(F.text.title() == "Andijon") #29
async def andijon(message: Message):
    await message.reply(f"Andijon jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1964-yil\n"
                         f"Shiori: -\n"
                         f"Stadion: malumot topilmadi\n"
                         f"Yutuqlari: (asosiy sovrinlari mavjud emas yoki kam)\n")

@dp.message(F.text.title() == "Neftchi") #30
async def neftchi(message: Message):
    await message.reply(f"Neftchi Fargʻona jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1962\n"
                         f"Shiori: -\n"
                         f"Stadion: Istiqlol Stadium \n"
                         f"Yutuqlari: 5× Superliga (1992–1995, 2001), 2× O‘zbekiston Kubogi (1994, 1996)\n")

@dp.message(F.text.title() == "Aston Villa") #31
async def astonvilla(message: Message):
    await message.reply(f"Aston Villa jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1874-yil\n"
                         f"Shiori: -\n"
                         f"Yutuqlari: UEFA Champions League, Premier League (First Division), FA Cup, Community Shield\n")

@dp.message(F.text.title() == "Everton") #32
async def everton(message: Message):
    await message.reply(f"Everton jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1878-yil\n"
                         f"Shiori: -\n"
                         f"Yutuqlari: UEFA Champions League, Premier League (First Division), FA Cup, Community Shield\n")

@dp.message(F.text.title() == "West Ham United") #33
async def westham(message: Message):
    await message.reply(f"West Ham United jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1895-yil\n"
                         f"Shiori: -\n"
                         f"Yutuqlari: UEFA Champions League, Premier League (First Division), FA Cup, Community Shield\n")

@dp.message(F.text.title() == "Leeds United") #34
async def leeds(message: Message):
    await message.reply(f"Leeds United jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1919-yil\n"
                         f"Shiori: -\n"
                         f"Yutuqlari: UEFA Champions League, Premier League (First Division), FA Cup, Community Shield\n")

@dp.message(F.text.title() == "Newcastle United") #35
async def newcastle(message: Message):
    await message.reply(f"Newcastle United jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1892-yil\n"
                         f"Shiori: -\n"
                         f"Yutuqlari: UEFA Champions League, Premier League (First Division), FA Cup, Community Shield\n")

@dp.message(F.text.title() == "Leicester City") #36
async def leicester(message: Message):
    await message.reply(f"Leicester City jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1884-yil\n"
                         f"Shiori: -\n"
                         f"Yutuqlari: UEFA Champions League, Premier League (First Division), FA Cup, Community Shield\n")

@dp.message(F.text.title() == "Aston Villa") #37
async def astonvilla(message: Message):
    await message.reply(f"Aston Villa jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1874-yil\n"
                         f"Shiori: Prepared\n"
                         f"Yutuqlari: 1× UEFA Champions League, 7× First Division, 7× FA Cup, 1× Community Shield\n")

@dp.message(F.text.title() == "Everton") #38
async def everton(message: Message):
    await message.reply(f"Everton jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1878-yil\n"
                         f"Shiori: Nil Satis Nisi Optimum\n"
                         f"Yutuqlari: 0× UEFA Champions League, 9× First Division, 5× FA Cup, 9× Community Shield\n")

@dp.message(F.text.title() == "West Ham United") #39
async def westham(message: Message):
    await message.reply(f"West Ham United jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1895-yil\n"
                         f"Shiori: -\n"
                         f"Yutuqlari: 0× UEFA Champions League, 0× First Division, 3× FA Cup, 0× Community Shield\n")

@dp.message(F.text.title() == "Leeds United") #40
async def leeds(message: Message):
    await message.reply(f"Leeds United jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1919-yil\n"
                         f"Shiori: Marching on Together\n"
                         f"Yutuqlari: 0× UEFA Champions League, 3× First Division, 1× FA Cup, 0× Community Shield\n")

@dp.message(F.text.title() == "Newcastle United") #41
async def newcastle(message: Message):
    await message.reply(f"Newcastle United jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1892-yil\n"
                         f"Shiori: -\n"
                         f"Yutuqlari: 0× UEFA Champions League, 4× First Division, 6× FA Cup, 0× Community Shield\n")

@dp.message(F.text.title() == "Leicester City") #42
async def leicester(message: Message):
    await message.reply(f"Leicester City jamoasi haqida:\n"
                         f"Tashkil topgan yili: 1884-yil\n"
                         f"Shiori: Foxes Never Quit / #Fearless\n"
                         f"Yutuqlari: 0× UEFA Champions League, 1× First Division, 1× FA Cup, 0× Community Shield\n")






async def main() -> None:
    await dp.start_polling(bot_token)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())