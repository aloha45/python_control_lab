from PIL import Image, ImageFilter, ImageGrab

img = Image.open('./Images/jt.jpg')

# img = Image.close()

# img.show()

img.thumbnail((300, 100))

# img.save('thumbnail.jpg')

screen = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=False, xdisplay=None)

# screen.show()

radius, diameter = 20, 40

background_size = (img.size[0] + diameter, img.size[1] + diameter)
background = Image.new('RGB', background_size, (255, 255, 255))
background.paste(img, (radius, radius))

mask_size = (img.size[0] + diameter, img.size[1] + diameter)
mask = Image.new('L', mask_size, 255)
black_size = (img.size[0] - diameter, img.size[1] - diameter)
black = Image.new('L', black_size, 0)

mask.paste(black, (diameter, diameter))

blur = background.filter(ImageFilter.GaussianBlur(radius / 2))
background.paste(blur, mask=mask)

background.save('test-background.jpg', quality=100)

background.show()

img.close()

screen.close()

background.close()