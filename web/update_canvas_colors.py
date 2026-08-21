import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("ctx.fillStyle = '#00264F';", "ctx.fillStyle = '#00495B';")
content = content.replace("ctx.fillStyle = 'rgba(0, 38, 79, 0.06)';", "ctx.fillStyle = 'rgba(0, 73, 91, 0.06)';")

# Also the inkBlob color might be hardcoded cyan? Let's check.
