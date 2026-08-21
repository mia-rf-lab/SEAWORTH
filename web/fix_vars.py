import re

with open("index (2).html", "r", encoding="utf-8") as f:
    src_content = f.read()

# Extract from src
css_vars = re.search(r'(:root\s*\{.*?\})', src_content, re.DOTALL).group(1)

with open("index-A.html", "r", encoding="utf-8") as f:
    dest_content = f.read()

# Inject the extracted :root block just before the newly added CSS rules
dest_content = dest_content.replace('/* 背景純淺藍水暈渲染 Canvas */', css_vars + '\n\n/* 背景純淺藍水暈渲染 Canvas */')

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(dest_content)

print("Variables injected.")
