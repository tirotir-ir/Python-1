#pip install jdatetime
import tkinter as tk
import datetime
import jdatetime

def get_dates():
    # تاریخ امروز میلادی
    today_gregorian = datetime.datetime.now()
    gregorian_date = today_gregorian.strftime('%Y-%m-%d')

    # تبدیل تاریخ میلادی به تاریخ شمسی
    today_jalali = jdatetime.date.today()
    jalali_date = today_jalali.strftime('%Y/%m/%d')

    return gregorian_date, jalali_date

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("نمایش تقویم")

# دریافت تاریخ‌ها
gregorian_date, jalali_date = get_dates()

# ایجاد و نمایش برچسب‌ها
label_gregorian = tk.Label(root, text=f"تاریخ امروز میلادی: {gregorian_date}", font=("Arial", 14))
label_gregorian.pack(pady=10)

label_jalali = tk.Label(root, text=f"تاریخ امروز شمسی: {jalali_date}", font=("Arial", 14))
label_jalali.pack(pady=10)

# شروع حلقه اصلی برنامه
root.mainloop()
