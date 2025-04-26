import cv2
import numpy as np

def apply_filter(frame, filter_type):
    # Apply filter to the frame
    filter_frame = frame.copy()
    if filter_type == "red_tint":
        filter_frame[:, :, 0] = 0
        filter_frame[:, :, 1] = 0
    elif filter_type == "green_tint":
        filter_frame[:, :, 0] = 0
        filter_frame[:, :, 2] = 0
    elif filter_type == "blue_tint":
        filter_frame[:, :, 1] = 0
        filter_frame[:, :, 2] = 0
    elif filter_type == "sobel":
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobel_x = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(gray_frame, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined = cv2.bitwise_or((sobel_x).astype(np.uint8), (sobel_y).astype(np.uint8))
        filter_frame = cv2.cvtColor(sobel_combined, cv2.COLOR_GRAY2BGR)
    elif filter_type == "canny":
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_frame, 100, 200)
        filter_frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filter_frame

# Load Camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
else:
    filter_type = "original"
    print("Choose a filter type:")
    print("r for red tint")
    print("g for green tint")
    print("b for blue tint")
    print("s for sobel")
    print("c for canny")    
    print("q for quit")

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Apply filter to the frame
        filtered_frame = apply_filter(frame, filter_type)
        
        # Display the filtered frame
        cv2.imshow("Camera Filter", filtered_frame)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF

        # Map key press to filter type
        if key == 255:
            continue
        elif key == ord("r"):
            filter_type = "red_tint"
        elif key == ord("g"):
            filter_type = "green_tint"
        elif key == ord("b"):
            filter_type = "blue_tint"
        elif key == ord("s"):
            filter_type = "sobel"
        elif key == ord("c"):
            filter_type = "canny"
        elif key == ord("q"):
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")

cap.release()
cv2.destroyAllWindows()
# End of code