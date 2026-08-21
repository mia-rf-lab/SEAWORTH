with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

start = content.find('<section class="esg-stage-section" id="esgShowcase">')
end = content.find('</section>', start) + 10
print(content[start:end])
