import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update CSS
old_css = '''  .white-block-img {
    flex: 1.1;
    min-width: 400px;
  }'''
new_css = '''  .white-block-img {
    flex: 1.1;
    min-width: 400px;
    position: relative;
  }
  .wb-img-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 60px;
    background: linear-gradient(to top, rgba(0,0,0,0.7), transparent);
    color: #fff;
  }
  .wb-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #ffffff;
    color: #000000;
    font-size: 0.8rem;
    font-weight: 700;
    font-family: var(--font-en);
    padding: 8px 16px;
    border-radius: 30px;
    margin-bottom: 20px;
  }
  .wb-img-title {
    font-size: 2.8rem;
    font-weight: 700;
    line-height: 1.2;
    margin: 0;
    font-family: var(--font-en);
  }'''
content = content.replace(old_css, new_css)

# 2. Update HTML
old_html = '''        <!-- 左半邊：情境圖 -->
        <div class="white-block-img">
          <img src="hero-noir.jpg" alt="SEAWORTH Contact">
        </div>
        <!-- 右半邊：表單 -->
        <div class="white-block-content">
          <h3 class="wb-title">Get in Touch</h3>
          <p class="wb-desc">請詳細說明您的需求，我們的專員將盡快與您聯繫並提供專業顧問服務。</p>'''

new_html = '''        <!-- 左半邊：情境圖 -->
        <div class="white-block-img">
          <img src="assets/hero-noir.jpg" alt="SEAWORTH Contact">
          <div class="wb-img-overlay">
            <div class="wb-badge"><i data-lucide="message-square" style="width: 16px; height: 16px;"></i> Contact Us</div>
            <h2 class="wb-img-title">Get in Touch<br>with SEAWORTH</h2>
          </div>
        </div>
        <!-- 右半邊：表單 -->
        <div class="white-block-content">
          <p class="wb-desc">請詳細說明您的需求，我們的專員將盡快與您聯繫並提供專業顧問服務。</p>'''

content = content.replace(old_html, new_html)

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed left image and overlay.")
