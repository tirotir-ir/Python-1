#pip install jdatetime
import datetime
import jdatetime

# تاریخ امروز میلادی
today_gregorian = datetime.datetime.now()
gregorian_date = today_gregorian.strftime('%Y-%m-%d')

# تبدیل تاریخ میلادی به تاریخ شمسی
today_jalali = jdatetime.date.today()
jalali_date = today_jalali.strftime('%Y/%m/%d')

print(f"تاریخ امروز میلادی: {gregorian_date}")
print(f"تاریخ امروز شمسی: {jalali_date}")
