import discord
from discord import colour
from discord import embeds
from discord import user
from discord.embeds import Embed
from discord.ext import commands
from datetime import*
import random
import asyncio
import time
from discord.ext import tasks
import os
import threading
client = commands.Bot(command_prefix = '-')

d = datetime.now()

@client.event
async def on_ready():
    print("봇 켜짐")
    print(client.user)
    print("======")
    game = discord.Game("뚜아~")
    await client.change_presence(status=discord.Status.online, activity=game) 
    
cl1_s = "00:00"
cl2_s = "00:00"
cl3_s = "00:00"
cl4_s = "00:00"
cl5_s = "00:00"
cl6_s = "00:00"
cl7_s = "00:00"
cl1_e = "00:00"
cl2_e = "00:00"
cl3_e = "00:00"
cl4_e = "00:00"
cl5_e = "00:00"
cl6_e = "00:00"
cl7_e = "00:00"


cl2_ss =  cl2_s[:2] 
cl3_ss =  cl3_s[:2] 
cl4_ss =  cl4_s[:2] 
cl5_ss =  cl5_s[:2] 
cl6_ss =  cl6_s[:2] 
cl7_ss =  cl7_s[:2] 
cl1_es =  cl1_e[:2] 
cl2_es =  cl2_e[:2] 
cl3_es =  cl3_e[:2] 
cl4_es =  cl4_e[:2] 
cl5_es =  cl5_e[:2] 
cl6_es =  cl6_e[:2] 
cl7_es =  cl7_e[:2]
 
cl2_sss =  cl2_s[-2:] 
cl3_sss =  cl3_s[-2:] 
cl4_sss =  cl4_s[-2:] 
cl5_sss =  cl5_s[-2:] 
cl6_sss =  cl6_s[-2:] 
cl7_sss =  cl7_s[-2:] 
cl1_ess =  cl1_e[-2:] 
cl2_ess =  cl2_e[-2:] 
cl3_ess =  cl3_e[-2:] 
cl4_ess =  cl4_e[-2:] 
cl5_ess =  cl5_e[-2:] 
cl6_ess =  cl6_e[-2:] 
cl7_ess =  cl7_e[-2:] 
cl1_ss =  cl1_s[:2]  
cl1_sss =  cl1_s[-2:]
@client.event
async def on_message(message):
    global d, cl1_e, cl1_s, cl2_e,cl2_s,cl3_s,cl4_s,cl5_s,cl6_s,cl7_s,cl3_e,cl4_e,cl5_e,cl6_e,cl7_e
    if message.content == "!도움":
        embed = discord.Embed(color=0x66FF00, title = "또치봇이라고 합니다", description="잘 부탁드려요")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        embed.add_field(name="!시간표", value="등록된 시간표를 알려줍니다", inline=False)
        embed.add_field(name="!설정 <교시> <시작 or 끝> <시간>", value="n교시 시작or끝을 시간으로 설정합니다", inline=False)
        embed.set_footer(text="시간은 예시와 같이 작성해주세요 (예: 12:00, 03:30)")
        await message.channel.send(embed=embed)
    if d_st_h == cl1_s[:2] and d_st_m == cl1_s[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "1교시 시작 알림", description="<@384596494180810762>님 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        embed.add_field(name="월요일", value="문학A", inline=True)
        embed.add_field(name="화요일", value="영어B", inline=True)
        embed.add_field(name="수요일", value="창체", inline=True)
        embed.add_field(name="목요일", value="문학A", inline=True)
        embed.add_field(name="금요일", value="수학1", inline=True)
        await ch.send(embed=embed)
    elif d_st_h == cl2_s[:2] and d_st_m == cl2_s[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "2교시 시작 알림", description="<@384596494180810762>님 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        embed.add_field(name="월요일", value="영어B", inline=True)
        embed.add_field(name="화요일", value="음악", inline=True)
        embed.add_field(name="수요일", value="창체", inline=True)
        embed.add_field(name="목요일", value="독일어", inline=True)
        embed.add_field(name="금요일", value="사문A", inline=True)
        await ch.send(embed=embed)
    elif d_st_h == cl3_s[:2] and d_st_m == cl3_s[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "3교시 시작 알림", description="<@384596494180810762>님 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        embed.add_field(name="월요일", value="사문A", inline=True)
        embed.add_field(name="화요일", value="수학1", inline=True)
        embed.add_field(name="수요일", value="창체", inline=True)
        embed.add_field(name="목요일", value="화학B", inline=True)
        embed.add_field(name="금요일", value="문학A", inline=True)
        await ch.send(embed=embed)
    elif d_st_h == cl4_s[:2] and d_st_m == cl4_s[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "4교시 시작 알림", description="<@384596494180810762>님 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        embed.add_field(name="월요일", value="문학B", inline=True)
        embed.add_field(name="화요일", value="스포츠", inline=True)
        embed.add_field(name="수요일", value="확통", inline=True)
        embed.add_field(name="목요일", value="영어A", inline=True)
        embed.add_field(name="금요일", value="확통", inline=True)
        await ch.send(embed=embed)
    elif d_st_h == cl5_s[:2] and d_st_m == cl5_s[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "5교시 시작 알림", description="<@384596494180810762>님 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        embed.add_field(name="월요일", value="화학B", inline=True)
        embed.add_field(name="화요일", value="물리C", inline=True)
        embed.add_field(name="수요일", value="사문A", inline=True)
        embed.add_field(name="목요일", value="진로", inline=True)
        embed.add_field(name="금요일", value="물리C", inline=True)
        await ch.send(embed=embed)
    elif d_st_h == cl6_s[:2] and d_st_m == cl6_s[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "6교시 시작 알림", description="<@384596494180810762>님 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        embed.add_field(name="월요일", value="물리C", inline=True)
        embed.add_field(name="화요일", value="독일어", inline=True)
        embed.add_field(name="수요일", value="영어B", inline=True)
        embed.add_field(name="목요일", value="음악", inline=True)
        embed.add_field(name="금요일", value="화학B", inline=True)
        await ch.send(embed=embed)
    elif d_st_h == cl7_s[:2] and d_st_m == cl7_s[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "7교시 시작 알림", description="<@384596494180810762>님 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        embed.add_field(name="월요일", value="수학1", inline=True)
        embed.add_field(name="화요일", value="문학A", inline=True)
        embed.add_field(name="수요일", value="끝", inline=True)
        embed.add_field(name="목요일", value="영어B", inline=True)
        embed.add_field(name="금요일", value="미술", inline=True)
        await ch.send(embed=embed)
    elif d_st_h == cl7_e[:2] and d_st_m == cl7_e[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "7교시 끝 알림", description="<@384596494180810762>님 수고하셨습니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        await ch.send(embed=embed)
    elif d_st_h == cl6_e[:2] and d_st_m == cl6_e[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "6교시 끝 알림", description="<@384596494180810762>님 수고하셨습니다. 다음 시간도 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        await ch.send(embed=embed)
    elif d_st_h == cl5_e[:2] and d_st_m == cl5_e[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "5교시 끝 알림", description="<@384596494180810762>님 수고하셨습니다. 다음 시간도 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        await ch.send(embed=embed)
    elif d_st_h == cl4_e[:2] and d_st_m == cl4_e[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "4교시 끝 알림", description="<@384596494180810762>님 수고하셨습니다. 다음 시간도 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        await ch.send(embed=embed)
    elif d_st_h == cl3_e[:2] and d_st_m == cl3_e[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "3교시 끝 알림", description="<@384596494180810762>님 수고하셨습니다. 다음 시간도 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        await ch.send(embed=embed)
    elif d_st_h == cl2_e[:2] and d_st_m == cl2_e[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "2교시 끝 알림", description="<@384596494180810762>님 수고하셨습니다. 다음 시간도 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        await ch.send(embed=embed)
    elif d_st_h == cl1_e[:2] and d_st_m == cl1_e[-2:] and d_st_s =="00":
        ch = client.get_channel(873195884089864242)
        embed = discord.Embed(color=0x66FF00, title = "1교시 끝 알림", description="<@384596494180810762>님 수고하셨습니다. 다음 시간도 늦지마세요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
        await ch.send(embed=embed)
    else:
        pass
    if message.content == "!시간표":
        user = message.author
        id = message.author.id
        if id == 384596494180810762:
            embed = discord.Embed(color=0x66FF00, title = f"{user.display_name}님의 시간표", description="수업 지각 하지마세요")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            embed.add_field(name="1교시 시작 / 1교시 끝", value="{0} / {1}".format(cl1_s, cl1_e), inline=False)
            embed.add_field(name="2교시 시작 / 2교시 끝", value="{0} / {1}".format(cl2_s, cl2_e), inline=False)
            embed.add_field(name="3교시 시작 / 3교시 끝", value="{0} / {1}".format(cl3_s, cl3_e), inline=False)
            embed.add_field(name="4교시 시작 / 4교시 끝", value="{0} / {1}".format(cl4_s, cl4_e), inline=False)
            embed.add_field(name="5교시 시작 / 5교시 끝", value="{0} / {1}".format(cl5_s, cl5_e), inline=False)
            embed.add_field(name="6교시 시작 / 6교시 끝", value="{0} / {1}".format(cl6_s, cl6_e), inline=False)
            embed.add_field(name="7교시 시작 / 7교시 끝", value="{0} / {1}".format(cl7_s, cl7_e), inline=False)           
            embed.set_footer(text="두둥탁#0972에 의해 제작되었습니다")
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("<@384596494180810762>님이 아닙니다")
    if message.content.startswith("!설정"):
        cl = message.content[4:7]
        se = message.content[8:10]
        time = str(message.content[-5:])
        if cl == "1교시" and se == "시작":
            cl1_s = time

            print(cl, se, time, cl1_s[:2], cl1_s[-2:])
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "1교시" and se == "끝 ":
            cl1_e = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "2교시" and se == "시작":
            cl2_s = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "2교시" and se == "끝 ":
            cl2_e = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "3교시" and se == "시작":
            cl3_s = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "3교시" and se == "끝 ":
            cl3_e = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "4교시" and se == "시작":
            cl4_s = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "4교시" and se == "끝 ":
            cl4_e = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "5교시"and  se == "시작":
            cl5_s = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "5교시" and se == "끝 ":
            cl5_e = time 
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "6교시" and se == "시작":
            cl6_s = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "6교시" and se == "끝 ":
            cl6_e = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "7교시"and se == "시작":
            cl7_s = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        elif cl == "7교시" and se == "끝 ":
            cl7_e = time
            embed = discord.Embed(color=0x66FF00, title = "{0} {1}".format(cl, se), description="{0}로 설정 되었습니다".format(time))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(color=0x66FF00, title = "오류", description="명령어 형식에 맞춰 입력해주세요")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/873071257074171904/asd.png")
            embed.add_field(name="예시", value="!설정 1교시 시작 09:00", inline=False)
            await message.channel.send(embed=embed)
d_st_h = 0
d_st_m = 0
d_st_s = 0 
class AsyncTask:
    def __init__(self):
        pass
    #ss 시작시간 sss 시작분 es끝시간 ess끝분
    def TaskA(self):
        global d, d_st_s, d_st_m, d_st_h
        d = datetime.now()
        d_st = d.strftime('%Y-%m-%d %H:%M:%S')
        d_st_h = d_st[-8:-6]
        d_st_m = d_st[-5:-3]
        d_st_s = d_st[-2:]
        print(d_st_h, d_st_m, d_st_s)
        return d_st_h, d_st_m, d_st_s
    
    def TaskB(self):
        threading.Timer(1,self.TaskA).start()
        threading.Timer(1, self.TaskB).start()


def main():
    print('Async Function')
    at = AsyncTask()
    at.TaskA()
    at.TaskB()
    
if __name__ == '__main__':
    main()


      
        
client.run(os.environ['token'])