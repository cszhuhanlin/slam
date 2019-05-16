import cv2


image1=cv2.imread('../../../data/rgbd_dataset_freiburg3_walking_xyz/rgb/1341846337.150037.png')
#(left, top), (right, bottom)244.0,85.0,454.0,460.0
cv2.rectangle(image1, (429,213),(640,479), (0, 255, 0), 1)
cv2.rectangle(image1, (244,85),(454,460 ), (0, 255, 0), 1)
cv2.imwrite('1341846337.150037.png',image1)




'''from PIL import Image,ImageDraw

left, top, right, bottom=0,42,113,460
image_path = '../../../data/rgbd_dataset_freiburg3_walking_xyz/rgb/1341846332.086502.png'
image = Image.open(image_path)
#创建一个可以在给定图像上绘图的对象
draw = ImageDraw.Draw(image)

draw.polygon([(left,top),(right,top),(left,bottom),(right,bottom)], outline=(255,0,0))
image.show()'''
