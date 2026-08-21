with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add a dummy div to balance the flexbox space-between layout
dummy = '    <!-- Flexbox 平衡用 Spacer -->\n    <div class="bottom-nav-controls" style="visibility: hidden; pointer-events: none; height: 44px;"></div>\n  </section>'

content = content.replace('  </section>', dummy)

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Flexbox balanced.")
