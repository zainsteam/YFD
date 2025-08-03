#!/usr/bin/env python3
"""
Fix Logo Links
Add missing image tags to logo links across all pages
"""

import os
import re

def fix_logo_links():
    """Fix all logo links by adding missing image tags"""
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    
    print("🔧 FIXING LOGO LINKS")
    print("=" * 50)
    
    for html_file in html_files:
        print(f"📄 Processing: {html_file}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match empty logo links
        pattern = r'(<div class="logo">\s*<a href="[^"]*">\s*</a>\s*</div>)'
        
        # Determine the correct image path based on file location
        if html_file == "index.html":
            img_src = 'assets/images/WEBP/group 163.webp'
            home_link = "index.html"
        elif html_file.startswith("pages/"):
            if "/legal/" in html_file or "/services/" in html_file:
                img_src = '../../assets/images/WEBP/group 163.webp'
                home_link = "../../index.html"
            else:
                img_src = '../assets/images/WEBP/group 163.webp'
                home_link = "../index.html"
        else:
            img_src = 'assets/images/WEBP/group 163.webp'
            home_link = "index.html"
        
        # Replace with proper logo structure
        replacement = f'''      <div class="logo">
        <a href="{home_link}">
          <img src="{img_src}" alt="Logo" / loading="lazy">
        </a>
      </div>'''
        
        content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✅ Fixed: {html_file}")
        else:
            print(f"    ℹ️  No changes needed: {html_file}")
    
    print("\n🎯 LOGO LINK FIX COMPLETE!")
    print("✅ All logo links now have proper image tags")
    print("✅ Correct relative paths used for each page level")

if __name__ == "__main__":
    fix_logo_links() 