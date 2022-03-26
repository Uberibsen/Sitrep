import discord, json, os
from dotenv import load_dotenv
from discord.ext import commands
from src.request import API
from src.compare import Hexagon

load_dotenv()

token = os.getenv('BOT_TOKEN')
bot = commands.Bot(command_prefix = os.getenv('PREFIX'), help_command=None, case_sensitive = True)

@bot.event
async def on_ready():
    print(f'{bot.user} reporting for duty!')

@bot.command(name = "test")
async def test(ctx):
    await ctx.send(f'{bot.user} is online!')

@bot.command(name = "report")
async def report(ctx):
    await ctx.send("Command received! Gathering intel...")
    with open("constants\shards.json", "r") as api_url:
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
    embed.set_footer(text="End of report")
    await ctx.send(embed=embed)

@bot.command(name = "hex")
async def hex(ctx, hex_name):   
    with open("constants\shards.json", "r") as api_url:
        data = json.load(api_url)
        api = data['shards'][0]['url']  
        hex_name = Hexagon.search_hex_name(hex_name)
        if hex_name:
            full_hex_name = Hexagon.split_hex_name(hex_name)
            await ctx.send(f'Hex identified: {full_hex_name}.\nGathering intel...')
            enlistments, warden_casualties, colonial_casualties = API.get_hex_info(api, hex_name)
        else:
            raise commands.BadArgument()
    # Embed formatting
    embed=discord.Embed(title=f"{full_hex_name} status report", description="Amount of casualties, enlistments and war duration")
    embed.add_field(name="Enlistments", value=str("{:,}".format(enlistments)), inline=False)
    embed.add_field(name="Colonials", value=str("{:,}".format(colonial_casualties)), inline=True)
    embed.add_field(name="Wardens", value=str("{:,}".format(warden_casualties)), inline=True)
    embed.set_footer(text="End of report")
    await ctx.send(embed=embed)

# Error handling
@bot.event
async def on_command_error(ctx, error):
    """Error handler"""

    if isinstance(error, commands.CommandNotFound):
        message = "This command does not exist."
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    elif isinstance(error, commands.MissingPermissions):
        message = "You are missing the required permissions to run this command!"
    elif isinstance(error, commands.BadArgument):
        message = "Hex not identified. Try a different input or check your spelling."
    elif isinstance(error, commands.UserInputError):
        message = "Something about your input was wrong, please check your input and try again!"
    else:
        message = "Oh no! Something went wrong while running the command!"
    await ctx.send(message, delete_after = 5)

bot.run(token)