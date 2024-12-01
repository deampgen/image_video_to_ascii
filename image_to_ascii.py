# Import necessary libraries
from PIL import Image
import cv2

# ASCII characters used to build the output text
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Resize image according to a new width

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65  # Adjust ratio for better aspect
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert pixels to a string of ASCII characters

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    return ascii_str

# Save ASCII art to a text file
def save_to_file(ascii_img, output_path):
    with open(output_path, 'w') as f:
        f.write(ascii_img)

# Main function to convert image to ASCII

def image_to_ascii(image_path, new_width=100):
    # Load image
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    # Convert image to ASCII
    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width

    ascii_str_len = len(ascii_str)
    ascii_img = ""

    # Split the string based on width of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    # Print result
    print(ascii_img)
    return ascii_img

# Function to convert video to ASCII

def video_to_ascii(video_path, new_width=100):
    # Open video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to PIL image
        frame_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Convert frame to ASCII
        ascii_art = image_to_ascii(frame_image, new_width)

        # Clear the console
        print("\033c", end="")

        # Print ASCII art
        print(ascii_art)

        # Wait for a short period to simulate video playback
        cv2.waitKey(50)

    cap.release()



output_path = r'C:\Users\deampgen\Desktop\projects\amina_ascii.txt'
ascii_art = image_to_ascii(r'C:\Users\deampgen\Desktop\amina.jpg')
save_to_file(ascii_art, output_path)

