import re

css_path = "c:/Users/Bharathi/Desktop/beauty-salon-bootstrap-html5-template/css/style.css"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace magenta with charcoal/gold
css = css.replace("#BC2A87", "#1A1A1A") # Primary to Charcoal
css = css.replace("#A92178", "#1A1A1A") # Secondary to Charcoal (darker)
css = css.replace("#FF6C71", "#B76E79") # Some text to Rose Gold
css = css.replace("#ED5441", "#D4AF37") # Buttons to Gold
css = css.replace("#f56eab", "#D4AF37")
css = css.replace("#FFC0E8", "#A0A0A0") # Light pink text to light grey
css = css.replace("'Open Sans'", "'Inter'")
css = css.replace("'Raleway'", "'Playfair Display'")

# Add my custom overrides at the end
overrides = """
/* =========================================
   LUMINA PREMIUM OVERRIDES (PRO MAX UI/UX)
   ========================================= */

/* Typography & Base */
body {
    background-color: #FAFAFA;
    color: #4A4A4A;
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    line-height: 1.6;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', serif;
    color: #1A1A1A;
}

.section-title h2 {
    font-size: 42px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 15px;
    text-transform: none;
}

.section-title h6 {
    color: #7A7A7A;
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    font-weight: 400;
    margin-bottom: 50px;
}

.separator {
    width: 60px;
    height: 2px;
    background-color: #D4AF37;
    margin: 0 auto 20px auto;
}

.separator.bg-white {
    background-color: #FFFFFF;
}

/* Nav & Header */
#header_wrapper {
    background: rgba(26, 26, 26, 0.6) !important;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-top: none;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    padding: 20px 0;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 999;
    transition: all 0.3s ease;
}

.logo a {
    color: #FFFFFF !important;
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    letter-spacing: 2px;
    font-weight: 700;
    text-transform: uppercase;
}

.navStyle ul li a {
    color: #E0E0E0 !important;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: color 0.3s ease;
}

.navStyle ul li a:hover,
.navStyle > li.active > a,
.navbar-inverse .navbar-nav > .active > a {
    color: #D4AF37 !important;
}

/* Hero Section */
.hero-section {
    position: relative;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.hero-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    z-index: 1;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(10, 10, 10, 0.8) 0%, rgba(26, 26, 26, 0.4) 100%);
    z-index: 2;
}

.hero-content {
    position: relative;
    z-index: 3;
    padding-top: 80px;
}

.hero-title {
    font-size: 72px;
    color: #FFFFFF;
    margin-bottom: 20px;
    font-weight: 700;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

.hero-title span {
    color: #D4AF37;
    font-style: italic;
}

.hero-subtitle {
    font-size: 22px;
    color: #E0E0E0;
    margin-bottom: 40px;
    font-weight: 300;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* Buttons */
.btn-premium {
    display: inline-block;
    padding: 16px 36px;
    background-color: transparent;
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    border: 1px solid #D4AF37;
    border-radius: 0;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    position: relative;
    overflow: hidden;
    z-index: 1;
}

.btn-premium:hover {
    background-color: #D4AF37;
    color: #1A1A1A !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
}

/* The Salon Section */
#aboutUs {
    padding: 100px 0;
    background-color: #FFFFFF;
}

.about-img {
    border-radius: 2px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    transition: transform 0.5s ease;
}

.about-img:hover {
    transform: scale(1.02);
}

.about-text h3 {
    font-size: 32px;
    margin-bottom: 25px;
    color: #1A1A1A;
}

.about-text p {
    font-size: 16px;
    color: #555555;
    margin-bottom: 20px;
    font-weight: 300;
}

.about-us-list {
    margin-top: 30px;
    padding-left: 0;
}

.about-us-list li {
    font-size: 16px;
    color: #1A1A1A;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
}

.about-us-list li i {
    color: #D4AF37;
    margin-right: 15px;
    font-size: 18px;
}

/* Services */
#service {
    padding: 100px 0;
    background-color: #FAFAFA !important;
}

.service-card {
    background: #FFFFFF;
    padding: 40px 30px;
    text-align: center;
    border-radius: 4px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    height: 100%;
    margin-bottom: 30px;
    border: 1px solid transparent;
}

.service-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    border-color: #F0F0F0;
}

.service-icon {
    width: 80px;
    height: 80px;
    margin: 0 auto 25px;
    background: #1A1A1A;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.4s ease;
}

.service-card:hover .service-icon {
    background: #D4AF37;
}

.service-icon i {
    color: #FFFFFF;
    font-size: 32px;
}

.service-card h3 {
    font-size: 22px;
    margin-bottom: 15px;
    color: #1A1A1A !important;
}

.service-card p {
    color: #666666 !important;
    font-size: 15px;
}

/* Gallery Hover Updates */
figure.effect-oscar figcaption {
    background-color: rgba(26, 26, 26, 0.85) !important;
}

figure.effect-oscar h2 span {
    color: #D4AF37;
}

.Portfolio-nav li a {
    color: #1A1A1A;
    text-transform: uppercase;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    letter-spacing: 1px;
}

.Portfolio-nav li a.active, .Portfolio-nav li a:hover {
    color: #D4AF37;
}

/* Testimonials */
.testimonial-section {
    padding: 100px 0;
    background: linear-gradient(135deg, #1A1A1A 0%, #2A2A2A 100%);
    color: #FFFFFF;
}

.testimonial-section h2 {
    color: #FFFFFF;
}

.testimonial-section h6 {
    color: #E0E0E0;
}

.quote-icon i {
    font-size: 48px;
    color: #D4AF37;
    opacity: 0.5;
    margin-bottom: 30px;
}

.carousel-inner blockquote {
    border: none;
    padding: 0;
    margin: 0 0 30px 0;
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    font-style: italic;
    line-height: 1.6;
    color: #FFFFFF;
}

.client-info h5 {
    color: #D4AF37;
    margin: 0 0 5px 0;
    font-size: 18px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.client-info span {
    color: #A0A0A0;
    font-size: 14px;
}

/* Footer & Contact */
#contact {
    padding: 100px 0 0 0;
    background-color: #1A1A1A;
    color: #E0E0E0;
}

#contact h2 {
    color: #FFFFFF;
}

.contact_info .detail h4 {
    color: #D4AF37;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 5px;
}

.contact_info .detail p {
    color: #E0E0E0;
    font-size: 16px;
    margin-bottom: 25px;
}

.social_links {
    margin: 0;
    padding: 0;
}

.social_links li {
    display: inline-block;
    margin-right: 10px;
}

.social_links li a {
    width: 40px;
    height: 40px;
    border: 1px solid #555555;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #E0E0E0;
    transition: all 0.3s ease;
}

.social_links li a:hover {
    border-color: #D4AF37;
    color: #D4AF37;
    background: transparent;
}

.contact-form .input-text {
    width: 100%;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #FFFFFF;
    padding: 15px 20px;
    margin-bottom: 20px;
    border-radius: 2px;
    font-family: 'Inter', sans-serif;
    transition: border-color 0.3s ease;
}

.contact-form .input-text:focus {
    border-color: #D4AF37;
    outline: none;
}

.contact-form .text-area {
    min-height: 150px;
    resize: vertical;
}

.footer_bottom {
    background-color: #0A0A0A;
    padding: 25px 0;
    margin-top: 60px;
    color: #7A7A7A;
    font-size: 14px;
    text-align: center;
}

.footer_bottom a {
    color: #D4AF37;
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translate3d(0, 40px, 0);
    }
    to {
        opacity: 1;
        transform: translate3d(0, 0, 0);
    }
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css + overrides)
print("CSS updated successfully")
