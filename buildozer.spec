[app]
# (str) عنوان التطبيق
title = TikTok Info Pro

# (str) اسم الحزمة (Package name)
package.name = tiktok_info_pro

# (str) النطاق (Domain)
package.domain = org.tiktoktool

# (str) مجلد الكود المصدري (المجلد الحالي)
source.dir = .

# (list) الامتدادات التي سيتم تضمينها (مهم جداً تضمين html و json و py)
source.include_exts = py,png,jpg,kv,atlas,html,css,js,json

# (str) نسخة التطبيق
version = 1.0

# (list) المتطلبات البرمجية (هذا أهم سطر لنجاح التطبيق)
requirements = python3,kivy,flask,requests,beautifulsoup4,werkzeug,jinja2,itsdangerous,click,pyjnius,urllib3,charset-normalizer,idna

# (str) الواجهة (portrait للعمودي)
orientation = portrait

# (bool) هل التطبيق ملء الشاشة؟
fullscreen = 1

# (list) الصلاحيات (مهم جداً للوصول للإنترنت)
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) المستوى المستهدف للأندرويد (33 ممتاز حالياً)
android.api = 33
android.minapi = 21
android.ndk = 25b

# (list) المعماريات المدعومة (arm64 هي الأهم للجوالات الحديثة)
android.archs = arm64-v8a, armeabi-v7a

# (bool) قبول الرخص تلقائياً
android.accept_sdk_license = True

[buildozer]
# (int) مستوى السجل (2 تظهر لك الأخطاء بالتفصيل إذا حدثت)
log_level = 2

# (int) التحذير عند التشغيل كجذر (Root)
warn_on_root = 1

