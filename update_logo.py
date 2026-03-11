import os

html_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/index.html'
gen_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/generate_service_pages.py'

# Replace in index.html
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('&copy; 2026 Lumina Luxury Salon.', '&copy; 2026 The Chennai Salon.')
content = content.replace('<span class="logo-title">THE CHENNAI</span>\n            <span class="logo-subtitle">SALON</span>', '<span class="logo-title" style="font-size: 20px; letter-spacing: 2px;">THE CHENNAI</span>\n            <span class="logo-subtitle" style="letter-spacing: 11px;">SALON</span>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Replace in generator script
with open(gen_path, 'r', encoding='utf-8') as f:
    gen_content = f.read()

gen_content = gen_content.replace('© 2026 Lumina Luxury Salon.', '© 2026 The Chennai Salon.')
gen_content = gen_content.replace('<span class="logo-title">THE CHENNAI</span>\n            <span class="logo-subtitle">SALON</span>', '<span class="logo-title" style="font-size: 20px; letter-spacing: 2px;">THE CHENNAI</span>\n            <span class="logo-subtitle" style="letter-spacing: 11px;">SALON</span>')

with open(gen_path, 'w', encoding='utf-8') as f:
    f.write(gen_content)

print('Updated logo sizing and footer copyright.')
