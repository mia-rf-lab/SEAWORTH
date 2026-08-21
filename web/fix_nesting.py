import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove </main> before footer
content = content.replace('</section>\n\n</main>\n\n<footer id="contact" class="footer-luxury-ancors">', '</section>\n\n<footer id="contact" class="footer-luxury-ancors">')

# Re-add </main> after blueDomain
content = content.replace('  </div><!-- End of blueDomain -->', '  </div><!-- End of blueDomain -->\n</main>')

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Nesting fixed.")
