#!/bin/bash
#
# Image Optimization Script
# Resizes large images and converts to WebP for better performance.
#
# Requirements:
#   - ImageMagick (convert, identify commands)
#   - WebP tools (cwebp command)
#
# Usage:
#   ./scripts/optimize-images.sh              # Process all posts
#   ./scripts/optimize-images.sh --dry-run    # Show what would be done
#

set -e

MAX_WIDTH=1200
JPEG_QUALITY=85
WEBP_QUALITY=80
DRY_RUN=false

# Parse arguments
if [[ "$1" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "DRY RUN - No files will be modified"
    echo ""
fi

# Check dependencies
command -v identify >/dev/null 2>&1 || { echo "Error: ImageMagick is required. Install with: sudo apt install imagemagick"; exit 1; }
command -v convert >/dev/null 2>&1 || { echo "Error: ImageMagick is required. Install with: sudo apt install imagemagick"; exit 1; }
command -v cwebp >/dev/null 2>&1 || { echo "Error: WebP tools required. Install with: sudo apt install webp"; exit 1; }

# Find and process images
echo "Scanning for large images (>${MAX_WIDTH}px wide)..."
echo ""

OPTIMIZED=0
SKIPPED=0

# Process images in content/posts/
find content/posts -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) | while read -r img; do
    # Skip if it's a thumbnail or already processed
    if [[ "$img" == *"_thumb"* ]] || [[ "$img" == *"_optimized"* ]]; then
        continue
    fi

    # Get image width
    width=$(identify -format "%w" "$img" 2>/dev/null || echo "0")

    if [[ "$width" -gt "$MAX_WIDTH" ]]; then
        # Get file size in MB
        size_bytes=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null || echo "0")
        size_mb=$(echo "scale=2; $size_bytes / 1048576" | bc)

        echo "Found: $img"
        echo "  Current: ${width}px wide, ${size_mb}MB"

        if [[ "$DRY_RUN" == false ]]; then
            # Resize the image in place
            convert "$img" -resize "${MAX_WIDTH}x>" -quality "$JPEG_QUALITY" "$img"

            # Get new size
            new_size_bytes=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null || echo "0")
            new_size_mb=$(echo "scale=2; $new_size_bytes / 1048576" | bc)

            echo "  Resized: ${MAX_WIDTH}px wide, ${new_size_mb}MB"

            # Create WebP version if it doesn't exist
            webp_path="${img%.*}.webp"
            if [[ ! -f "$webp_path" ]]; then
                cwebp -q "$WEBP_QUALITY" "$img" -o "$webp_path" 2>/dev/null
                webp_size_bytes=$(stat -f%z "$webp_path" 2>/dev/null || stat -c%s "$webp_path" 2>/dev/null || echo "0")
                webp_size_kb=$(echo "scale=0; $webp_size_bytes / 1024" | bc)
                echo "  WebP: ${webp_size_kb}KB"
            fi
        else
            echo "  Would resize to ${MAX_WIDTH}px and create WebP"
        fi

        echo ""
        ((OPTIMIZED++)) || true
    else
        ((SKIPPED++)) || true
    fi
done

echo ""
echo "Done! Processed $OPTIMIZED images, skipped $SKIPPED already-optimized images."
