#تمرین شماره 2 منزل: پیاده‌سازی درخت تصمیم برای برنامه زندگی روزانه
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# نمونه داده‌ها
# ویژگی‌ها: [دما, بارش, روز هفته]
# 0: دما پایین، 1: دما متوسط، 2: دما بالا
# 0: بدون بارش، 1: بارش
# 0: روز کاری، 1: روز تعطیل
features = np.array([
    [2, 0, 0], [0, 1, 0], [1, 0, 0], [2, 1, 0], [0, 0, 1], [1, 1, 1]
])

# برچسب‌ها: فعالیت‌های پیشنهادی
labels = np.array(['پیاده‌روی', 'مطالعه', 'دوچرخه‌سواری', 'فیلم دیدن', 'تفریح', 'خوابیدن'])

# ایجاد و آموزش مدل
clf = DecisionTreeClassifier()
clf.fit(features, labels)

# پیش‌بینی برای شرایط خاص
# مثال: دمای بالا، بدون بارش، روز تعطیل
new_conditions = np.array([[2, 0, 1]])
prediction = clf.predict(new_conditions)

print(f"برنامه پیشنهادی برای شما: {prediction[0]}")
