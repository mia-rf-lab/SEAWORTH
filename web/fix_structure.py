import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix missing closing div for .esg-scroll-pin-wrapper
if '</section>\n\n  \n\n\n  <!-- NEW: 白底聯絡表單區塊 -->' in content:
    content = content.replace('</section>\n\n  \n\n\n  <!-- NEW: 白底聯絡表單區塊 -->', '</section>\n  </div>\n\n  <!-- NEW: 白底聯絡表單區塊 -->')
elif '</section>\n\n  <!-- NEW: 白底聯絡表單區塊 -->' in content:
    content = content.replace('</section>\n\n  <!-- NEW: 白底聯絡表單區塊 -->', '</section>\n  </div>\n\n  <!-- NEW: 白底聯絡表單區塊 -->')
else:
    # Let's just do a regex replace
    content = re.sub(r'</section>\s*<!-- NEW: 白底聯絡表單區塊 -->', r'</section>\n</div>\n\n<!-- NEW: 白底聯絡表單區塊 -->', content)

# Fix footer background color
footer_css_old = '''  footer.footer-luxury-ancors {
    background-color: var(--ci-deep-black);
    color: #FFFFFF;
    padding: 100px 0 36px 0;
    position: relative;
    overflow: hidden;
    border-top: 1px solid rgba(0, 139, 156, 0.25);
  }'''
footer_css_new = '''  footer.footer-luxury-ancors {
    background-color: var(--ci-abundant-blue);
    color: #FFFFFF;
    padding: 60px 0 36px 0;
    position: relative;
    overflow: hidden;
    border-top: none;
  }'''
content = content.replace(footer_css_old, footer_css_new)

# Make sure giant wordmark HTML is removed
content = re.sub(r'<div class="footer-giant-wrapper" id="giantWordmark">.*?</div>\s*</div>', '', content, flags=re.DOTALL)

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Structure fixed.")
