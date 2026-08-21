import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. CSS
content = content.replace('''    #fluidCanvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 1;''', '''    #fluidCanvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1;''')

# 2. HTML
content = content.replace('''  <!-- 純淺藍水暈渲染 Canvas (海軍深藍 #00264F 底色) -->
  <canvas id="fluidCanvas"></canvas>

  <!-- 模組主舞台 -->
  <section class="esg-stage-section" id="esgShowcase">''', '''  <!-- 模組主舞台 -->
  <section class="esg-stage-section" id="esgShowcase">
    <!-- 純淺藍水暈渲染 Canvas (海軍深藍 #00264F 底色) -->
    <canvas id="fluidCanvas"></canvas>''')

# 3. JS Resize
content = content.replace('''    function resizeCanvas() {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;''', '''    function resizeCanvas() {
      const section = document.getElementById('esgShowcase');
      width = canvas.width = section.offsetWidth;
      height = canvas.height = section.offsetHeight;''')

# 4. JS Pointer
content = content.replace('''    window.addEventListener('pointermove', (e) => {
      pointer.vx = (e.clientX - pointer.x) * 0.35;
      pointer.vy = (e.clientY - pointer.y) * 0.35;
      pointer.x = e.clientX;
      pointer.y = e.clientY;''', '''    window.addEventListener('pointermove', (e) => {
      const rect = canvas.getBoundingClientRect();
      const clientX = e.clientX - rect.left;
      const clientY = e.clientY - rect.top;
      pointer.vx = (clientX - pointer.x) * 0.35;
      pointer.vy = (clientY - pointer.y) * 0.35;
      pointer.x = clientX;
      pointer.y = clientY;''')

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Canvas fixed.")
