import re

html_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/index.html'
css_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/css/style.css'

# --- UPDATE HTML CACHE BUSTER ---
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update ?v=6 to ?v=7 for cache busting
html = html.replace('css/style.css?v=6', 'css/style.css?v=7')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# --- UPDATE CSS ---
new_gallery_css = """
/*==================================================
   Gallery Redesign (Premium Theme)
==================================================*/

/* Section Background */
#Portfolio {
    background-color: #FAFAFA;
}

/* Filter Navigation */
#filters {
    margin-bottom: 40px;
    text-align: center;
}

#filters ul {
    display: inline-flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
}

#filters ul li {
    margin: 0;
}

#filters ul li a {
    display: inline-block;
    padding: 10px 24px;
    background-color: transparent;
    border: 1px solid #E0E0E0;
    border-radius: 30px;
    color: #555555 !important;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    transition: all 0.3s ease;
    text-decoration: none;
}

#filters ul li a h5 {
    margin: 0;
    font-size: inherit;
    font-weight: inherit;
}

#filters ul li a:hover,
#filters ul li a.active {
    background-color: #1A1A1A;
    border-color: #1A1A1A;
    color: #D4AF37 !important;
    box-shadow: 0 4px 15px rgba(26, 26, 26, 0.1);
}

/* Gallery Grid Items */
.grid figure {
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 20px;
    background: #1A1A1A; /* Base color behind image */
}

.grid figure img {
    opacity: 1;
    transition: transform 0.5s ease, opacity 0.5s ease;
    width: 100%;
}

/* Override Oscar Effect with Luxury Theme */
figure.effect-oscar {
    background: #1A1A1A; /* Charcoal background for hover */
}

figure.effect-oscar figcaption::before {
    border: 1px solid rgba(212, 175, 55, 0.5); /* Gold elegant border */
    top: 20px;
    right: 20px;
    bottom: 20px;
    left: 20px;
    transition: all 0.4s ease;
}

figure.effect-oscar figcaption {
    background-color: rgba(26, 26, 26, 0.6); /* Translucent charcoal overlay */
    padding: 2em;
}

figure.effect-oscar h2 {
    color: #FFFFFF !important;
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    font-weight: 400;
    text-transform: capitalize;
    margin-top: 15%;
}

figure.effect-oscar h2 span {
    color: #D4AF37; /* Gold accent in title */
    font-style: italic;
    font-weight: 600;
}

figure.effect-oscar p {
    color: #E0E0E0;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    letter-spacing: 0.5px;
    text-transform: none;
    margin-top: 10px;
}

/* Hover States */
figure.effect-oscar:hover img {
    opacity: 0.3;
    transform: scale(1.05); /* Slight zoom on image */
}

figure.effect-oscar:hover figcaption::before {
    border-color: #D4AF37; /* Solid gold border on hover */
    top: 15px;
    right: 15px;
    bottom: 15px;
    left: 15px;
}

figure.effect-oscar:hover figcaption {
    background-color: rgba(26, 26, 26, 0.85); /* Darken overlay slightly */
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Append or replace the custom block
if '/*==================================================' in css and 'Gallery Redesign (Premium Theme)' in css:
    start_idx = css.find('/*==================================================')
    css = css[:start_idx] + new_gallery_css + '\n'
else:
    css = css + '\n' + new_gallery_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Gallery CSS and HTML cache buster updated successfully.")
