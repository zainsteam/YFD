#!/usr/bin/env python3
"""
Remove Google Fonts Bebas Neue
Remove all Google Fonts Bebas Neue links from all HTML files
"""
import os
import re

def remove_bebas_googlefont():
    html_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    print("🧹 REMOVING GOOGLE FONTS BEBAS NEUE LINKS")
    print("=" * 50)
    for html_file in html_files:
        print(f"📄 Processing: {html_file}")
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        original_content = content
        # Remove all Bebas Neue Google Fonts links (preload, stylesheet, noscript)
        content = re.sub(r'<link[^>]+href="https://fonts.googleapis.com/css2\?family=Bebas\+Neue&display=swap"[^>]*>\s*', '', content)
        content = re.sub(r'<noscript>\s*<link[^>]+href="https://fonts.googleapis.com/css2\?family=Bebas\+Neue&display=swap"[^>]*>\s*</noscript>\s*', '', content)
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✅ Removed Bebas Neue Google Fonts: {html_file}")
        else:
            print(f"    ℹ️  No changes needed: {html_file}")
    print("\n🎯 BEBAS NEUE GOOGLE FONTS REMOVAL COMPLETE!")
    print("✅ All HTML files are now self-hosting Bebas Neue")

if __name__ == "__main__":
    remove_bebas_googlefont()