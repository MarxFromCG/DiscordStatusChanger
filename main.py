import discord
from discord.ext import commands 
from colorama import Fore, Style

#####///LOOK HERE\\\#####
token = "Your Token Here"
#####///LOOK HERE\\\#####

b = Style.BRIGHT
print(f"""{Fore.LIGHTBLUE_EX}
DDDDDDDDDDDDD           SSSSSSSSSSSSSSS         CCCCCCCCCCCCC
D::::::::::::DDD      SS:::::::::::::::S     CCC::::::::::::C
D:::::::::::::::DD   S:::::SSSSSS::::::S   CC:::::::::::::::C
DDD:::::DDDDD:::::D  S:::::S     SSSSSSS  C:::::CCCCCCCC::::C
  D:::::D    D:::::D S:::::S             C:::::C       CCCCCC
  D:::::D     D:::::DS:::::S            C:::::C              
  D:::::D     D:::::D S::::SSSS         C:::::C              
  D:::::D     D:::::D  SS::::::SSSSS    C:::::C              
  D:::::D     D:::::D    SSS::::::::SS  C:::::C              
  D:::::D     D:::::D       SSSSSS::::S C:::::C              
  D:::::D     D:::::D            S:::::SC:::::C              
  D:::::D    D:::::D             S:::::S C:::::C       CCCCCC
DDD:::::DDDDD:::::D  SSSSSSS     S:::::S  C:::::CCCCCCCC::::C
D:::::::::::::::DD   S::::::SSSSSS:::::S   CC:::::::::::::::C
D::::::::::::DDD     S:::::::::::::::SS      CCC::::::::::::C
DDDDDDDDDDDDD         SSSSSSSSSSSSSSS           CCCCCCCCCCCCC

{Fore.LIGHTBLACK_EX}====================================================================
====================================================================
====================================================================

{b+Fore.BLUE} >> {Fore.WHITE}{Style.BRIGHT}Options

  {b+Fore.RED} >1< {Fore.WHITE}{Style.BRIGHT}Playing
  {b+Fore.RED} >2< {Fore.WHITE}{Style.BRIGHT}Watching
  {b+Fore.RED} >3< {Fore.WHITE}{Style.BRIGHT}Listening
  {b+Fore.RED} >4< {Fore.WHITE}{Style.BRIGHT}Streaming
""")

class DSCclient(discord.Client):
  async def on_connect(self):
    option = input(f"{Fore.BLUE}Type the number coordinating to your chosen status type {Fore.WHITE}>>: ")
    msgcontent = input(f"{Fore.BLUE}Now type the message you want to be used in the status {Fore.WHITE}>>: ")
    if option == "1":
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=msgcontent))
      print(f"{Fore.GREEN}[+] Changed status to playing.{Fore.RESET}")
    if option == "2":
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=msgcontent))
      print(f"{Fore.GREEN}[+] Changed status to watching.{Fore.RESET}")
    if option == "3":
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=msgcontent))
      print(f"{Fore.GREEN}[+] Changed status to listening.{Fore.RESET}")  
    if option == "4":
      streamurl = input(f"{Fore.BLUE}Copy paste the youtube/twitch link you want to be used {Fore.WHITE}>>: ")
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=msgcontent, url=streamurl))
      print(f"{Fore.GREEN}[+] Changed status to streaming.{Fore.RESET}")  


client = DSCclient()
client.run(token, bot = False)
