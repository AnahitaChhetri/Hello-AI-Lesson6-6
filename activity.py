import cv2
#importing cv2
photo=cv2.imread("dog.jpeg")
cv2.namedWindow('Dog Image', cv2.WINDOW_NORMAL)
#Resizing the window
cv2.resizeWindow('Dog Image', 800, 500)
cv2.imshow('Dog Image', photo)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"Image Dimensions:{photo.shape}")