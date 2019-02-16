import PIL.Image
img = PIL.Image.open('./media/image/photo.jpg')
exif_data = img._getexif()

print(exif_data) # Renverra None si aucune métadata


