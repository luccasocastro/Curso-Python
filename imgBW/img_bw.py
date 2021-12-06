from PIL import Image

img = Image.open('img_teste.jpg')
img_transform = img.convert('L')
img_transform.save('img_teste_BW.jpg')
