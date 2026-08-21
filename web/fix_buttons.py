import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove .bottom-nav-controls completely
content = re.sub(r'<!-- 底部控制按鈕 -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# Insert .arrow-btn-group at the end of .right-info-display
arrow_buttons = '''
        <div class="arrow-btn-group" style="margin-top: 32px;">
          <button class="btn-ctrl" onclick="navigateCard(-1)"><i data-lucide="arrow-left" style="width: 18px; height: 18px;"></i></button>
          <button class="btn-ctrl" onclick="navigateCard(1)"><i data-lucide="arrow-right" style="width: 18px; height: 18px;"></i></button>
        </div>
'''

content = content.replace('      </div>\n    </div>\n\n    <!-- 下半部：右下方 3D 斜向透視卡片畫廊 (點選卡片直接切換對應資訊) -->',
arrow_buttons + '      </div>\n    </div>\n\n    <!-- 下半部：右下方 3D 斜向透視卡片畫廊 (點選卡片直接切換對應資訊) -->')


with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Buttons moved.")
