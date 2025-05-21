#!/bin/bash

# Directory containing the images
IMAGE_DIR="./content/posts/volunteering_wildlife_rescue_centers/images/"

# Output directory for resized images
OUTPUT_DIR="./content/posts/volunteering_wildlife_rescue_centers/images2/"

# Check if the IMAGE_DIR exists
if [ ! -d "$IMAGE_DIR" ]; then
    echo "Error: The directory $IMAGE_DIR does not exist."
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through all jpg, webp, and png images in the directory
for img in "$IMAGE_DIR"/*.{jpg,jpeg,webp,png}; do
    # Check if the file exists to avoid errors
    if [ -e "$img" ]; then
        # Get the base name of the image
        base_name=$(basename "$img")

        # Resize the image and save it to the output directory
        convert "$img" -resize 800x "$OUTPUT_DIR/$base_name"

        echo "Resized $base_name and saved to $OUTPUT_DIR"
    fi
done

echo "All images have been resized."
