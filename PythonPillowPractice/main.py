import PIL.Image
from PIL import Image
from PIL import ImageFile
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw

"""
im=Image.open(r"C:\sers\kaaan\Desktop\Pillow projem\astronot1.jpg")
print(im.format,im.size,im.mode)

r,g,b=im.split()
im=Image.merge("RGB",(b,g,r))
im.show()

simdikiAci=im.rotate(45)
simdikiAci.show()

with Image.open(r"C:\sers\kaaan\Desktop\Pillow projem\stokfoto_4.jpg") as im:
    im=im.convert("L")
im.show()

cikti=im.filter(ImageFilter.DETAIL)
cikti=im.point(lambda i:i*1.2)
cikti.show()



enh=ImageEnhance.Contrast(im)
enh.enhance(0.3).show("%30 more contrast")

with Image.open(r"C:\sers\kaaan\Desktop\Pillow projem\punisher.gif") as im:
    im.seek(1)

    try:
        while 1:
            im.seek(im.tell()+1)
    except EOFError:
        pass
    im.show()


#GEEK FOR GEEKS'den başladim
img=Image.open(r"C:\sers\kaaan\Desktop\Pillow projem\stokfoto_2.jpg")
print(img.mode)
img=img.rotate(90,PIL.Image.NEAREST,expand=1)
img.show()

img=Image.open(r"C:\sers\kaaan\Desktop\Pillow projem\stokfoto_3.jpg")
dikey_img=img.transpose(method=Image.FLIP_TOP_BOTTOM)
dikey_img.show()

img=Image.open(r"C:\sers\kaaan\Desktop\Pillow projem\stokfoto5_.jpg")
width,height=img.size
left=4
top=height/5
right=154
bottom=3*height/5
img1=img.crop((left,top,right,bottom))
newsize=(1920,1080)
img1=img.resize(newsize)
img1.show()


from PIL import Image
def tnails():
   try:
      image = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat.jpg')
      image.thumbnail((90,90))
      image.save(r'C:\sers\kaaan\Desktop\Pillow projem\thumbnail.jpg')
      image1 = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\thumbnail.jpg')
      image1.show()
   except IOError:
      pass
tnails()




# pass the image as command line argument

img = Image.open(r"C:\sers\kaaan\Desktop\Pillow projem\python1.png")

# resize the image
width, height = img.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.26
img = img.resize((new_width, int(new_height)))
# new size of image
# print(img.size)

# convert image to greyscale format
img = img.convert('L')

pixels = img.getdata()

# replace each pixel with a character from array
chars = ["|","S","#","&","@","$","%","*","B",":","."]
new_pixels = [chars[pixel//24] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

# write to a text file.
with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)




img = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\denemeGeek.png')
rgba = img.convert("RGBA")
datas = rgba.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 0:  # finding yellow colour
        # replacing it with a transparent value
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

rgba.putdata(newData)
rgba.save("transparent_image.png", "PNG")

from PIL import Image

img = Image.open('image.png')
rgba = img.convert("RGBA")
datas = rgba.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 0:  # finding yellow colour
        # replacing it with a transparent value
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

rgba.putdata(newData)
rgba.save("transparent_image.png", "PNG")


"""

"""
im = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')

im1 = im.filter(ImageFilter.BLUR)
im1.save(r"C:\sers\kaaan\Desktop\Pillow projem\kedi_Blur.png")
im1.show()

im2 = im.filter(ImageFilter.MinFilter(5))
im2.show()

im3 = im.filter(ImageFilter.MinFilter) # same as MinFilter(3)
im3.show()

im4=im.filter(ImageFilter.CONTOUR)
im4.save(r"C:\sers\kaaan\Desktop\Pillow projem\kedi_Contour.png")
im4.show()

im5=im.filter(ImageFilter.DETAIL)
im5.save(r"C:\sers\kaaan\Desktop\Pillow projem\kedi_Detail.png")
im5.show()

im6=im.filter(ImageFilter.EDGE_ENHANCE)
im6.save(r"C:\sers\kaaan\Desktop\Pillow projem\kedi_EDGE_ENHANCE.png")
im6.show()

im7=im.filter(ImageFilter.EDGE_ENHANCE_MORE)
im7.save(r"C:\sers\kaaan\Desktop\Pillow projem\kedi_EDGE_ENHANCE_MORE.png")
im7.show()


im8=im.filter(ImageFilter.EMBOSS)
im8.save(r"C:\sers\kaaan\Desktop\Pillow projem\kedi_EMBOSS.png")
im8.show()


def tnails():
    try:
        image=Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')
        image.thumbnail((90,90))
        image.save(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_thumbnail.jpeg')
        image1=Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_thumbnail.jpeg')
        image1.show()
    except IOError:
        pass
tnails()


img = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')
rgba = img.convert("RGBA")
datas = rgba.getdata()

newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
        # storing a transparent value when we find a black colour
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)  # other colours remain unchanged

rgba.putdata(newData)
rgba.save(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_AlphaKanallı.jpeg', "PNG")


im2 = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')
kutu=(200,200,600,600)
kesilmis=im2.crop(kutu)
kesilmis.show()

# Importing the PIL library

from PIL import ImageDraw

# Open an Image
img = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Add Text to an image
I1.text((1000,1000),"Bu bir kedi",fill=(255,200,200))

# Display edited image
img.show()

# Save the edited image

img.save(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_Yazı_Yazıldı.jpeg')


# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\denemeGeek.png')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size


# Add Text to an image
I1.text((10, 10), "Nice Car", font="Calibri", fill=(255, 0, 0))

# Display edited image
img.show()

# Save the edited image
img.save(r'C:\sers\kaaan\Desktop\Pillow projem\denemeGeek_Yazili.png')


img = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')
a=img.resize((300,300))
b=a.transpose(Image.FLIP_LEFT_RIGHT)
b.save(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_DöndürmeKırpma.jpeg')
b.show()


resim=Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_Blur.png')
resimkeskin=ImageEnhance.Sharpness(resim)
resimkeskin.enhance(4.0).show()
resim.save(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_Kekinleştirilmiş.jpeg')


resim=Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')
b,g,r=resim.split()
resim=Image.merge("RGB",(r,g,b))
resim.show()
resim.save(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_Split.jpeg')

resim=Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')
resim2=Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')
a=resim2.resize((300,300))
rgba = a.convert("RGBA")
resim.paste(rgba,(0,0),mask=rgba)
resim.show()
resim.save(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_ustResim.jpeg')


img = Image.open(r'C:\sers\kaaan\Desktop\Pillow projem\cat_2.jpeg')
# Creating a Draw object
draw = ImageDraw.Draw(img)
# Drawing a green rectangle
# in the middle of the image
draw.rectangle(xy=(300, 300, 500, 500),
               fill=(0, 206, 200),
               outline=(224,171,249),
               width=20)
# Method to display the modified image
img.show()
img.save(r'C:\sers\kaaan\Desktop\Pillow projem\kedi_kare.jpeg')
"""

#https://stackoverflow.com/questions/71851406/how-to-convert-pngs-to-gif-with-very-short-delay-in-python
dosya=[Image.open(r'C:\Users\kaaan\Desktop\Pillow projem\cat_2.jpeg'),Image.open(r'C:\Users\kaaan\Desktop\Pillow projem\kedi_AlphaKanallı.jpeg'),Image.open(r'C:\Users\kaaan\Desktop\Pillow projem\kedi_Blur.png'),Image.open(r'C:\Users\kaaan\Desktop\Pillow projem\kedi_Detail.png'),Image.open(r'C:\Users\kaaan\Desktop\Pillow projem\kedi_EDGE_ENHANCE.png'),Image.open(r'C:\Users\kaaan\Desktop\Pillow projem\kedi_EDGE_ENHANCE_MORE.png'),Image.open(r'C:\Users\kaaan\Desktop\Pillow projem\kedi_Kekinleştirilmiş.jpeg'),Image.open(r'C:\Users\kaaan\Desktop\Pillow projem\kedi_Split.jpeg')]
dosya[0].save(r'C:\Users\kaaan\Desktop\Pillow projem\test.gif',format='GIF',append_images=dosya[1:],save_all=True,cikar=2,duration=10,loop=0,transparency=0)











