#!/usr/bin/env python3
"""
Add Bebas Neue Font
Add Google Fonts Bebas Neue link to all HTML files
"""

import os
import re

def add_bebas_font():
    """Add Bebas Neue Google Fonts link to all HTML files"""
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    
    print("🔤 ADDING BEBAS NEUE FONT")
    print("=" * 50)
    
    for html_file in html_files:
        print(f"📄 Processing: {html_file}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Check if Bebas Neue font is already linked
        if 'fonts.googleapis.com/css2?family=Bebas+Neue' in content:
            print(f"    ℹ️  Already has Bebas Neue: {html_file}")
            continue
        
        # Add Google Fonts preconnect and font link
        # Find the head tag and add font links before the closing head tag
        head_pattern = r'(<head[^>]*>)'
        
        def add_font_links(match):
            head_tag = match.group(1)
            font_links = '''  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">'''
            return head_tag + '\n' + font_links
        
        content = re.sub(head_pattern, add_font_links, content)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✅ Added Bebas Neue: {html_file}")
        else:
            print(f"    ℹ️  No changes needed: {html_file}")
    
    print("\n🎯 BEBAS NEUE FONT ADDITION COMPLETE!")
    print("✅ All HTML files now have Bebas Neue font links")
    print("✅ Font will load from Google Fonts")

if __name__ == "__main__":
    add_bebas_font() 