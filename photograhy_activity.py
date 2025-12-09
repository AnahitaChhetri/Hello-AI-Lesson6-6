import cv2
import matplotlib.pyplot as plot

image=cv2.imread("dog.jpeg")
img=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def cropping():
    cropped_image=img[1000:2000,2300:3200]
    plot.imshow(cropped_image)
    plot.show()
    save(cropped_image)

def brightening():
    contrast=1
    brightness=2
    brightened_img=cv2.convertScaleAbs(img,contrast,brightness)
    plot.imshow(brightened_img)
    plot.show()
    save(brightened_img)

def rotation():
    width,height=img.shape[:2]
    center= (width//2, height//2)
    angle=90
    scale=1
    matrix_rotation=cv2.getRotationMatrix2D(center, angle, scale)
    rotated_image=cv2.warpAffine(img, matrix_rotation, (width, height))
    plot.imshow(rotated_image)
    plot.show()
    save(rotated_image)

def save(image_type):
    cv2.waitKey(0)
    save=input("Press 's' if you would like to save the image (as shih_tzu.png). Otherwise, press any other letter. : ").lower()
    if save=="s":
        cv2.imwrite("shih_tzu.png", cv2.cvtColor(image_type, cv2.COLOR_BGR2RGB))
    else:
        print("Image not saved.")
    

print("Welcome to the photography editor! I have 3 tools-brightening, resizing to the face, and rotating the image!")
print("Press S to save each of the images")
plot.imshow(img)
plot.show()

cropping()
brightening()
rotation()
cv2.destroyAllWindows()
