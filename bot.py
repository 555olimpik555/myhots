import discord 
from discord.ext import commands
import os

client = commands.Bot(command_prefix= "o!")


hellowords =['hello', 'hi','дарова', "привет","привіт","ку","дароу"]
    #слова приветствия
answerwords=['информацию у боте',"информацию о боте","что сдесь делать","команды","команды сервера"]
    #слова ответа
badwords=["нахуй","хуй","сука", "сюк","сюка","сук","пидр","пидорас","пидор","уебан","ебать","ебана","ебаный","ебаная"]
    #плохие слова
goodbaywords=["пока","бб","до свидания","bb","poka","досвидос","пока всем","бб алл"]
    #слова ответы

@client.event
async def on_ready():
    print("Бот в сети")
    #пишет в консоль, когда он в сети

@client.event 
async def on_message (message):
    msg= message.content.lower()

    if msg in hellowords:
        await message.channel.send("Привет, чего хотел?")

    if msg in answerwords:
        await message.channel.send("Напиши в чат комманду o!help, и все узнаешь")

    if msg in goodbaywords:
        await message.channel.send("Пока, удачи тебе!")
    
    for i in badwords:
        if i in msg.content:
            await message.channel.send("Давай общаться нормально {ctx.author.mention}!!!")

    

@client.command(pass_content= True)
@commands.has_permissions( administrator= True )
async def clear(ctx, amount= input(int())):
    await ctx.channel.purge(limit= amount)

@client.command(pass_content= True)
async def hug(ctx, arg= discord.Member):
    embed= discord.Embed(
        colour= discord.Colour.magenta(),
        description= "{ctx.author.mention} обнял(а) {arg}"
    )
    await ctx.send(embed=embed)

token = os.environ.get("BOT_TOKEN")
client.run(str(token))