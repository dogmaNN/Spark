#導入discord模組
import discord, listData, random
# 導入commands指令模組
from discord.ext import commands
from botToken import botToken


#要求機器人權限
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix = "$", intents = intents)

adminMode = False
talkingMode = True

@bot.event
#當機器人完成啟動
async def on_ready():
    print("哈囉!")
    print(f"目前登入身份 -> {bot.user}")


@bot.event
#回訊息
async def on_message(message):
    global talkingMode, adminMode

    #排除自己訊息
    if message.author == bot.user:
        return
    if message.content == "$adminMode" and message.author.id == 839133432008540191:
        await message.channel.send("載入中....")
        embedVar = discord.Embed(title=f"歡迎 {message.author.name}", description="已啟用管理模式")
        await message.channel.send(embed=embedVar)
        adminMode = True

    elif message.content == "$meme":
        await message.channel.send(random.choice(listData.memeList))
        
    #you can opening it with talkingMode, but there's only i can do it lol
    elif message.content == "$talkingMode" and adminMode:
        if talkingMode:
            await message.channel.send(random.choice(listData.wordList))
        talkingMode ^= True
    
    elif message.content != "閉嘴" and talkingMode:
        await message.channel.send(message.content)
    elif message.content == "閉嘴" and talkingMode:
        await message.channel.send("我不要")


bot.run(botToken) #TOKEN