import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

# COLOQUE OS IDS AQUI DEPOIS
CANAL_APROVACAO = 123456789012345678
CARGO_APROVADO = 123456789012345678

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

class RegistroModal(discord.ui.Modal, title="Registro"):
    nome = discord.ui.TextInput(label="Nome no jogo")
    id_jogo = discord.ui.TextInput(label="ID no jogo")
    recrutador = discord.ui.TextInput(label="Quem recrutou")
    cargo = discord.ui.TextInput(label="Cargo desejado")

    async def on_submit(self, interaction):
        canal = bot.get_channel(CANAL_APROVACAO)

        embed = discord.Embed(
            title="📋 Novo Registro",
            color=discord.Color.blue()
        )

        embed.add_field(name="Nome", value=self.nome.value, inline=False)
        embed.add_field(name="ID", value=self.id_jogo.value, inline=False)
        embed.add_field(name="Recrutador", value=self.recrutador.value, inline=False)
        embed.add_field(name="Cargo", value=self.cargo.value, inline=False)

        await canal.send(embed=embed)
        await interaction.response.send_message(
            "✅ Registro enviado para análise dos administradores.",
            ephemeral=True
        )

@bot.tree.command(name="registro", description="Abrir formulário de registro")
async def registro(interaction):
    await interaction.response.send_modal(RegistroModal())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot conectado: {bot.user}")

bot.run(TOKEN)
