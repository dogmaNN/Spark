#導入discord模組
import discord, listData, random
# 導入commands指令模組
from discord.ext import commands
from botToken import botToken


#要求機器人權限
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix = "$", intents = intents)


@bot.event
#當機器人完成啟動
async def on_ready():
    print("哈囉!")
    print(f"目前登入身份 -> {bot.user}")


@bot.event
#回訊息
async def on_message(message):
    #排除自己訊息
    if message.author == bot.user:
        return

    if message.content == "$meme":
        await message.channel.send(random.choice(listData.memeList))
    elif message.content != "閉嘴":
        await message.channel.send(message.content)
    elif message.content == "閉嘴":
        await message.channel.send("我不要")


bot.run(botToken) #TOKEN