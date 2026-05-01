import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

# MENSAJE DE AYUDA
@bot.command()
async def ayuda(ctx):
    mensaje = """
🌱 **EcoBot - Comandos**

!tip → Consejo ecológico
!reto → Reto ecológico diario
!reciclar [objeto] → Clasificar residuos
!degradacion [objeto] → Tiempo de degradación
!quiz → Mini juego ecológico
!tecno → Consejo sobre uso de tecnología
"""
    await ctx.send(mensaje)

# CONSEJOS
tips = [
    "Usa bolsas reutilizables 🛍️",
    "Apaga las luces cuando no las uses 💡",
    "Evita botellas de plástico 🚫",
    "Reduce el uso del celular antes de dormir 📵",
    "Recicla papel y cartón ♻️"
]

@bot.command()
async def tip(ctx):
    await ctx.send(random.choice(tips))

# RETOS
retos = [
    "Hoy no uses plástico 🚫",
    "Camina en vez de usar transporte 🚶",
    "Desconéctate 1 hora del celular 📵",
    "Reutiliza algo en casa ♻️"
]

@bot.command()
async def reto(ctx):
    await ctx.send(random.choice(retos))

# RECICLAJE
@bot.command()
async def reciclar(ctx, objeto):
    objeto = objeto.lower()

    reciclables = {
        "botella": "Plástico ♻️",
        "papel": "Papel ♻️",
        "lata": "Metal ♻️",
        "vidrio": "Vidrio ♻️"
    }

    if objeto in reciclables:
        await ctx.send(f"{objeto} → {reciclables[objeto]}")
    else:
        await ctx.send("No estoy seguro 😕 Intenta con botella, papel, lata o vidrio")

# DEGRADACIÓN
@bot.command()
async def degradacion(ctx, objeto):
    objeto = objeto.lower()

    datos = {
        "plastico": "500 años 😱",
        "papel": "2 a 5 meses",
        "vidrio": "Más de 4000 años 😳",
        "lata": "10 años"
    }

    if objeto in datos:
        await ctx.send(f"{objeto} tarda {datos[objeto]}")
    else:
        await ctx.send("No tengo datos de eso")

# MINI QUIZ
@bot.command()
async def quiz(ctx):
    pregunta = "¿Qué material tarda más en degradarse?"
    opciones = "A) Papel\nB) Plástico\nC) Vidrio"
    await ctx.send(pregunta + "\n" + opciones)

# TECNOLOGÍA
@bot.command()
async def tecno(ctx):
    consejos = [
        "No uses el celular antes de dormir",
        "Toma descansos cada 30 minutos",
        "Sal a caminar sin el teléfono",
        "Reduce redes sociales"
    ]
    await ctx.send(random.choice(consejos))

bot.run("")