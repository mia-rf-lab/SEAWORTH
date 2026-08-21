import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

old_vars = '''    /* 針對此模組的獨立變數 */
    .esg-stage-section {
      --c-navy-bg: #00264F;
      --c-navy-surface: #0a3560;
      --c-accent-cyan: #38bdf8;
      --c-accent-glow: #00d2ff;
      --c-gold-light: #dfca9b;
      --c-text-primary: #ffffff;
      --c-text-muted: #94a3b8;
      --c-line: rgba(255, 255, 255, 0.15);
      
      --font-display: 'Plus Jakarta Sans', sans-serif;
      --font-cinzel: 'Cinzel', serif;
      --font-serif: 'Noto Serif TC', serif;
      --font-sans: 'Noto Sans TC', sans-serif;
      --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
    }'''

new_vars = '''    /* 針對此模組的獨立變數 (已整合至主視覺系統) */
    .esg-stage-section {
      --c-navy-bg: var(--ci-abundant-blue); /* #00495B 或原深藍 */
      --c-navy-surface: rgba(255,255,255,0.05);
      --c-accent-cyan: var(--ci-boundless-blue);
      --c-accent-glow: rgba(0, 139, 156, 0.7);
      --c-gold-light: rgba(255, 255, 255, 0.85);
      --c-text-primary: #ffffff;
      --c-text-muted: rgba(255, 255, 255, 0.65);
      --c-line: rgba(255, 255, 255, 0.15);
      
      --font-display: var(--font-en);
      --font-cinzel: var(--font-en);
      --font-serif: var(--font-cn);
      --font-sans: var(--font-cn);
      --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
    }'''

content = content.replace(old_vars, new_vars)

# Also let's make sure the background of .esg-stage-section is using the new color.
# Actually --c-navy-bg is used. I'll just keep the #00264F if the user liked the original navy?
# The user said "這藍色區塊", and earlier "讓他純藍色就好".
# But SEAWORTH brand colors:
# --ci-abundant-blue: #00495B (Dark Teal / Navy)
# --ci-deep-black: #000000
# The original canvas color `#00264F` is standard navy.
# If I change `--c-navy-bg` to `var(--ci-abundant-blue)`, it matches perfectly with the brand.
# Let's write the file.

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Variables updated.")
