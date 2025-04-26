import cv2
import numpy as np

def apply_filter(image, filter_type):
    #Apply image to filter image
    filter_image= image.copy()
    if filter_type=="red_tint":
        filter_image[:, :, 0]= 0
        filter_image[:, :, 1]= 0
    elif filter_type=="green_tint":
        filter_image[:, :, 0]= 0
        filter_image[:, :, 2]= 0
    elif filter_type=="blue_tint":
        filter_image[:, :, 1]= 0
        filter_image[:, :, 2]= 0
    elif filter_type=="sobel":
        gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobel_x= cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y= cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined= cv2.bitwise_or((sobel_x).astype(np.uint8), (sobel_y).astype(np.uint8))
        filter_image= cv2.cvtColor(sobel_combined, cv2.COLOR_GRAY2BGR)
    elif filter_type=="canny":
        gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges= cv2.Canny(gray_image, 100, 200)
        filter_image= cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filter_image

#Load image
image_path= "image.jpg"
image= cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
    exit()
else:
    filter_type= "original"
    print("Choose a filter type:")
    print("r for red tint")
    print("g for green tint")
    print("b for blue tint")
    print("s for sobel")
    print("c for canny")    
    print("q for quit")

    while True:
        #Apply filter to image
        filtered_image= apply_filter(image, filter_type)
        
        #Display filtered image
        cv2.imshow("Filtered Image", filtered_image)

        #Wait for key press
        key= cv2.waitKey(0) & 0xFF

        #Map key press to filter type
        if key== ord("r"):
            filter_type= "red_tint"
        elif key== ord("g"):
            filter_type= "green_tint"
        elif key== ord("b"):
            filter_type= "blue_tint"
        elif key== ord("s"):
            filter_type= "sobel"
        elif key== ord("c"):
            filter_type= "canny"
        elif key== ord("q"):
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")

cv2.destroyAllWindows()
#End of code