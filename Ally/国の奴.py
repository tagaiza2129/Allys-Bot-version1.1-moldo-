import os
import discord
import logging
from datetime import datetime
import json
from discord.ext import commands
logger=logging.getLogger("Ally_bot")
time=datetime.now()
now=time.strftime("%Y-%m-%d %H:%M:%S")
logging.basicConfig(format=f"[{now}] - [%(levelname)s] - %(name)s: %(message)s",level=logging.INFO)
Permission_error=discord.Embed(title="エラー",description="貴方はそのコマンドを実行する権限を持っていないようです...")
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("config2.json",mode="r",encoding="utf-8") as f:
    jsn=json.load(f)
    token=jsn["token"]
    MY_server=jsn["Discord_server"]
    Admin_role=jsn["Admin_role"]
#サーバーIDとBotトークンの指定
MY_GUILD = discord.Object(MY_server) 
class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intents = discord.Intents.all()
bot = MyBot(command_prefix="!", intents=intents)
@bot.hybrid_command(name="同盟チェッカー",description="国が同盟関係かどうかを確認します")
async def Serch(ctx,国名):
    os.chdir(os.path.dirname(__file__))
    with open("list.txt", mode="r") as f:
        data_list = f.read().split()
    if 国名 in data_list:
        embedding=discord.Embed(title="Good",description="同盟関係です。",color=discord.Colour.green())
        embedding.set_footer(text=f"実行者:{ctx.author}",icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=embedding)
    else:
        embedding=discord.Embed(title="Error",description="同盟関係ではありません殺せ!!!。",color=discord.Colour.red())
        embedding.set_footer(text=f"実行者:{ctx.author}",icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=embedding)
@bot.hybrid_command(name="同盟追加",description="リストに同盟国を追加します")
async def save(ctx,国名):
    user=ctx.author
    role=ctx.guild.get_role(int(Admin_role))
    if ctx.author.id==511206584869847042:
        os.chdir(os.path.dirname(__file__))
        with open("list.txt", mode="a") as f:
            f.write(f"\n{国名}")
        embedding=discord.Embed(title="セーブ完了",description=f"{国名}をリストに追加しました",color=discord.Colour.green())
        embedding.set_footer(text=f"実行者:{ctx.author}",icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=embedding)
    else:
        Permission_error.set_footer(text=f"実行者:{ctx.author}",icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=Permission_error)
@bot.hybrid_command(name="同盟削除",description="リストから同盟国を削除します")
async def delete(ctx,国名):
    user=ctx.author
    role=ctx.guild.get_role(int(Admin_role))
    if ctx.author.id==511206584869847042:
        os.chdir(os.path.dirname(__file__))
        with open("list.txt", mode="r") as f:
            data=f.read()
            save=data.replace(f"{str(国名)}","",1)
        with open("list.txt", mode="w") as f:
            f.write(f"{save}")
        embedding=discord.Embed(title="Good",description=f"{国名}をリストから削除しました",color=discord.Colour.green())
        embedding.set_footer(text=f"実行者:{ctx.author}",icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=embedding)
    else:
        Permission_error.set_footer(text=f"実行者:{ctx.author}",icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=Permission_error)
@bot.hybrid_command(name="リスト表示",description="リスト")
async def view(ctx):
    user=ctx.author
    role=ctx.guild.get_role(1055051387924398101)
    if ctx.author.id==511206584869847042:
        with open("list.txt", mode="r") as f:
            Description=f.read()
        embedding=discord.Embed(title="リスト",description=f"{Description}",color=discord.Colour.green())
        embedding.set_footer(text=f"実行者:{ctx.author}",icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=embedding)
    else:
        Permission_error.set_footer(text=f"実行者:{ctx.author}",icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=Permission_error)
@bot.event
async def on_ready():
    logger.info("Ally_botを起動しました")
    await bot.change_presence(activity=discord.Game(name="未来最高!未来最高!ｲｪｲｲｴｨ"),status=discord.Status.idle)
bot.run(token)
#ソース製作者:tagaiza2192