import re

with open("index-A.html", "r", encoding="utf-8") as f:
    content = f.read()

# Revert to #00264F
content = content.replace('--c-navy-bg: var(--ci-abundant-blue);', '--c-navy-bg: #00264F;')

# Fix contact form background
old_contact = '''  .contact-extended-section {
    background-color: var(--ci-abundant-blue);'''
new_contact = '''  .contact-extended-section {
    background-color: #00264F;'''
content = content.replace(old_contact, new_contact)

# Fix footer background
old_footer = '''  footer.footer-luxury-ancors {
    background-color: var(--ci-abundant-blue);'''
new_footer = '''  footer.footer-luxury-ancors {
    background-color: #00264F;'''
content = content.replace(old_footer, new_footer)

with open("index-A.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Colors fixed.")
