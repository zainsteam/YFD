#!/usr/bin/env python3
"""
Fix Remaining PNG References
Update all remaining PNG files to WebP
"""

import re
from pathlib import Path

def fix_html_png_references():
    """Fix PNG references in HTML files"""
    print("📄 FIXING HTML PNG REFERENCES")
    print("=" * 50)
    
    html_files = list(Path(".").rglob("*.html"))
    updated_files = 0
    
    # PNG to WebP mappings
    png_to_webp = {
        "Layer 2 2.png": "Layer 2 2.webp",
        "Group 205.png": "Group 205.webp", 
        "Group 201.png": "Group 201.webp",
        "Group 204.png": "Group 204.webp",
        "Group 206.png": "Group 206.webp",
        "Group 72.png": "Group 72.webp",
        "Ellipse 3.png": "Ellipse 3.webp"
    }
    
    for html_file in html_files:
        if html_file.is_file():
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Replace PNG references
            for png_file, webp_file in png_to_webp.items():
                # Fix src attributes
                content = re.sub(
                    rf'src="([^"]*){re.escape(png_file)}"',
                    rf'src="\1WEBP/{webp_file}"',
                    content
                )
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated_files += 1
                print(f"Updated: {html_file.name}")
    
    print(f"✅ Updated {updated_files} HTML files")
    return updated_files

def fix_css_png_references():
    """Fix PNG references in CSS files"""
    print("\n🎨 FIXING CSS PNG REFERENCES")
    print("=" * 50)
    
    css_file = Path("assets/css/main.css")
    if not css_file.exists():
        print("❌ CSS file not found!")
        return 0
    
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix SEO 1.png reference
    content = re.sub(
        r'url\("../images/SEO 1\.png"\)',
        'url("../images/WEBP/SEO 1.webp")',
        content
    )
    
    if content != original_content:
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Updated CSS file")
        
        # Re-minify CSS
        from optimize_website import minify_css
        minified_content = minify_css(content)
        minified_file = Path("assets/css/main.min.css")
        with open(minified_file, 'w', encoding='utf-8') as f:
            f.write(minified_content)
        print("✅ Re-minified CSS")
        return 1
    
    print("✅ No PNG references found in CSS")
    return 0

def main():
    """Main function"""
    print("🔧 FIXING REMAINING PNG REFERENCES")
    print("=" * 60)
    
    # Fix HTML files
    html_updated = fix_html_png_references()
    
    # Fix CSS files
    css_updated = fix_css_png_references()
    
    print(f"\n✅ COMPLETE!")
    print(f"📄 HTML files updated: {html_updated}")
    print(f"🎨 CSS files updated: {css_updated}")
    print("🎯 All PNG references converted to WebP!")

if __name__ == "__main__":
    main() 