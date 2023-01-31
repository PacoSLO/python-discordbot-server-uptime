from discord.ext import commands
import discord, datetime, time, os, ctypes

# Just add your desired prefix there.
bot = commands.Bot(command_prefix='!')

#Bot status
@bot.event
async def on_ready():  # This function is run upon the bots startup completing
    # os.system('cls')
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Status: Running")
    print("########################################")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"UP: {days}d {hour:02}h {mins:02}m"))
    
#Sending channels msg
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if message.content.startswith('!uptime'):
        await message.channel.send(f"{days} days, {hour:02}h:{mins:02}m{sec:02}s") 
    
    if message.content.startswith('!youtube'):
        await message.channel.send("YOUR COMMAND HERE") 
        
    if message.content.startswith('!twitch'):
        await message.channel.send("YOUR COMMAND HERE")

    if message.content.startswith('!invite'):
        await message.channel.send("YOUR COMMAND HERE") 
    
    if message.content.startswith('!ping'):
        await message.channel.send(f"Ping: {round(bot.latency * 1000)}ms")

    if message.content.startswith('!commands'):
        await message.channel.send("!youtube, !twitch, !invite, !uptime, !ping")        

# getting the library in which GetTickCount64() resides
lib = ctypes.windll.kernel32
 
# calling the function and storing the return value
t = lib.GetTickCount64()
 
# since the time is in milliseconds i.e. 1000 * seconds
# therefore truncating the value
t = int(str(t)[:-3])
 
# extracting hours, minutes, seconds & days from t
# variable (which stores total time in seconds)
mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)
 
# formatting the time in readable form
# (format = x days, HH:MM:SS)
print(f"{days} days, {hour:02}h:{mins:02}m:{sec:02}s")
    
#BOT TOKEN
bot.run('YOUR TOKEN HERE')

