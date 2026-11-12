import os 
import discord
from discord.ext import commands
# إعداد الصلاحيات الأساسية للبوت
intents = discord.Intents.default()
intents.message_content = True
# تعريف بادئة الأوامر (مثلاً علامة التعجب !)
bot = commands.Bot(command_prefix="!*,
intents=intents)
@bot.event
async def on_ready:
اتم تسجيل الدخول بنجاح باسم")
# أمر تجريبي بسيط للتأكد أن البوت يعمل
@bot.command
async def ping(ctx):
await ctx.send("ساعة 24 أهلاً بك! البوت شغال وجاهز
# تشغيل البوت باستخدام التوكن المخزن في إعدادات المنصة
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
