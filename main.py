import discord
from discord.ext import commands
from para import para_kontrol
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Selam! Ben {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def save_img(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            file_name = attachments.filename
            await attachments.save(f"./images/{file_name}")
            await ctx.send(f"Fotoğraf başarıyla eklendi {file_name}")
    else:
        await ctx.send("Fotoğraf eklemelisiniz")

  

@bot.command()
async def YIKIL_KARŞIMDAN(ctx):
    await ctx.send("Emredersiniz efendim 🙇")
    await ctx.send("Hemen kayboluyorum 🙇")
    await ctx.send("Canımı bağışladığınız için teşekkür ederim 🙏🙇")
    await bot.close()  

@bot.command()
async def para(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            file_name = attachments.filename
            await attachments.save(f"./images/{file_name}")
            await ctx.send(para_kontrol(resim=f"./images/{file_name}"))
    else:
        await ctx.send("Bir fotoğraf eklemelisiniz")






bot.run("TOKEN")

