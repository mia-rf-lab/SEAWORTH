import re

with open("index (2).html", "r", encoding="utf-8") as f:
    src_content = f.read()

with open("index-A.html", "r", encoding="utf-8") as f:
    dest_content = f.read()

# Extract from src
css_vars = re.search(r'(:root\s*\{.*?\})', src_content, re.DOTALL).group(1)
css_rules = src_content[src_content.find('/* 背景純淺藍水暈渲染 Canvas */'):src_content.find('</style>')]
html_content = src_content[src_content.find('<!-- 純淺藍水暈渲染 Canvas (海軍深藍 #00264F 底色) -->'):src_content.find('<!-- 互動腳本：純淺藍水暈渲染 + 3D 切換邏輯 -->')]
js_content = src_content[src_content.find('lucide.createIcons();'):src_content.find('</script>\n</body>')]
lucide_script = '<script src="https://unpkg.com/lucide@latest"></script>'

# Inject into dest
# 1. CSS rules at the end of style block
dest_content = dest_content.replace('</style>', css_rules + '\n</style>')

# 2. HTML replace .motif section
motif_regex = re.compile(r'<!-- BRAND MOTIF -->.*?</section>', re.DOTALL)
dest_content = motif_regex.sub(html_content, dest_content)

# 3. JS at the end of script block
dest_content = dest_content.replace('</script>\n\n</body>', js_content + '\n</script>\n\n</body>')

# 4. Lucide script in head
dest_content = dest_content.replace('</head>', lucide_script + '\n</head>')

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(dest_content)

print("Merge completed successfully.")
