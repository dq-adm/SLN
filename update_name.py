import os
import re

html_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/index.html'
gen_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/generate_service_pages.py'

def safe_replace(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replacements_html = [
    ('<span class="logo-title">LUMINA</span>\n            <span class="logo-subtitle">SALON & SPA</span>', '<span class="logo-title">THE CHENNAI</span>\n            <span class="logo-subtitle">SALON</span>'),
    ('<title>Lumina | Luxury Beauty Salon</title>', '<title>The Chennai Salon</title>'),
    ('At Lumina,', 'At The Chennai Salon,'),
    ('escape, Lumina is your destination', 'escape, The Chennai Salon is your destination'),
    ('Lumina transformed my hair completely.', 'The Chennai Salon transformed my hair completely.'),
    ('<h2>Visit Lumina</h2>', '<h2>Visit The Chennai Salon</h2>'),
    ('booking@luminasalon.com', 'booking@thechennaisalon.com'),
    ('© 2026 Lumina Luxury Salon', '© 2026 The Chennai Salon')
]

replacements_gen = [
    ('<span class="logo-title">LUMINA</span>\n            <span class="logo-subtitle">SALON & SPA</span>', '<span class="logo-title">THE CHENNAI</span>\n            <span class="logo-subtitle">SALON</span>'),
    ('<title>Lumina | {title}</title>', '<title>The Chennai Salon | {title}</title>'),
    ('hello@luminasalon.com', 'hello@thechennaisalon.com'),
    ('© 2026 Lumina Luxury Salon', '© 2026 The Chennai Salon')
]

safe_replace(html_path, replacements_html)
safe_replace(gen_path, replacements_gen)

print('Successfully updated branding to The Chennai Salon in index.html and generator script.')
