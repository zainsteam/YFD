#!/usr/bin/env python3
"""
Add font loading optimization to all HTML files
"""

import os
import re

def add_font_optimization(file_path):
    """Add font loading optimization to a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the Google Fonts link
        font_link_pattern = r'(<link href="https://fonts\.googleapis\.com/css2\?family=Bebas\+Neue&family=Poppins:wght@300;400;500;600;700&display=swap"\s+rel="stylesheet">)'
        
        # Font optimization styles
        optimization_styles = '''  <style>
    /* Font loading optimization */
    .desktop-nav .nav-links a,
    .mobile-nav .nav-links a {
      font-family: "Bebas Neue", Arial, sans-serif !important;
      font-display: swap;
    }
    .dropdown-menu a {
      font-family: "Poppins", Arial, sans-serif !important;
      font-display: swap;
    }
  </style>'''
        
        # Replace the font link with font link + optimization styles
        updated_content = re.sub(font_link_pattern, r'\1' + optimization_styles, content)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Added font optimization to: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Main function to add font optimization to all HTML files"""
    print("🔄 ADDING FONT LOADING OPTIMIZATION")
    print("=" * 50)
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    updated_count = 0
    for file_path in html_files:
        if add_font_optimization(file_path):
            updated_count += 1
    
    print(f"\n🎯 OPTIMIZATION COMPLETE!")
    print(f"📊 Files updated: {updated_count}/{len(html_files)}")

if __name__ == "__main__":
    main() 