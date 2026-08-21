with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Undo the bad spacer and stray </div> in .solutions
bad_part = '''    <!-- Flexbox 平衡用 Spacer -->
    <div class="bottom-nav-controls" style="visibility: hidden; pointer-events: none; height: 44px;"></div>
  </section>
  </div>'''

content = content.replace(bad_part, '  </section>')

# 2. Add the spacer and closing </div> to .esg-stage-section
# Let's find the closing tag of esg-stage-section
# It should be after "</div>\n    </div>\n\n  </section>"
# The actual content around it is:
#         </div>
# 
#       </div>
#     </div>
# 
#   </section>
# 
# </main>
import re

target = r'      </div>\n    </div>\n\n  </section>\n\n\n</main>'
replacement = '''      </div>
    </div>

    <!-- Flexbox 平衡用 Spacer -->
    <div class="bottom-nav-controls" style="visibility: hidden; pointer-events: none; height: 44px;"></div>
  </section>
  </div>


</main>'''

content = re.sub(target, replacement, content)

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("HTML structure fixed.")
