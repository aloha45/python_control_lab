from PIL import Image, ImageFilter

# grab the image

img = Image.open('./Images/luau.jpg')

print(img)

# take the grabbed image and blur it

filtered_img = img.filter(ImageFilter.BLUR)

# filtered_img.save('blur.png', 'png')

filtered_img = img.convert('L') #greyscale the image

# filtered_img.save('grey.png', 'png')

# filtered_img.show()

resize = filtered_img.resize((100, 100))

# resize.save('resize.png', 'png')

box = (100, 100, 400, 400)

cropped_region = filtered_img.crop(box)

# cropped_region.save('cropped.png', 'png')

# point transformation

transformed_img = img.point(lambda i: i * 2)

transformed_img.save('transformed.png', 'png')

img.close()
transformed_img.close()

