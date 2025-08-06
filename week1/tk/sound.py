"""
import pyttsx3  # کتابخانه تبدیل متن به گفتار

engine = pyttsx3.init()  # مقداردهی اولیه موتور گفتار
engine.say("Hello!")  # تنظیم پیام گفتاری
engine.runAndWait()  # اجرای پیام گفتاری

"""

import pyttsx3  

text = input("چه چیزی می‌خواهید بگویید؟ ")  # گرفتن متن از کاربر
engine = pyttsx3.init()  
engine.say(text)  
engine.runAndWait()  
