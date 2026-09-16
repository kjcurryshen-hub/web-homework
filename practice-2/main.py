import cv2

# read image
img = cv2.imread("hello.jpg")

# to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img.shape)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(img[i][j] < 50):
            print("o", end='')
        else:
            print(" ", end='')
        
    print()