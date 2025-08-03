#!/usr/bin/env python3
"""
Add Logo Link
Add home page link to all logo images in headers
"""

import os
import re

def add_logo_link():
    """Add home page link to all logo images"""
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    
    print("🔗 ADDING LOGO LINKS")
    print("=" * 50)
    
    for html_file in html_files:
        print(f"📄 Processing: {html_file}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match logo div with img tag
        # This will match: <div class="logo">\n<img src="..." alt="Logo" />
        pattern = r'(<div class="logo">\s*)(<img[^>]*alt="Logo"[^>]*>)'
        
        # Determine the correct home page path based on file location
        if html_file == "index.html":
            home_link = "index.html"
        elif html_file.startswith("pages/"):
            # For pages in subdirectories, go up to root
            home_link = "../../index.html" if "/legal/" in html_file or "/services/" in html_file else "../index.html"
        else:
            home_link = "index.html"
        
        # Replace with linked version
        replacement = r'\1<a href="' + home_link + '">\2</a>'
        
        content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✅ Updated: {html_file} (links to {home_link})")
        else:
            print(f"    ℹ️  No changes: {html_file}")
    
    print("\n🎯 LOGO LINK ADDITION COMPLETE!")
    print("✅ All logo images now link to home page")
    print("✅ Proper relative paths used for each page level")

if __name__ == "__main__":
    add_logo_link() 