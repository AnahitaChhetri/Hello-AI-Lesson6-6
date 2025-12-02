import cv2

# Importing OpenCV, which allows your computer to proccess images, and supports image visualisation.
photo=cv2.imread("dog.jpeg")


def save(image_obj):
    key=cv2.waitKey(1)

    user_save=input("Do you want to save the image? Press 'yes' to save: ").lower()
    if user_save=="yes":
        cv2.imwrite("dog.png", image_obj)
        print("Image saved as 'dog.png'.")
    else:
        print("Image not saved.")
    

# Ask user the size
user_size=input("What size of photo do you like? S, M, or L? Please put the letter. (small, medium, or large): ").lower()


# Based on size, call correct resize and show image
if user_size=="s":
    # Depending on the user's choice, they are shown different images of the dog.
    # resize function accepts location of photo and size (width, height)
    image_obj=cv2.resize(photo, (300,200))
    cv2.imshow("Small_Dog", image_obj)
elif user_size=="m":
    image_obj=cv2.resize(photo,(500,400))
    cv2.imshow("Medium_Dog",image_obj)
else:
    image_obj=cv2.resize(photo, (700,600))
    cv2.imshow("Large Dog", image_obj)

# wait for a milisecond before calling save function
cv2.waitKey(1)
save(image_obj)

# close all windows
cv2.destroyAllWindows()