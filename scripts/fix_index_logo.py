#!/usr/bin/env python3
"""
Fix Index Logo
Fix the missing image in index.html logo link
"""

def fix_index_logo():
    """Fix the missing image in index.html logo"""
    
    with open("index.html", 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the empty logo link with proper structure
    old_pattern = r'<div class="logo">\s*<a href="index\.html"></a>\s*</div>'
    new_pattern = '''      <div class="logo">
        <a href="index.html">
          <img src="assets/images/WEBP/group 163.webp" alt="Logo" / loading="lazy">
        </a>
      </div>'''
    
    content = content.replace(old_pattern, new_pattern)
    
    with open("index.html", 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Fixed index.html logo - added missing image")

if __name__ == "__main__":
    fix_index_logo() 