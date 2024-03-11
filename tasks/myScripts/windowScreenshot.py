from PIL import Image, ImageGrab
import os
import datetime

# Specify the path of the image to open
image_path = r'D:\softwares\image.jpg'

# Check if the image exists
if os.path.exists(image_path):
    # Specify the directory to save the screenshot
    save_directory = r'D:\screenshots'

    # Ensure that the save directory exists
    os.makedirs(save_directory, exist_ok=True)

    # Open the image using the Image module
    image = Image.open(image_path)

    # Take a screenshot of the entire screen
    screenshot = ImageGrab.grab()

    # Generate a timestamp for the screenshot filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Specify the path to save the screenshot
    screenshot_path = os.path.join(save_directory, f'screenshot_{timestamp}.png')

    # Save the screenshot to the specified location
    screenshot.save(screenshot_path)

    # Close the opened image
    image.close()

    print("Screenshot saved successfully at:", screenshot_path)
else:
    print("The specified image file does not exist.")
