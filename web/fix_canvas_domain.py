import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Move <canvas> and add <div id="blueDomain">
old_esg_start = '''  <!-- 滾動釘選容器 (高度 300vh) -->
  <div class="esg-scroll-pin-wrapper" id="esgScrollWrap">
    <!-- 模組主舞台 (改為 sticky) -->
    <section class="esg-stage-section" id="esgShowcase">
    <!-- 純淺藍水暈渲染 Canvas (海軍深藍 #00264F 底色) -->
    <canvas id="fluidCanvas"></canvas>'''

new_esg_start = '''  <!-- 藍色連續領域，讓 Canvas 當作整體的背景 -->
  <div id="blueDomain" style="position: relative; background: #00264F;">
    <canvas id="fluidCanvas" style="position: sticky; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0; pointer-events: none; display: block;"></canvas>
    
    <div style="position: relative; z-index: 1; margin-top: -100vh;">
      <!-- 滾動釘選容器 (高度 300vh) -->
      <div class="esg-scroll-pin-wrapper" id="esgScrollWrap">
        <!-- 模組主舞台 (改為 sticky) -->
        <section class="esg-stage-section" id="esgShowcase" style="background: transparent;">'''

content = content.replace(old_esg_start, new_esg_start)

# 2. Add closing tags after footer
old_footer_end = '''      </div>
    </div>
  </div>
</footer>'''
new_footer_end = '''      </div>
    </div>
  </div>
</footer>
    </div><!-- End of relative content wrapper -->
  </div><!-- End of blueDomain -->'''

content = content.replace(old_footer_end, new_footer_end)

# 3. Make the background of contact and footer transparent
content = content.replace('background-color: #00264F;', 'background-color: transparent;')
content = content.replace('background-color: var(--c-navy-bg);', 'background-color: transparent;')

# 4. Update canvas resize logic
old_resize = '''    function resizeCanvas() {
      const section = document.getElementById('esgShowcase');
      width = canvas.width = section.offsetWidth;
      height = canvas.height = section.offsetHeight;
      ctx.fillStyle = '#00264F';
      ctx.fillRect(0, 0, width, height);
    }'''

new_resize = '''    function resizeCanvas() {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
      ctx.fillStyle = '#00264F';
      ctx.fillRect(0, 0, width, height);
    }'''

content = content.replace(old_resize, new_resize)

# 5. Make sure the body margin-bottom is not messed up (I removed syncFooterReveal earlier)
# And the canvas CSS for fluidCanvas is now inline, but I should remove the old CSS just in case.
old_canvas_css = '''    #fluidCanvas {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1; /* 在卡片底層 */
      pointer-events: none;
    }'''
content = content.replace(old_canvas_css, '    /* fluidCanvas CSS moved inline */')

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Canvas extended.")
