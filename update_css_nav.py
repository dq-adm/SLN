import sys

html_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/index.html'
css_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/css/style.css'
js_path = 'c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/js/custom.js'

with open(css_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = -1
end = -1
for i, line in enumerate(lines):
    if '/* Nav & Header' in line:
        start = i
    if '/* Hero Section' in line or '/* Mobile Toggle' in line or '/* Top_content' in line:
        if i > start and start != -1:
            end = i
            break

new_nav_css = '''/* Dynamic Nav Bar */
#header_wrapper {
    position: fixed;
    width: 100%;
    top: 0;
    left: 0;
    z-index: 9999;
    background: transparent;
    padding: 20px 0;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    border-top: none;
}

.nav-container {
    transition: all 0.4s ease;
    padding: 0 15px;
    max-width: 1100px;
    margin: 0 auto;
}

.header_box {
    background: rgba(26, 26, 26, 0.95);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 50px;
    padding: 10px 25px 10px 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.4s ease;
}

/* When at the top (not scrolled), make it touch the ends */
#header_wrapper.at-top {
    padding: 0;
    background: rgba(26, 26, 26, 0.95); /* solid at top */
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

#header_wrapper.at-top .nav-container {
    width: 100%;
    max-width: 100%;
    padding: 0 40px;
}

#header_wrapper.at-top .header_box {
    border-radius: 0;
    background: transparent;
    border: none;
    box-shadow: none;
    padding: 15px 0;
}

.logo { display: flex; align-items: center; }
.logo a {
    color: #FFFFFF !important;
    font-family: 'Playfair Display', serif !important;
    display: flex; flex-direction: column; justify-content: center;
    line-height: 1.1; text-decoration: none;
}
.logo-title { font-size: 24px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; float: none; line-height: 1.1;}
.logo-subtitle { font-size: 10px; font-weight: 500; letter-spacing: 3px; color: #D4AF37; text-transform: uppercase; float: none;}

.navbar { min-height: auto; margin: 0; border: none; }
.navStyle ul { margin: 0; display: flex; align-items: center; list-style: none; padding: 0; }
.navStyle ul li { margin: 0 5px; }
.navStyle ul li a {
    color: #E0E0E0 !important;
    font-family: 'Inter', sans-serif;
    font-size: 14px; font-weight: 500; letter-spacing: 1px;
    text-transform: uppercase; transition: all 0.3s ease; padding: 10px 15px !important; text-decoration: none; border: none !important;
}

.navStyle ul li a:hover,
.navStyle > li.active > a {
    color: #D4AF37 !important; background: transparent !important;
}

.nav-cta-item { margin-left: 20px !important; }
.nav-btn {
    background-color: transparent !important; color: #FFFFFF !important; border-radius: 30px !important; padding: 8px 24px !important;
    border: 1px solid #D4AF37 !important; transition: all 0.3s ease !important;
}
.nav-btn:hover { background-color: #D4AF37 !important; color: #1A1A1A !important; transform: translateY(-2px); }

/* Remove default bootstrap navbar borders */
.navbar-inverse, .navbar-collapse {
    border-color: transparent !important;
    box-shadow: none !important;
}

/* Adjust res-nav_click */
.res-nav_click { display: none; }

'''

if start != -1 and end != -1:
    lines = lines[:start] + [new_nav_css + '\n'] + lines[end:]
    with open(css_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('CSS Updated!')
else:
    print('Could not find CSS block boundaries')

