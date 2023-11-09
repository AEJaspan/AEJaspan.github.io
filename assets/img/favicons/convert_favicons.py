from PIL import Image

# Define paths for the images
original_image_path = 'favicon.png'
favicon_32_path = 'favicon_32x32.png'
favicon_16_path = 'favicon_16x16.png'
favicon_ico_path = 'favicon.ico'

# Open the original image
with Image.open(original_image_path) as image:
    # Create 32x32 PNG
    favicon_32 = image.resize((32, 32), Image.ANTIALIAS)
    favicon_32.save(favicon_32_path)

    # Create 16x16 PNG
    favicon_16 = image.resize((16, 16), Image.ANTIALIAS)
    favicon_16.save(favicon_16_path)

    # Create favicon ICO
    image.save(favicon_ico_path, format='ICO', sizes=[(32, 32), (16, 16)])

(favicon_32_path, favicon_16_path, favicon_ico_path)
