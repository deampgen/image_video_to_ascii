# ASCII Art Generator

This project allows you to convert images and videos into ASCII art using Python. It provides functions to process images and frames, resize them, convert them to grayscale, and map their pixels to ASCII characters for a text-based visual representation.

## Features

- Convert images to ASCII art and save the result to a file.
- Generate ASCII art in real-time from videos.
- Adjustable ASCII output width for custom results.
- Compatible with `.jpg`, `.png`, and most common image/video formats.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/deampgen/image_video_to_ascii.git
   cd ascii-art-generator
   ```

2. Install dependencies:

   ```bash
   pip install pillow opencv-python
   ```

---

## Usage

### 1. Convert Image to ASCII

To convert an image to ASCII art:

```python
# Import the script
from ascii_art import image_to_ascii, save_to_file

# Define input and output paths
input_path = "path/to/your/image.jpg"
output_path = "path/to/save/ascii_art.txt"

# Convert image to ASCII
ascii_art = image_to_ascii(input_path, new_width=100)

# Save the ASCII art to a file
save_to_file(ascii_art, output_path)
```

### 2. Convert Video to ASCII

To process a video and display ASCII art frame-by-frame in the console:

```python
# Import the script
from ascii_art import video_to_ascii

# Define the video path
video_path = "path/to/your/video.mp4"

# Generate ASCII art from the video
video_to_ascii(video_path, new_width=100)
```

---

## How It Works

1. **Image Resizing**  
   The image is resized to maintain aspect ratio while reducing the resolution to fit the ASCII art format.

2. **Grayscale Conversion**  
   The resized image is converted to grayscale, simplifying pixel intensity values.

3. **Pixel Mapping to ASCII**  
   Pixel intensity values are mapped to a predefined set of ASCII characters, ranging from dense (`@`) to sparse (`.`).

4. **Text Output**  
   The ASCII art is either printed to the console, saved to a file, or both.

---

## Example

### Input Image
A sample image of dimensions 300x300.

### Output ASCII
```plaintext
@@@@@@@%%%??*+++++;;;;::
@@@@@%%%??*+++;;;;:::...
@@@@%%%%??*++;;;:::....
```

---

## Notes

- Video playback as ASCII is computationally intensive. Use smaller widths for smoother results.
- Modify the `ASCII_CHARS` array for custom character mappings.

---

## Contributing

Feel free to submit issues or contribute by opening pull requests. Make sure to follow the contribution guidelines.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
