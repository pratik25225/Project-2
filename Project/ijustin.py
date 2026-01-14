import os
from PIL import Image

# Locate the first .jpg file in the current directory
current_dir = os.path.dirname(__file__)
image_file = next((f for f in os.listdir(current_dir) if f.endswith('.jpg')), None)
if not image_file:
    raise FileNotFoundError("No .jpg files found.")

# Load image
img = Image.open(os.path.join(current_dir, image_file))

# Convert to grayscale
img = img.convert("L")

# Resize for console output
# width, height = img.size
# img = img.resize((120, int(height * 120 / width)))  # Increase width for higher resolution
new_width = 120
new_height = int((img.height / img.width) * new_width * 0.42)
img = img.resize((new_width, new_height))


# Subtle ASCII characters from dark → light
ascii_chars = "@#*+=-:. "

pixels = img.getdata()

# Convert pixels to ASCII
ascii_image = ""

for i in range(len(pixels)):
    brightness = pixels[i]

    # Conditional mapping
    if brightness < 30:
        ascii_image += ascii_chars[0]
    elif brightness < 60:
        ascii_image += ascii_chars[1]
    elif brightness < 90:
        ascii_image += ascii_chars[2]
    elif brightness < 120:
        ascii_image += ascii_chars[3]
    elif brightness < 150:
        ascii_image += ascii_chars[4]
    elif brightness < 180:
        ascii_image += ascii_chars[5]
    elif brightness < 210:
        ascii_image += ascii_chars[6]
    else:
        ascii_image += ascii_chars[7]  # FIXED >240 case


    # New line after width
    if (i + 1) % 120 == 0:  # Match the new width
        ascii_image += "\n"

print(ascii_image)