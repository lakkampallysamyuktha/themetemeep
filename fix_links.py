import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to change links for "Solar Energy", "Wind Turbines", "EV Charging", "Smart Grid", "Privacy Policy", "Terms & Conditions"
    # To point to "404.html".
    # The links look like: <a href="something">Solar Energy</a>
    
    # We will use regex to find and replace hrefs.
    patterns = [
        r'Solar Energy',
        r'Wind Turbines',
        r'EV Charging',
        r'Smart Grid',
        r'Privacy Policy',
        r'Terms & Conditions'
    ]
    
    for pattern in patterns:
        # Regex to match <a href="..." ...>pattern</a>
        # This replaces the href attribute value
        content = re.sub(
            r'(<a[^>]*?href=["\']).*?(["\'][^>]*?>' + pattern + r'</a>)', 
            r'\g<1>404.html\g<2>', 
            content
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links in all HTML files.")
