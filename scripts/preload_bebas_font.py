#!/usr/bin/env python3
"""
Preload Bebas Neue Font
Replace Google Fonts stylesheet link with preload+onload+noscript for Bebas Neue in all HTML files
"""
import os
import re

def preload_bebas_font():
    html_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    print("🚀 PRELOADING BEBAS NEUE FONT")
    print("=" * 50)
    preload_block = '''<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" onload="this.rel='stylesheet'">
<noscript>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
</noscript>'''
    for html_file in html_files:
        print(f"📄 Processing: {html_file}")
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        original_content = content
        # Remove old Bebas Neue stylesheet link
        content = re.sub(r'<link[^>]+href="https://fonts.googleapis.com/css2\?family=Bebas\+Neue&display=swap"[^>]*>', '', content)
        # Remove duplicate preconnects (optional, but safe)
        content = re.sub(r'<link rel="preconnect" href="https://fonts.googleapis.com"[^>]*>\s*', '', content)
        content = re.sub(r'<link rel="preconnect" href="https://fonts.gstatic.com"[^>]*>\s*', '', content)
        # Insert preload block after <head>
        content = re.sub(r'(<head[^>]*>)', r'\1\n' + preload_block, content)
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✅ Preload added: {html_file}")
        else:
            print(f"    ℹ️  No changes needed: {html_file}")
    print("\n🎯 BEBAS NEUE FONT PRELOAD COMPLETE!")
    print("✅ All HTML files now preload Bebas Neue font")

if __name__ == "__main__":
    preload_bebas_font()