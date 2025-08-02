#!/usr/bin/env python3
"""
Website Optimization Script
Comprehensive optimization for YFD website
"""

import os
import re
from pathlib import Path

def get_file_size(file_path):
    """Get file size in KB"""
    try:
        size = os.path.getsize(file_path)
        return size / 1024  # Convert to KB
    except:
        return 0

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

def analyze_website():
    """Analyze website performance"""
    print("📊 WEBSITE PERFORMANCE ANALYSIS")
    print("=" * 50)
    
    # Analyze WebP images
    webp_size = 0
    webp_count = 0
    webp_dir = Path("assets/images/WEBP")
    if webp_dir.exists():
        for webp_file in webp_dir.glob("*.webp"):
            webp_size += get_file_size(webp_file)
            webp_count += 1
    
    # Analyze CSS
    css_original = get_file_size("assets/css/main.css")
    css_minified = get_file_size("assets/css/main.min.css")
    
    # Analyze HTML files
    html_files = list(Path(".").rglob("*.html"))
    total_html_size = 0
    for html_file in html_files:
        if html_file.is_file():
            total_html_size += get_file_size(html_file)
    
    print(f"🖼️  Images: {webp_count} WebP files, {webp_size:.1f} KB")
    print(f"🎨 CSS: Original {css_original:.1f} KB, Minified {css_minified:.1f} KB")
    print(f"📄 HTML: {len(html_files)} files, {total_html_size:.1f} KB")
    print(f"📊 Total Size: {webp_size + css_minified + total_html_size:.1f} KB")
    
    return webp_size, css_minified, total_html_size

def optimize_css():
    """Optimize CSS"""
    print("\n🎨 CSS OPTIMIZATION")
    print("=" * 50)
    
    css_file = Path("assets/css/main.css")
    if not css_file.exists():
        print("❌ CSS file not found!")
        return False
    
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
    
    # Save minified version
    minified_file = Path("assets/css/main.min.css")
    with open(minified_file, 'w', encoding='utf-8') as f:
        f.write(minified_content)
    
    print(f"✅ Minified CSS saved to: {minified_file}")
    return True

def update_html_to_minified_css():
    """Update HTML files to use minified CSS"""
    print("\n📄 UPDATING HTML FILES")
    print("=" * 50)
    
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
    
    print(f"✅ Updated {updated_files} HTML files")
    return updated_files

def main():
    """Main optimization function"""
    print("🚀 YFD WEBSITE OPTIMIZATION")
    print("=" * 60)
    
    # Analyze current state
    webp_size, css_minified, html_size = analyze_website()
    
    # Optimize CSS
    if optimize_css():
        # Update HTML files
        updated_files = update_html_to_minified_css()
        
        print(f"\n✅ OPTIMIZATION COMPLETE!")
        print(f"📊 Total optimized size: {webp_size + css_minified + html_size:.1f} KB")
        print(f"📄 HTML files updated: {updated_files}")
        print("🎯 Website is optimized and ready!")
    else:
        print("❌ Optimization failed!")

if __name__ == "__main__":
    main() 