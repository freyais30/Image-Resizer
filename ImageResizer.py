from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    # Open the image
    with Image.open(input_path) as image:
        # Resize the image
        image = image.resize((new_width, new_height))
        # Save the resized image
        image.save(output_path)

# Get input from the user
input_path = input("Enter the path to the image file: ")
new_width = int(input("Enter the new width: "))
new_height = int(input("Enter the new height: "))
output_path = input("Enter the path to save the resized image: ")

# Resize the image
resize_image(input_path, output_path, new_width, new_height)
