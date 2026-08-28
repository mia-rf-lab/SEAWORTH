import re

with open("index-A.html", "r") as f:
    content = f.read()

# We will inject the WebGL enhancement right after the original 2D ripple script ends
target_marker = "loopRipples();\n  })();"

webgl_enhancement = """loopRipples();
  })();

  // ========================================================
  // Hero 封面圖：超輕量化 WebGL 真實水波扭曲 (漸進式增強)
  // 若環境支援 (例如 localhost 伺服器)，會自動取代原本的 2D 線條
  // ========================================================
  (function () {
    const hero = document.querySelector('.hero');
    if (!hero) return;

    const glCanvas = document.createElement('canvas');
    glCanvas.style.position = 'absolute';
    glCanvas.style.inset = '0';
    glCanvas.style.width = '100%';
    glCanvas.style.height = '100%';
    glCanvas.style.zIndex = '1'; 
    glCanvas.style.pointerEvents = 'none';
    
    const stack = hero.querySelector('.hero-stack');
    if (stack) hero.insertBefore(glCanvas, stack);
    else hero.appendChild(glCanvas);

    const gl = glCanvas.getContext('webgl', { antialias: false, depth: false, alpha: false });
    if (!gl) return; 

    const vsSource = `
      attribute vec2 a_position;
      void main() { gl_Position = vec4(a_position, 0.0, 1.0); }
    `;
    const fsSource = `
      precision highp float;
      uniform sampler2D u_image;
      uniform vec2 u_resolution;
      uniform vec2 u_imageResolution;
      uniform vec3 u_ripples[12];
      
      void main() {
        vec2 ratio = u_resolution / u_imageResolution;
        float maxRatio = max(ratio.x, ratio.y);
        vec2 newSize = u_imageResolution * maxRatio;
        vec2 offset = (newSize - u_resolution) / 2.0;
        
        vec2 uv = (gl_FragCoord.xy + offset) / newSize;
        uv.y = 1.0 - uv.y; 
        
        vec2 displacement = vec2(0.0);
        for(int i = 0; i < 12; i++) {
          float p = u_ripples[i].z; 
          if(p > 0.0) {
            vec2 d = gl_FragCoord.xy - u_ripples[i].xy;
            float dist = length(d);
            float radius = p * 400.0; 
            float diff = abs(dist - radius);
            
            if (diff < 60.0) { 
              float wave = sin((dist - radius) * 0.15); 
              float strength = (1.0 - p) * (1.0 - diff / 60.0) * 0.025; 
              displacement += (d / dist) * wave * strength;
            }
          }
        }
        
        gl_FragColor = texture2D(u_image, uv - displacement);
      }
    `;
    
    function compile(type, source) {
      const shader = gl.createShader(type);
      gl.shaderSource(shader, source);
      gl.compileShader(shader);
      return shader;
    }
    const program = gl.createProgram();
    gl.attachShader(program, compile(gl.VERTEX_SHADER, vsSource));
    gl.attachShader(program, compile(gl.FRAGMENT_SHADER, fsSource));
    gl.linkProgram(program);
    gl.useProgram(program);
    
    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 1,-1, -1,1, -1,1, 1,-1, 1,1]), gl.STATIC_DRAW);
    const posLoc = gl.getAttribLocation(program, "a_position");
    gl.enableVertexAttribArray(posLoc);
    gl.vertexAttribPointer(posLoc, 2, gl.FLOAT, false, 0, 0);
    
    const resLoc = gl.getUniformLocation(program, "u_resolution");
    const imgResLoc = gl.getUniformLocation(program, "u_imageResolution");
    const ripplesLoc = gl.getUniformLocation(program, "u_ripples");

    const img = new Image();
    img.src = 'assets/kv-2.png';
    img.crossOrigin = "anonymous";
    let imgW = 1, imgH = 1;
    img.onload = () => {
      imgW = img.width; imgH = img.height;
      const texture = gl.createTexture();
      gl.bindTexture(gl.TEXTURE_2D, texture);
      
      try {
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, img);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        
        // WebGL 啟動成功，隱藏原本的 2D 圖片與舊 Canvas
        const heroImg = hero.querySelector('.hero-kv-img');
        if (heroImg) heroImg.style.opacity = '0';
        const oldCanvas = document.getElementById('heroRippleCanvas');
        if (oldCanvas) oldCanvas.style.display = 'none';
        
        startLoop();
      } catch (e) {
        console.warn("WebGL CORS Error: 採用預設 2D 水滴特效");
      }
    };

    let ripples = [];
    let lastSpawn = 0;
    let isAnimating = false;
    
    hero.addEventListener('pointermove', (e) => {
      const now = performance.now();
      if (now - lastSpawn > 70) { 
        const rect = glCanvas.getBoundingClientRect();
        const dpr = window.devicePixelRatio || 1;
        const x = (e.clientX - rect.left) * dpr;
        const y = glCanvas.height - ((e.clientY - rect.top) * dpr);
        ripples.push({x, y, p: 0});
        if (ripples.length > 12) ripples.shift(); 
        lastSpawn = now;
        
        if (!isAnimating) startLoop();
      }
    });

    function startLoop() {
      if (isAnimating) return;
      isAnimating = true;
      render();
    }

    function render() {
      const rect = hero.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      const cw = rect.width * dpr;
      const ch = rect.height * dpr;
      
      if (glCanvas.width !== cw || glCanvas.height !== ch) {
        glCanvas.width = cw; glCanvas.height = ch;
        gl.viewport(0, 0, cw, ch);
      }
      
      gl.uniform2f(resLoc, cw, ch);
      gl.uniform2f(imgResLoc, imgW, imgH);
      
      let hasActive = false;
      const rippleData = new Float32Array(12 * 3);
      for(let i = 0; i < 12; i++) {
        if (i < ripples.length) {
          let r = ripples[i];
          r.p += 0.015; 
          if (r.p < 1.0) hasActive = true;
          rippleData[i*3] = r.x;
          rippleData[i*3+1] = r.y;
          rippleData[i*3+2] = r.p;
        }
      }
      gl.uniform3fv(ripplesLoc, rippleData);
      
      gl.drawArrays(gl.TRIANGLES, 0, 6);
      
      if (hasActive) {
        requestAnimationFrame(render);
      } else {
        ripples = [];
        isAnimating = false;
      }
    }
  })();"""

idx = content.find(target_marker)
if idx != -1:
    new_content = content[:idx] + webgl_enhancement + content[idx + len(target_marker):]
    with open("index-A.html", "w") as f:
        f.write(new_content)
    print("Success")
else:
    print("Failed to find marker")
