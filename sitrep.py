import discord, json, os
from dotenv import load_dotenv
from discord.ext import commands
from src.request import API

load_dotenv()

token = os.getenv('BOT_TOKEN')
bot = commands.Bot(command_prefix = os.getenv('PREFIX'), help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.command(name = "report")
async def report(ctx):
    await ctx.send("Command received! Gathering intel...")
    with open("Sitrep/constants/shards.json", "r") as api_url:
        data = json.load(api_url)
        api = data['shards'][0]['url']
        api_response = API.get_war_report(api)
    war_number = api_response["warNumber"]
    days_at_war, enlistments, warden_casualties, colonial_casualties = API.get_total_casualties(api)

    # Embed formatting
    embed=discord.Embed(title=f"War {war_number} status report", description="Amount of casualties, enlistments and war duration")
    embed.add_field(name="Enlistments", value=str("{:,}".format(enlistments)), inline=False)
    embed.add_field(name="Colonials", value=str("{:,}".format(colonial_casualties)), inline=True)
    embed.add_field(name="Wardens", value=str("{:,}".format(warden_casualties)), inline=True)
    embed.add_field(name="Days at war", value=days_at_war, inline=False)
    embed.set_footer(text="Updated: 13:37") # Last fetch update
    await ctx.send(embed=embed)

bot.run(token)