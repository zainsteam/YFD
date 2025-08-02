#!/usr/bin/env python3
"""
CSS Minification Script
Quick CSS optimization for YFD website
"""

import re
from pathlib import Path

def minify_css(css_content):
    """Minify CSS content"""
    # Remove comments
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    
    # Remove unnecessary whitespace
    css_content = re.sub(r'\s+', ' ', css_content)
    css_content = re.sub(r'\s*{\s*', '{', css_content)
    css_content = re.sub(r'\s*}\s*', '}', css_content)
    css_content = re.sub(r'\s*:\s*', ':', css_content)
    css_content = re.sub(r'\s*;\s*', ';', css_content)
    css_content = re.sub(r'\s*,\s*', ',', css_content)
    
    # Remove trailing semicolons before closing braces
    css_content = re.sub(r';+}', '}', css_content)
    
    # Remove leading/trailing whitespace
    css_content = css_content.strip()
    
    return css_content

def update_html_files():
    """Update HTML files to use minified CSS"""
    html_files = list(Path(".").rglob("*.html"))
    updated_files = 0
    
    for html_file in html_files:
        if html_file.is_file():
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace CSS link
            if 'assets/css/main.css' in content:
                content = content.replace('assets/css/main.css', 'assets/css/main.min.css')
                
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated_files += 1
                print(f"Updated: {html_file.name}")
    
    return updated_files

def main():
    """Main CSS minification function"""
    print("🎨 CSS MINIFICATION")
    print("=" * 50)
    
    css_file = Path("assets/css/main.css")
    
    if not css_file.exists():
        print("❌ CSS file not found!")
        return
    
    # Read original CSS
    with open(css_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    original_size = len(original_content)
    print(f"Original CSS: {original_size:,} characters")
    
    # Minify CSS
    minified_content = minify_css(original_content)
    minified_size = len(minified_content)
    
    print(f"Minified CSS: {minified_size:,} characters")
    print(f"Reduction: {((original_size - minified_size) / original_size * 100):.1f}%")
    print(f"Bytes saved: {original_size - minified_size:,}")
    
    # Save minified version
    minified_file = Path("assets/css/main.min.css")
    with open(minified_file, 'w', encoding='utf-8') as f:
        f.write(minified_content)
    
    print(f"✅ Minified CSS saved to: {minified_file}")
    
    # Update HTML files
    print("\n📄 Updating HTML files...")
    updated_files = update_html_files()
    print(f"✅ Updated {updated_files} HTML files")
    
    print(f"\n🎯 CSS minification complete!")
    print(f"📊 Size reduction: {((original_size - minified_size) / original_size * 100):.1f}%")

if __name__ == "__main__":
    main() 