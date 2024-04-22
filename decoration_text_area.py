import os
from PIL import Image

def decoration_textarea_image(file_path, index, replace_dict):
    # Open the GIF image
    gif_image = Image.open(file_path)

    # Convert to RGB format
    rgb_image = gif_image.convert('RGB')

    # Create a new blank image with the same size
    result_image = Image.new('RGB', rgb_image.size)

    # Process each pixel
    for x in range(rgb_image.width):
        for y in range(rgb_image.height):
            # Get the RGB value of the current pixel
            r, g, b = rgb_image.getpixel((x, y))

            # Check if the pixel needs to be replaced
            if (r, g, b) in replace_dict:
                result_image.putpixel((x, y), replace_dict[(r, g, b)])
            else:
                result_image.putpixel((x, y), (r, g, b))

    # Save the result image in PNG format with sequential names
    result_image.save(f"decoration_textarea_masks/{index:02d}.png")

# Define the colors to replace and their replacement colors
replace_dict = {
    (0, 0, 255): (255, 255, 0),
    (255, 0, 255): (255, 255, 0),
    (0, 255, 255): (255, 255, 0),
    (0, 255, 0): (255, 255, 0)
}

# Process each GIF image in the "ground_truth" folder
for index, file_name in enumerate(os.listdir("ground_truth")):
    if file_name.endswith(".gif"):
        decoration_textarea_image(os.path.join("ground_truth", file_name), index, replace_dict)

print("Color replacement complete.")
