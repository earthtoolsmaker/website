#!/bin/bash
#
# Install git hooks for this repository
#

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

echo "Installing git hooks..."

# Create pre-commit hook
cat > "$HOOKS_DIR/pre-commit" << 'EOF'
#!/bin/bash
#
# Pre-commit hook for image optimization
# Runs the optimize-images.sh script before each commit
#

# Only process if there are staged image files in content/posts/
STAGED_IMAGES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(jpg|jpeg|png)$' | grep -E '^content/posts/')

if [ -z "$STAGED_IMAGES" ]; then
    exit 0
fi

echo "Running image optimization..."

# Run the optimization script
if [ -x "./scripts/optimize-images.sh" ]; then
    ./scripts/optimize-images.sh

    # Re-add any modified images to staging
    for img in $STAGED_IMAGES; do
        if [ -f "$img" ]; then
            git add "$img"
            # Also add WebP version if created
            webp="${img%.*}.webp"
            if [ -f "$webp" ]; then
                git add "$webp"
            fi
        fi
    done
else
    echo "Warning: scripts/optimize-images.sh not found or not executable"
fi

exit 0
EOF

chmod +x "$HOOKS_DIR/pre-commit"

echo "Done! Pre-commit hook installed."
echo ""
echo "The hook will automatically optimize large images in content/posts/"
echo "before each commit using scripts/optimize-images.sh"
