import cv2
photo=cv2.imread("dog.jpeg")
grey_dog=cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
resized=cv2.resize(grey_dog, (600, 400))
cv2.imshow("Grey Dog", resized)
key=cv2.waitKey(0)
if key==ord("s"):
    cv2.imwrite("grayscale_dog.png", resized)
    print("Image saved as 'grayscale_dog.png'.")
else:
    print("Image not saved.")

cv2.destroyAllWindows()
