import discord

from discord.ext import commands
from pystyle import Colors, Colorate

# CONFIG EDIT EVERYTHING YOU NEED TO HERE! :)
# -------------------------------------------

# selfbot settings
prefix = "."
token = "ACOUNT TOKEN HERE..."

# cryptos 
btc = "address"
ltc = "address"
eth = "address"

# real cash money moolahs
paypal = "https://paypal.me/"
cashapp = "$"

# as this is just a base you can add more payments if you would like :)
# -------------------------------------------

client = commands.Bot(self_bot=True, command_prefix=prefix)

@client.event
async def on_connect():
  logo = """
  __  __         ____                                  _       
 |  \/  |_   _  |  _ \ __ _ _   _ _ __ ___   ___ _ __ | |_ ___ 
 | |\/| | | | | | |_) / _` | | | | '_ ` _ \ / _ \ '_ \| __/ __|
 | |  | | |_| | |  __/ (_| | |_| | | | | | |  __/ | | | |_\__ |
 |_|  |_|\__, | |_|   \__,_|\__, |_| |_| |_|\___|_| |_|\__|___/
         |___/              |___/                              
---------------------------------------------------------------
"""
  print(Colorate.Horizontal(Colors.red_to_white, logo, 1))
  print(" ")
  print(Colorate.Horizontal(Colors.red_to_white, f"Logged Into -> {client.user}\nPrefix -> {prefix}\nToken -> REDACTED", 1))

# MAIN PAYMENT COMMAND :)
# -------------------------------------------

@client.command()
async def mypayments(ctx, payment = None):
  await ctx.message.delete()
  if payment == None:
    await ctx.send(f"# Payment Methods\n \n## Cryptos\n> **BTC ->** `{btc}`\n> **LTC ->** `{ltc}`\n> **ETH ->** `{eth}`\n \n## Direct Pyament\n> **Paypal ->** `{paypal}`\n> **Cashapp ->** `{cashapp}`")
  if payment == "btc":
    await ctx.send(f"## Bitcoin Address\n> `{btc}`")
  if payment == "ltc":
    await ctx.send(f"## Litecoin Address\n> `{ltc}`")
  if payment == "eth":
    await ctx.send(f"## Ethereum Address\n> `{eth}`")
  if payment == "paypal":
    await ctx.send(f"## Paypal Information\n> {paypal}")
  if payment == "cashapp":
    await ctx.send(f"## Cashapp Cashtag\n> `{cashapp}`")

# -------------------------------------------

client.run(token, log_handler=None)