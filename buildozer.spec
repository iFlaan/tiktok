[app]
title = TikTok Analyzer
package.name = tiktok.analyzer.pro
package.domain = org.yourname
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js,json
version = 1.0

# المكتبات المطلوبة للعمل على أندرويد
requirements = python3,kivy==2.1.0,flask==2.1.0,requests,beautifulsoup4,werkzeug==2.0.3,jinja2,itsdangerous,click,pyjnius,urllib3,charset-normalizer,idna

orientation = portrait
fullscreen = 1
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
