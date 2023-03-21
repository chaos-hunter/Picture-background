from PIL import Image
from statistics import mode

while True:
    try:
        # Get the image path
        imagepath = input("Enter the path to the image file: ")
        # Open the image file
        image = Image.open(imagepath)
        break
    except FileNotFoundError:
        print("File not found. Please try again and enter a valid path.")

# Convert the image to RGB format
imagergb = image.convert("RGB")

# Get the dimensions of the image
width, height = image.size

# Prompt the user for a new background color
while True:
    colouroption = input("Enter the new background color (in RGB format, separated by commas): ")
    try:
        colour = tuple(map(int, colouroption.split(',')))
        break
    except ValueError:
        print("Invalid input. Please enter RGB values separated by commas.")

# Store the pixel values
pixel_values = []

# Loop through each pixel in the image and store its RGB values in the pixel_values list
for x in range(width):
    for y in range(height):
        r, g, b = imagergb.getpixel((x, y))
        pixel_values.append((r, g, b))

# Find the mode pixel value from the pixel_values list
mode_pixel = mode(pixel_values)

# Loop through each pixel in the image again
for x in range(width):
    for y in range(height):
        r, g, b = imagergb.getpixel((x, y))
        if (r, g, b) == mode_pixel:
            
            imagergb.putpixel((x, y), colour)

# Save the modified image to a file:
imagergb.save("new picture.jpg")
imagergb.show()
