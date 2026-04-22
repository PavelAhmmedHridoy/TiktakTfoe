[app]

title = Stylish APK Demo
package.name = stylishapk
package.domain = org.demo

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# 🎨 ICON (add your icon file later)
# icon.filename = icon.png

# 🌐 IMPORTANT (for chat/socket apps)
android.permissions = INTERNET

# ⚡ better storage handling
android.private_storage = True

# 📱 Android version settings (important for stability)
android.minapi = 21
android.api = 33
android.ndk_api = 21

# 🧠 architecture (modern phones)
android.archs = arm64-v8a, armeabi-v7a

# 🚀 stable bootstrap
p4a.bootstrap = sdl2

# ⚙️ keep default entry
# android.entrypoint = org.kivy.android.PythonActivity
