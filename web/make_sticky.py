import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update CSS
css_add = '''
  .esg-scroll-pin-wrapper {
    position: relative;
    height: 300vh;
  }
  .esg-stage-section {
    position: sticky;
    top: 0;
'''
content = content.replace('  .esg-stage-section {\n    position: relative;', css_add)

# 2. Update HTML Wrapper
content = content.replace('  <!-- 模組主舞台 -->\n  <section class="esg-stage-section" id="esgShowcase">', 
'''  <!-- 滾動釘選容器 (高度 300vh) -->
  <div class="esg-scroll-pin-wrapper" id="esgScrollWrap">
    <!-- 模組主舞台 (改為 sticky) -->
    <section class="esg-stage-section" id="esgShowcase">''')

content = content.replace('  </section>\n\n  <!-- 浮動圖片容器 -->', 
'''  </section>
  </div>

  <!-- 浮動圖片容器 -->''')


# 3. Update JS Logic
# Remove old wheel event listener
wheel_logic = '''    // 滾輪上下滾動切換
    const section = document.getElementById('esgShowcase');
    let isThrottled = false;

    section.addEventListener('wheel', (e) => {
      if (isThrottled) return;

      if (e.deltaY > 30) {
        if (currentIndex < totalCards - 1) {
          e.preventDefault();
          switchCard(currentIndex + 1);
          throttleScroll();
        }
      } else if (e.deltaY < -30) {
        if (currentIndex > 0) {
          e.preventDefault();
          switchCard(currentIndex - 1);
          throttleScroll();
        }
      }
    }, { passive: false });

    function throttleScroll() {
      isThrottled = true;
      setTimeout(() => {
        isThrottled = false;
      }, 550);
    }'''
content = content.replace(wheel_logic, '''    // 滾動偵測切換 (Sticky Scroll)
    window.addEventListener('scroll', () => {
      const esgWrap = document.getElementById('esgScrollWrap');
      if (!esgWrap) return;
      
      const rect = esgWrap.getBoundingClientRect();
      
      // 當 Sticky 區塊到達視窗頂部時開始計算
      if (rect.top <= 0 && rect.bottom >= window.innerHeight) {
        const scrollRange = rect.height - window.innerHeight; 
        const scrolled = -rect.top; 
        const progress = Math.max(0, Math.min(1, scrolled / scrollRange));
        
        let newIndex = 0;
        if (progress < 0.33) newIndex = 0;
        else if (progress < 0.66) newIndex = 1;
        else newIndex = 2;
        
        if (newIndex !== currentIndex) {
          switchCard(newIndex);
        }
      } else if (rect.top > 0) {
        if (currentIndex !== 0) switchCard(0);
      } else if (rect.bottom < window.innerHeight) {
        if (currentIndex !== 2) switchCard(2);
      }
    });''')

# Update navigateCard to scroll the page instead of just switching cards
navigate_old = '''    function navigateCard(direction) {
      let nextIndex = (currentIndex + direction + totalCards) % totalCards;
      switchCard(nextIndex);
    }'''

navigate_new = '''    function navigateCard(direction) {
      let nextIndex = (currentIndex + direction + totalCards) % totalCards;
      
      const esgWrap = document.getElementById('esgScrollWrap');
      if (esgWrap) {
        const scrollRange = esgWrap.offsetHeight - window.innerHeight;
        // nextIndex 為 0, 1, 2
        // 計算對應的滾動進度比例 (0%, 50%, 100%)
        const targetScrolled = (nextIndex / 2) * scrollRange; 
        // 算出該滾動到的絕對 Y 座標
        const targetY = esgWrap.offsetTop + targetScrolled;
        window.scrollTo({ top: targetY, behavior: 'smooth' });
      } else {
        switchCard(nextIndex);
      }
    }'''
content = content.replace(navigate_old, navigate_new)

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Sticky scroll implemented.")
