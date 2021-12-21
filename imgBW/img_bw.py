from PIL import Image

try:
    img = Image.open('img.jpg')
    img_transform = img.convert('L')
    img_transform.save('img_BW.jpg')
except:
    print('Error!!')
print('Convert Succesfully!!')

