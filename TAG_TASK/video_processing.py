import cv2  #OpenCV Library





cap = cv2.VideoCapture(0) # Open the webcam



if not cap.isOpened():   #Check if the webcam is not accessible
    print("Could not open webcam.")
    exit()

while True:  # Keep capturing frames continuously 

    

    ret, frame = cap.read() 

    if not ret:
        print("Failed to capture frame...")  #If frame not read properly, exit while loop
        break

    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert frame to grayscale
    blurred_frame = cv2.GaussianBlur(grayscale_frame, (3,3), 0)
    edge_frame = cv2.Canny(blurred_frame, 50, 150)



    cv2.imshow('Original webcam', frame)  #Display the normal live video
    cv2.imshow('Grayscale webcam', grayscale_frame) # Display the grayscale live video
    cv2.imshow('Blurred webcam', blurred_frame) # Display the blurred live video
    cv2.imshow('Edges webcam', edge_frame) # Display the detected edges



    if cv2.waitKey(1) == ord('q'):   

        break


cap.release()  # release the webcam
cv2.destroyAllWindows() # close windows

