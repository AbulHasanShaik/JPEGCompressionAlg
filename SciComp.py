from PIL import Image

def rgb_to_hsv(rgb):
    r, g, b = rgb
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    if delta == 0:
        h = 0
    elif cmax == r:
        h = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)

    if cmax == 0:
        s = 0
    else:
        s = delta / cmax

    v = cmax

    return h, s, v

def rgb_to_cmyk(rgb):
    r, g, b = rgb
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    k = 1 - max(r, g, b)
    if k == 1:
        c = m = y = 0
    else:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)

    return c, m, y, k

# Load the image
image_path = "C:\\Users\\shaik\\OneDrive\\School\\Scientific Comp\\Color Space Coversion\\230621042149-01-cristiano-ronaldo-euro-200-apps-062023-restricted.jpg"
image = Image.open(image_path)

# Convert image to RGB mode if not already in RGB
image_rgb = image.convert("RGB")

# Get pixel data
pixels = image_rgb.load()

# Example conversion for the first pixel
rgb_color = pixels[0, 0]
hsv_color = rgb_to_hsv(rgb_color)
print("RGB Color:", rgb_color)
print("HSV Color:", hsv_color)

# Example conversion for the first pixel
cmyk_color = rgb_to_cmyk(rgb_color)
print("CMYK Color:", cmyk_color)

# Convert each pixel to CMYK
for y in range(image_rgb.size[1]):
    for x in range(image_rgb.size[0]):
        r, g, b = image_rgb.getpixel((x, y))
        cmyk_color = rgb_to_cmyk((r, g, b))
        image_rgb.putpixel((x, y), tuple(int(value * 255) for value in cmyk_color))

# Convert the RGB image to CMYK
image_cmyk = image_rgb.convert("CMYK")

# Convert the RGB image to YCbCr
image_ycbcr = image_rgb.convert("YCbCr")

# Save the YCbCr image as JPEG
output_path = "output_image.jpg"
image_ycbcr.save(output_path, format='JPEG')

# Show the images
image.show()
image_ycbcr.show()
