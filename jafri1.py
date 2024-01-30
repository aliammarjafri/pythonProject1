import cv2 as opencv

image = opencv.imread("C:\\Users\Admin\\Desktop\\New folder (3)\\lenna.png")
print("Resolution : ", image.shape, type(image))


gray_image = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)

print("Resolution : ", gray_image.shape)

opencv.imshow("Input Image", image)
opencv.imshow("output Image", gray_image)

opencv.waitKey(0)


