import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. CSS Additions
new_css = '''
  /* NEW: 白底聯絡表單 */
  .contact-extended-section {
    background-color: var(--ci-abundant-blue);
    padding: 60px 0 100px 0;
  }
  .white-block-form {
    background: #ffffff;
    border-radius: 32px;
    display: flex;
    overflow: hidden;
    box-shadow: 0 40px 80px rgba(0,0,0,0.2);
    min-height: 640px;
  }
  .white-block-img {
    flex: 1.1;
    min-width: 400px;
  }
  .white-block-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .white-block-content {
    flex: 1;
    padding: 60px 80px;
    color: var(--text);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .wb-title {
    font-size: 2.2rem;
    font-weight: 700;
    margin-bottom: 12px;
    color: var(--ci-abundant-blue);
  }
  .wb-desc {
    font-size: 0.95rem;
    color: var(--text-soft);
    margin-bottom: 40px;
  }
  
  .form-light-group {
    margin-bottom: 24px;
  }
  .form-2-split {
    display: flex;
    gap: 20px;
  }
  .form-2-split > .form-light-group {
    flex: 1;
  }
  .form-light-label {
    display: block;
    font-family: var(--font-en);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    color: var(--text-soft);
    margin-bottom: 8px;
  }
  .form-light-input, .form-light-select, .form-light-textarea {
    width: 100%;
    background: #F4F6F7;
    border: 1px solid transparent;
    border-radius: 12px;
    padding: 16px 20px;
    font-family: var(--font-cn);
    font-size: 0.95rem;
    color: var(--text);
    transition: all 0.3s;
  }
  .form-light-input:focus, .form-light-select:focus, .form-light-textarea:focus {
    outline: none;
    border-color: var(--ci-boundless-blue);
    background: #ffffff;
    box-shadow: 0 0 0 4px rgba(0, 139, 156, 0.1);
  }
  .btn-submit-light {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: #ffffff;
    color: var(--ci-abundant-blue);
    border: 1px solid var(--ci-abundant-blue);
    border-radius: 30px;
    padding: 16px 40px;
    font-family: var(--font-en);
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    cursor: pointer;
    transition: all 0.3s;
    margin-top: 10px;
    width: 100%;
  }
  .btn-submit-light:hover {
    background: var(--ci-abundant-blue);
    color: #ffffff;
  }
  .toast-san {
    position: fixed;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--ci-abundant-blue);
    color: #fff;
    padding: 16px 32px;
    border-radius: 30px;
    font-family: var(--font-en);
    font-weight: 600;
    font-size: 0.9rem;
    display: none;
    align-items: center;
    gap: 12px;
    z-index: 9999;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
  }
'''
content = content.replace('</style>', new_css + '\n</style>')

# 2. Update Footer CSS
footer_css_old = '''  .footer-luxury-ancors {
    background-color: var(--ci-deep-black);
    color: #FFFFFF;
    padding: 100px 0 36px 0;
    position: relative;
    overflow: hidden;
    border-top: 1px solid rgba(0, 139, 156, 0.25);
  }'''
footer_css_new = '''  .footer-luxury-ancors {
    background-color: var(--ci-abundant-blue);
    color: #FFFFFF;
    padding: 60px 0 36px 0;
    position: relative;
    overflow: hidden;
    border-top: none;
  }'''
content = content.replace(footer_css_old, footer_css_new)

# Remove giant wordmark CSS
content = re.sub(r'/\* 頁尾巨幅字.*?\.footer-giant-wordmark img {.*?\n  }', '', content, flags=re.DOTALL)

# 3. HTML Structure
form_html = '''
  <!-- NEW: 白底聯絡表單區塊 -->
  <section class="contact-extended-section" id="inquiry">
    <div class="wrap">
      <div class="white-block-form">
        <!-- 左半邊：情境圖 -->
        <div class="white-block-img">
          <img src="hero-noir.jpg" alt="SEAWORTH Contact">
        </div>
        <!-- 右半邊：表單 -->
        <div class="white-block-content">
          <h3 class="wb-title">Get in Touch</h3>
          <p class="wb-desc">請詳細說明您的需求，我們的專員將盡快與您聯繫並提供專業顧問服務。</p>
          <form id="sanContactForm" onsubmit="handleFormSubmit(event)">
            <div class="form-light-group">
                <label class="form-light-label" for="serviceSelect">SELECT INQUIRY CATEGORY *</label>
                <select id="serviceSelect" class="form-light-select" required>
                    <option value="" disabled selected>請選擇洽詢事項類別</option>
                    <option value="IR">投資人關係洽詢 (invest@seaworth.com)</option>
                    <option value="Partnership">商務合作與業務洽詢 (partnership@seaworth.com)</option>
                    <option value="PR">公共關係與媒體事務 (pr@seaworth.com)</option>
                    <option value="Other">其他合作事宜</option>
                </select>
            </div>

            <div class="form-2-split">
                <div class="form-light-group">
                    <label class="form-light-label" for="nameField">YOUR NAME *</label>
                    <input type="text" id="nameField" class="form-light-input" placeholder="例如：陳經理" required>
                </div>
                <div class="form-light-group">
                    <label class="form-light-label" for="companyField">COMPANY NAME *</label>
                    <input type="text" id="companyField" class="form-light-input" placeholder="例如：全球海運貿易集團" required>
                </div>
            </div>

            <div class="form-2-split">
                <div class="form-light-group">
                    <label class="form-light-label" for="phoneField">PHONE</label>
                    <input type="tel" id="phoneField" class="form-light-input" placeholder="+886 912 345 678">
                </div>
                <div class="form-light-group">
                    <label class="form-light-label" for="emailField">EMAIL *</label>
                    <input type="email" id="emailField" class="form-light-input" placeholder="name@domain.com" required>
                </div>
            </div>

            <div class="form-light-group">
                <label class="form-light-label" for="messageField">MESSAGE *</label>
                <textarea id="messageField" class="form-light-textarea" rows="2" placeholder="請詳細說明您的需求與合作構想..." required></textarea>
            </div>

            <button type="submit" class="btn-submit-light">
                SEND INQUIRY →
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>

</main>'''

content = content.replace('</main>', form_html)

# Add Toast HTML
toast_html = '''
  <!-- 訊息送出 Toast 反饋 -->
  <div class="toast-san" id="sanToast">
    <i data-lucide="check" style="width: 18px; height: 18px;"></i>
    <span>INQUIRY SUBMITTED SUCCESSFULLY.</span>
  </div>
'''
content = content.replace('</footer>', '</footer>\n' + toast_html)

# Remove Giant Wordmark HTML
content = re.sub(r'<!-- 頁尾超巨大實心字.*?</div>\n  </div>', '', content, flags=re.DOTALL)

# Remove JS
js_to_remove = r'// 設定頁尾揭示特效的 margin 與視差滾動 \(Parallax\).*?giant\.style\.transform = `translateY\(\$\{sink\}px\)`;\n    }\n  \}\);'
content = re.sub(js_to_remove, '', content, flags=re.DOTALL)

# Add Form JS
form_js = '''
  function handleFormSubmit(e) {
      e.preventDefault();
      const toast = document.getElementById('sanToast');
      toast.style.display = 'flex';
      
      document.getElementById('sanContactForm').reset();

      setTimeout(() => {
          toast.style.display = 'none';
      }, 4500);
  }
'''
content = content.replace('lucide.createIcons();', 'lucide.createIcons();\n' + form_js)


with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Applied changes.")
