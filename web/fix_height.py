import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update .esg-stage-section CSS
css_old = '''    .esg-stage-section {
      position: sticky;
      top: 0;
      z-index: 2;
      width: 100%;
      height: 100vh;
      background-color: var(--c-navy-bg);
      padding: 70px 0 0 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
    }'''

css_new = '''    .esg-stage-section {
      position: sticky;
      top: 0;
      z-index: 2;
      width: 100%;
      height: 100dvh;
      background-color: var(--c-navy-bg);
      padding: clamp(30px, 5vh, 80px) 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: clamp(20px, 4vh, 60px);
      overflow: hidden;
    }'''

content = content.replace(css_old, css_new)

# Update the wrapper to use dvh as well
content = content.replace('      height: 300vh;\n    }', '      height: 300dvh;\n    }')

# 2. Remove the dummy spacer from HTML
spacer = '''    <!-- Flexbox 平衡用 Spacer -->
    <div class="bottom-nav-controls" style="visibility: hidden; pointer-events: none; height: 44px;"></div>'''
content = content.replace(spacer, '')

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Height fixed.")
