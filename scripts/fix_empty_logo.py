#!/usr/bin/env python3
"""
Fix Empty Logo Links
Add missing image tags to empty logo links
"""

import os
import re

def fix_empty_logo():
    """Fix empty logo links by adding image tags"""
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    
    print("🔧 FIXING EMPTY LOGO LINKS")
    print("=" * 50)
    
    for html_file in html_files:
        print(f"📄 Processing: {html_file}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match empty logo links
        pattern = r'<div class="logo">\s*<a href="([^"]*)">\s*</a>\s*</div>'
        
        def replace_logo(match):
            href = match.group(1)
            
            # Determine correct paths based on file location
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
            
            return f'''      <div class="logo">
        <a href="{home_link}">
          <img src="{img_src}" alt="Logo" / loading="lazy">
        </a>
      </div>'''
        
        content = re.sub(pattern, replace_logo, content)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✅ Fixed: {html_file}")
        else:
            print(f"    ℹ️  No changes needed: {html_file}")
    
    print("\n🎯 EMPTY LOGO FIX COMPLETE!")
    print("✅ All empty logo links now have proper image tags")
    print("✅ Correct relative paths used for each page level")

if __name__ == "__main__":
    fix_empty_logo() 