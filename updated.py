import cv2
import re
import os

# Function to sanitize text for use as filename
def sanitize_filename(text):
    # Remove any characters that are not allowed in filenames
    return re.sub(r'[^\w\-\.]', '_', text)

# Define the subdirectory name
subdirectory = "output_images"

# Open the CSV file
with open("list.csv") as file:
    for name in file:
        # Remove trailing newline character
        name = name.rstrip()

        # Read the image
        img = cv2.imread("2.png")

        # Define the text, font, size, and color
        text = name
        font = cv2.FONT_HERSHEY_COMPLEX
        font_scale = 3
        font_color = (255, 255, 255)  # white
        thickness = 10

        # Get the size of the text
        (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)

        # Calculate text position
        text_x = ((img.shape[1] - text_width) // 2)
        text_y = (img.shape[0] + (text_height )) // 2
        


        # Add the text to the image
        cv2.putText(img, text, (text_x, text_y), font, font_scale, font_color, thickness)
        text_y=text_x=0
        #text_x = ((img.shape[1] - (text_width)+220) // 2)
        print(text_x)
        text_y = (img.shape[0] + (text_height)+280 ) // 2
        cv2.putText(img, text, (450, text_y), font, 1, font_color, 2)
    
        # Generate filename based on text content
        filename = sanitize_filename(text)
        output_path = os.path.join(subdirectory, f"cert_{filename}.jpg")  # Output filename based on text
        output_path = output_path[:255]  # Limit filename length for compatibility

        # Ensure that the output subdirectory exists
        os.makedirs(subdirectory, exist_ok=True)

        # Save the modified image
        cv2.imwrite(output_path, img)
        print(f"Image with text '{text}' saved as '{output_path}'")
