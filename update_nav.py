import re

css_path = "c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/css/style.css"
html_path = "c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/index.html"

# --- UPDATE HTML ---
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the existing header with the new structure
old_header = """  <!--Header_section-->
  <header id="header_wrapper">
    <div class="container">
      <div class="header_box">
        <div class="logo"><a href="#">LUMINA</a></div>
        <nav class="navbar navbar-inverse" role="navigation">
          <div class="navbar-header">
            <button type="button" id="nav-toggle" class="navbar-toggle" data-toggle="collapse" data-target="#main-nav">
              <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span
                class="icon-bar"></span> <span class="icon-bar"></span> </button>
          </div>
          <div id="main-nav" class="collapse navbar-collapse navStyle">
            <ul class="nav navbar-nav" id="mainNav">
              <li class="active"><a href="#hero" class="scroll-link">Home</a></li>
              <li><a href="#aboutUs" class="scroll-link">The Salon</a></li>
              <li><a href="#service" class="scroll-link">Services</a></li>
              <li><a href="#Portfolio" class="scroll-link">Gallery</a></li>
              <li><a href="#experience" class="scroll-link">Reviews</a></li>
              <li><a href="#contact" class="scroll-link">Contact</a></li>
            </ul>
          </div>
        </nav>
      </div>
    </div>
  </header>
  <!--Header_section-->"""

new_header = """  <!--Header_section-->
  <header id="header_wrapper">
    <div class="container nav-container">
      <div class="header_box">
        <div class="logo">
           <a href="#hero" class="scroll-link">
             <span class="logo-title">LUMINA</span>
             <span class="logo-subtitle">SALON & SPA</span>
           </a>
        </div>
        <nav class="navbar navbar-inverse" role="navigation">
          <div class="navbar-header">
            <button type="button" id="nav-toggle" class="navbar-toggle" data-toggle="collapse" data-target="#main-nav">
              <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span
                class="icon-bar"></span> <span class="icon-bar"></span> </button>
          </div>
          <div id="main-nav" class="collapse navbar-collapse navStyle">
            <ul class="nav navbar-nav" id="mainNav">
              <li class="active"><a href="#hero" class="scroll-link">Home</a></li>
              <li><a href="#aboutUs" class="scroll-link">The Salon</a></li>
              <li><a href="#service" class="scroll-link">Services</a></li>
              <li><a href="#Portfolio" class="scroll-link">Gallery</a></li>
              <li><a href="#experience" class="scroll-link">Reviews</a></li>
              <li class="nav-cta-item"><a href="#contact" class="scroll-link nav-btn">Get in Touch</a></li>
            </ul>
          </div>
        </nav>
      </div>
    </div>
  </header>
  <!--Header_section-->"""

if old_header in html:
    html = html.replace(old_header, new_header)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("HTML replaced")

# --- UPDATE CSS ---
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

new_nav_css = """/* Nav & Header (Floating Pill Style) */
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

.nav-container {
    padding: 0 15px; /* Keep container from touching edges completely */
}

.header_box {
    background: #0d6efd; /* Bright blue from image */
    border-radius: 50px;
    padding: 10px 25px 10px 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 10px 30px rgba(13, 110, 253, 0.2);
}

.logo {
    display: flex;
    align-items: center;
}

.logo a {
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif !important;
    display: flex;
    flex-direction: column;
    justify-content: center;
    line-height: 1.1;
    text-decoration: none;
}

.logo-title {
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: capitalize;
}

.logo-subtitle {
     font-size: 10px;
     font-weight: 500;
     letter-spacing: 2px;
     color: rgba(255, 255, 255, 0.7);
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
    margin: 0 10px;
}

.navStyle ul li a {
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 0px;
    text-transform: capitalize;
    transition: opacity 0.3s ease;
    padding: 10px 15px !important;
}

.navStyle ul li a:hover,
.navStyle > li.active > a,
.navbar-inverse .navbar-nav > .active > a {
    color: #FFFFFF !important;
    opacity: 0.8;
}

/* Specific styling for the 'Get in Touch' button in nav */
.nav-cta-item {
    margin-left: 20px !important;
}

.nav-btn {
    background-color: #1a1e29 !important; /* Dark slate color from image */
    color: #FFFFFF !important;
    border-radius: 30px !important;
    padding: 10px 24px !important;
    transition: all 0.3s ease;
    border: 1px solid transparent;
}

.nav-btn:hover {
    background-color: #0d1017 !important;
    transform: translateY(-2px);
    opacity: 1 !important;
}
"""

if "/* Nav & Header */" in css:
    start_idx = css.find("/* Nav & Header */")
    end_idx = css.find("/* Hero Section */")
    
    if start_idx != -1 and end_idx != -1:
        css = css[:start_idx] + new_nav_css + css[end_idx:]
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css)
        print("CSS replaced using indexes successfully")
    else:
        print("Could not find end index")
else:
    print("Could not find start index")
