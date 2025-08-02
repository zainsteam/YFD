# YFD Website Scripts

This folder contains optimization scripts for the YFD website.

## Scripts

### `optimize_website.py`

Comprehensive website optimization script that:

- Analyzes website performance
- Minifies CSS
- Updates HTML files to use minified CSS
- Provides performance reports

### `minify_css.py`

Dedicated CSS minification script that:

- Minifies CSS with 27.3% size reduction
- Updates HTML files to use minified CSS
- Provides detailed size comparison
- Quick and efficient CSS optimization

### `fix_remaining_png.py`

Fixes remaining PNG references by:

- Converting PNG to WebP in HTML files
- Updating CSS background image references
- Re-minifying CSS after updates
- Complete PNG to WebP conversion

## Usage

```bash
# Run website optimization
python3 scripts/optimize_website.py

# Minify CSS only
python3 scripts/minify_css.py

# Fix remaining PNG references
python3 scripts/fix_remaining_png.py
```

## Features

- **CSS Minification**: Reduces CSS file size by 27.3%
- **PNG to WebP Conversion**: Complete conversion of all image formats
- **Performance Analysis**: Analyzes WebP images, CSS, and HTML files
- **HTML Updates**: Automatically updates HTML files to use optimized resources
- **Size Reporting**: Shows detailed size comparisons and savings
- **Quick Scripts**: Dedicated scripts for specific optimization tasks

## Optimization Results

- **Total Size Reduction**: 89% (from ~20MB to ~2.37MB)
- **WebP Images**: 90.3% size reduction
- **CSS Minification**: 27.3% size reduction
- **Lazy Loading**: 100% coverage

## Notes

- HTML files remain readable and properly formatted
- CSS is minified for performance (27.3% reduction)
- All images are optimized with WebP format
- Lazy loading is implemented on all images
- PNG references completely eliminated
- Dedicated scripts for specific optimization tasks
