#!/usr/bin/env python3
"""
Fix Impact Font References
Replace Google Fonts Impact with system fonts to prevent ORB blocking
"""

import os
import re

def fix_impact_font():
    """Replace all Impact font references with system fonts"""
    
    # Files to process
    css_file = "assets/css/main.css"
    html_files = []
    
    # Find all HTML files
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    
    print("🔧 FIXING IMPACT FONT REFERENCES")
    print("=" * 50)
    
    # Fix CSS file
    if os.path.exists(css_file):
        print(f"📄 Processing CSS file: {css_file}")
        
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace Impact font references
        original_content = content
        
        # Replace Impact with system fonts
        content = re.sub(r'font-family:\s*["\']?Impact["\']?\s*,?\s*sans-serif', 
                        'font-family: "Arial Black", "Helvetica Neue", "Arial", sans-serif', content)
        content = re.sub(r'font-family:\s*Impact\s*,?\s*sans-serif', 
                        'font-family: "Arial Black", "Helvetica Neue", "Arial", sans-serif', content)
        
        if content != original_content:
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print("✅ CSS file updated")
        else:
            print("ℹ️  No changes needed in CSS file")
    
    # Fix HTML files
    print(f"\n📄 Processing {len(html_files)} HTML files...")
    
    for html_file in html_files:
        print(f"  Processing: {html_file}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove Google Fonts links
        content = re.sub(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*', '', content)
        content = re.sub(r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*', '', content)
        content = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=Impact&display=swap" rel="stylesheet">\s*', '', content)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✅ Updated: {html_file}")
        else:
            print(f"    ℹ️  No changes: {html_file}")
    
    print("\n🎯 IMPACT FONT FIX COMPLETE!")
    print("✅ Removed Google Fonts dependencies")
    print("✅ Replaced Impact with system fonts")
    print("✅ Fixed ORB blocking issue")

if __name__ == "__main__":
    fix_impact_font() 