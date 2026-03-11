import os
import re

directories = ['.']
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

meta_tags_to_remove = [
    r'<meta http-equiv="Content-Security-Policy" content="[^"]*">',
    r'<meta http-equiv="Permissions-Policy" content="[^"]*">',
    r'<meta http-equiv="Referrer-Policy" content="[^"]*">',
    r'<meta http-equiv="Strict-Transport-Security" content="[^"]*">',
    r'<meta http-equiv="X-Content-Type-Options" content="[^"]*">',
    r'<meta http-equiv="X-Frame-Options" content="[^"]*">',
]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for pattern in meta_tags_to_remove:
        new_content = re.sub(pattern + r'\s*', '', new_content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {filename}")
    else:
        print(f"No changes needed for {filename}")
