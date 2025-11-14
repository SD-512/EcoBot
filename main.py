import discord
from psw import gen_pass
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hola! Soy un EcoBot, estoy aqui para ayudarte a cuidar el planeta 🌎​🌱​")

@bot.command()
async def ecotip(ctx):
    tips = [
        "Desconectar/desenchufar nuestros electrodomesticos nos ayuda a ahorrar energia!⚡",
        "Mantener las luces apagadas durante el dia mientras disfrutamos de la luz solas es bueno para el planeta y nuestro cuerpo!☀️​🌈​"
        "Limpiar los rios ayuda a los animalitos!🐳​🐠",
        "Cerrá la canilla ayuda para ahorrar agua.",
        "Separá tus residuos para reciclar ayuda al planeta!",
        "Usá transporte público o bicicleta.",
        "Plantá un árbol o cuidá las plantas.",
        "Comprá productos con menos envase."
    ]
    await ctx.send(random.choice(tips))

@bot.command()
async def info_agua(ctx):
    await ctx.send("El agua dulce representa menos del 3% del total del agua del planeta. Cuidarla reduce sequías, contaminación y protege la vida.")

@bot.command()
async def info_basura(ctx):
    await ctx.send("Reciclar reduce la contaminación, ahorra energía y disminuye la cantidad de residuos en los vertederos.")

@bot.command()
async def co2(ctx):
    await ctx.send("El CO₂ es un gas de efecto invernadero que contribuye al calentamiento global. Reducirlo ayuda a desacelerar el cambio climático.")

@bot.command()
async def plantas(ctx):
    await ctx.send("Las plantas producen oxígeno, filtran el aire, reducen el calor y ayudan a la biodiversidad. ¡Cuidalas!")

@bot.command()
async def reducir(ctx):
    await ctx.send("Para reducir residuos: evitá productos descartables, comprá a granel, reutilizá envases y elegí materiales duraderos.")
token=
bot.run(token)
