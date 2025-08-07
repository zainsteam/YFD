#!/usr/bin/env python3
"""
Update all HTML files to use Google Fonts CDN instead of local font files
"""

import os
import re
from pathlib import Path

def update_html_file(file_path):
    """Update a single HTML file to use Google Fonts CDN"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the old font preload links
        old_pattern = r'<link rel="preload" href="[^"]*fonts/[^"]*\.ttf" as="font" type="font/ttf" crossorigin>\s*<link rel="preload" href="[^"]*fonts/[^"]*\.ttf" as="font" type="font/ttf" crossorigin>'
        
        # New Google Fonts CDN links
        new_links = '''  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">'''
        
        # Replace the old links with new ones
        updated_content = re.sub(old_pattern, new_links, content)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Updated: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    print("🔄 UPDATING HTML FILES TO USE GOOGLE FONTS CDN")
    print("=" * 50)
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    # Skip the main index.html (already updated)
    html_files = [f for f in html_files if f != './index.html']
    
    updated_count = 0
    for file_path in html_files:
        if update_html_file(file_path):
            updated_count += 1
    
    print(f"\n🎯 UPDATE COMPLETE!")
    print(f"📊 Files updated: {updated_count}/{len(html_files)}")

if __name__ == "__main__":
    main() 