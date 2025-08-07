#!/usr/bin/env python3
"""
Fix font optimization in all HTML files by making dropdown menu selectors more specific
"""

import os
import re

def fix_font_optimization(file_path):
    """Fix font optimization in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the old dropdown menu selector
        old_pattern = r'\.dropdown-menu a \{'
        new_pattern = r'.desktop-nav .dropdown-menu a,\n    .mobile-nav .dropdown-menu a {'
        
        # Replace the old selector with the new specific selectors
        updated_content = re.sub(old_pattern, new_pattern, content)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Fixed font optimization in: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Main function to fix font optimization in all HTML files"""
    print("🔄 FIXING FONT OPTIMIZATION")
    print("=" * 50)
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    updated_count = 0
    for file_path in html_files:
        if fix_font_optimization(file_path):
            updated_count += 1
    
    print(f"\n🎯 FIX COMPLETE!")
    print(f"📊 Files updated: {updated_count}/{len(html_files)}")

if __name__ == "__main__":
    main() 