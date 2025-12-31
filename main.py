from kivy.app import App
from kivy.uix.webview import WebView # سنحتاج لتعديل هذا ليعمل على أندرويد
from android.runnable import run_on_ui_thread
from jnius import autoclass
import threading
import os

# استدعاء مكتبة Flask وتشغيلها في خلفية التطبيق
from app import app 

def start_flask():
    # تشغيل السيرفر داخلياً على منفذ 5000
    app.run(host='127.0.0.1', port=5000)

class TikTokApp(App):
    def build(self):
        # تشغيل سيرفر Flask في مسار منفصل (Thread)
        threading.Thread(target=start_flask, daemon=True).start()
        
        # إنشاء واجهة عرض الويب (WebView)
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        
        webview = WebView(activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.setWebViewClient(WebViewClient())
        webview.loadUrl('http://127.0.0.1:5000')
        
        activity.setContentView(webview)
        return webview

if __name__ == '__main__':
    TikTokApp().run()
