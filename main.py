import os
import datetime

# --- BUILD Phase ---
# This section simulates the "Build" step: generating static content.
# In a real BPS setup, this could involve compiling code, bundling assets,
# or generating static pages from templates/markdown.

# Define content for our simple website
PAGE_TITLE = "BPS Felsefesi ile Hızlı Gelişim"
PAGE_HEADING = "Merhaba BPS Dünyası!"
PAGE_CONTENT = """
<p>Bu sayfa, BPS (Build, Push, Sleep) felsefesinin bir gösterimi olarak otomatik olarak oluşturulmuştur.</p>
<p>Geleneksel karmaşıklıklardan uzak, hızlı ve etkin web geliştirme için BPS yaklaşımını benimsiyoruz.</p>
<p>Sadece <b>İnşa Et</b> (Build), <b>Yayımla</b> (Push) ve sonra huzur içinde <b>Uyu</b> (Sleep).</p>
<p>Bu dosya, bir Python betiği tarafından oluşturuldu ve dağıtıma hazır hale getirildi.</p>
"""
BUILD_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Basic HTML template
HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{PAGE_TITLE}</title>
    <style>
        body {{ font-family: sans-serif; margin: 2em; line-height: 1.6; background-color: #f4f4f4; color: #333; }}
        .container {{ max-width: 800px; margin: auto; background: #fff; padding: 2em; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ color: #0056b3; }}
        footer {{ margin-top: 2em; padding-top: 1em; border-top: 1px solid #eee; text-align: center; font-size: 0.9em; color: #666; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{PAGE_HEADING}</h1>
        {PAGE_CONTENT}
        <footer>
            <p>Bu sayfa BPS felsefesiyle oluşturuldu. Oluşturulma Zamanı: {BUILD_TIME}</p>
        </footer>
    </div>
</body>
</html>
"""

OUTPUT_FILENAME = "index.html"

try:
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)
    print(f"'{OUTPUT_FILENAME}' başarıyla oluşturuldu. (Build Aşaması Tamamlandı)") # BPS: Build
except IOError as e:
    print(f"Hata: '{OUTPUT_FILENAME}' dosyası oluşturulamadı: {e}")
    exit(1)

# --- PUSH Phase (Simulated) ---
# In a real BPS scenario, this would involve deploying the generated 'index.html'
# to a web server, CDN, or static hosting service (e.g., 'git push' to Netlify/Vercel).
# Here, we simply confirm the file is ready for deployment.

print(f"'{OUTPUT_FILENAME}' dağıtıma hazır. (Push Aşaması Tamamlandı)") # BPS: Push
print("Şimdi bu dosyayı bir web sunucusuna yükleyebilir veya doğrudan tarayıcınızda açabilirsiniz.")

# --- SLEEP Phase ---
# The developer can now "sleep" knowing the build artifact is ready and pushed (or ready to be pushed).
# The system is stable and doesn't require constant monitoring from the build/push process itself.

print("BPS döngüsü tamamlandı. Huzur içinde uyuyabilirsiniz! (Sleep Aşaması)") # BPS: Sleep

# Instructions for viewing the generated file
print("\nOluşturulan web sayfasını görmek için:")
print(f"1. Tarayıcınızda '{OUTPUT_FILENAME}' dosyasını açın.")
print("Veya")
print("2. Terminalinizde 'python -m http.server' komutunu çalıştırın ve tarayıcınızda http://localhost:8000 adresine gidin.")
