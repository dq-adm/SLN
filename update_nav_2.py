import re

css_path = "c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/css/style.css"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

new_nav_css = """/* Nav & Header (Floating Pill Style - Themed) */
#header_wrapper {
    background: transparent !important;
    border-top: none;
    box-shadow: none;
    padding: 20px 0;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 999;
    transition: all 0.3s ease;
}

/* Ensure padding on scroll */
#header_wrapper.is-sticky {
    padding: 10px 0;
}

.nav-container {
    padding: 0 15px; 
}

.header_box {
    background: rgba(26, 26, 26, 0.95); /* Charcoal from Lumina theme */
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 50px;
    padding: 10px 25px 10px 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.logo {
    display: flex;
    align-items: center;
}

.logo a {
    color: #FFFFFF !important;
    font-family: 'Playfair Display', serif !important;
    display: flex;
    flex-direction: column;
    justify-content: center;
    line-height: 1.1;
    text-decoration: none;
}

.logo-title {
    font-size: 24px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.logo-subtitle {
     font-size: 10px;
     font-weight: 500;
     letter-spacing: 3px;
     color: #D4AF37; /* Gold accent */
     text-transform: uppercase;
}

.navbar {
    min-height: auto;
    margin: 0;
}

.navStyle ul {
    margin: 0;
    display: flex;
    align-items: center;
}

.navStyle ul li {
    margin: 0 5px;
}

.navStyle ul li a {
    color: #E0E0E0 !important;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.3s ease;
    padding: 10px 15px !important;
}

.navStyle ul li a:hover,
.navStyle > li.active > a,
.navbar-inverse .navbar-nav > .active > a {
    color: #D4AF37 !important; /* Gold hover */
}

/* Specific styling for the 'Get in Touch' button in nav */
.nav-cta-item {
    margin-left: 20px !important;
}

.nav-btn {
    background-color: transparent !important;
    color: #FFFFFF !important;
    border-radius: 30px !important;
    padding: 8px 24px !important;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    border: 1px solid #D4AF37 !important;
}

.nav-btn:hover {
    background-color: #D4AF37 !important;
    color: #1A1A1A !important;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(212, 175, 55, 0.2);
}

/* Mobile Toggle Reset */
.navbar-inverse .navbar-toggle {
    border-color: rgba(255,255,255,0.3);
    margin-top: 5px;
    margin-bottom: 5px;
}
.navbar-inverse .navbar-toggle:hover, .navbar-inverse .navbar-toggle:focus {
    background-color: rgba(255,255,255,0.1);
}
.navbar-inverse .navbar-toggle .icon-bar {
    background-color: #D4AF37;
}
"""

if "/* Nav & Header (Floating Pill Style) */" in css:
    start_idx = css.find("/* Nav & Header (Floating Pill Style) */")
    end_idx = css.find("/* Hero Section */")
    css = css[:start_idx] + new_nav_css + css[end_idx:]
elif "/* Nav & Header */" in css:
    start_idx = css.find("/* Nav & Header */")
    end_idx = css.find("/* Hero Section */")
    css = css[:start_idx] + new_nav_css + css[end_idx:]

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("CSS updated with themed pill navigation")
