import re

html_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ('href="img/portfolio_pic1.jpg" class="fancybox"', 'href="service-balayage.html"'),
    ('href="img/portfolio_pic2.jpg" class="fancybox"', 'href="service-bridal-glow.html"'),
    ('href="img/portfolio_pic3.jpg" class="fancybox"', 'href="service-oxygen-facial.html"'),
    ('href="img/portfolio_pic4.jpg" class="fancybox"', 'href="service-hot-stone-massage.html"'),
    ('href="img/portfolio_pic5.jpg" class="fancybox"', 'href="service-precision-cut.html"'),
    ('href="img/portfolio_pic6.jpg" class="fancybox"', 'href="service-evening-glamour.html"'),
    ('href="img/portfolio_pic7.jpg" class="fancybox"', 'href="service-restorative-mask.html"'),
    ('href="img/portfolio_pic8.jpg" class="fancybox"', 'href="service-aromatherapy-bath.html"')
]

for old, new in replacements:
    html = html.replace(old, new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html to link to dedicated service pages.')
