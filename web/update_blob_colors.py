import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

old_gradients = '''        gradient.addColorStop(0, `rgba(224, 242, 254, ${blob.alpha * 0.9})`);
        gradient.addColorStop(0.35, `rgba(56, 189, 248, ${blob.alpha * 0.6})`);
        gradient.addColorStop(0.7, `rgba(0, 210, 255, ${blob.alpha * 0.25})`);
        gradient.addColorStop(1, 'rgba(0, 38, 79, 0)');'''

new_gradients = '''        gradient.addColorStop(0, `rgba(180, 230, 240, ${blob.alpha * 0.9})`);
        gradient.addColorStop(0.35, `rgba(0, 180, 200, ${blob.alpha * 0.6})`);
        gradient.addColorStop(0.7, `rgba(0, 139, 156, ${blob.alpha * 0.25})`);
        gradient.addColorStop(1, 'rgba(0, 73, 91, 0)');'''

content = content.replace(old_gradients, new_gradients)

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Blob colors updated.")
