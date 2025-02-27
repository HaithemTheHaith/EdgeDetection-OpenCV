import cv2 #OpenCV library
 


image = cv2.imread('test_image.jpg') 





if image is None:                   
    print("Error: Image not found.")

else:

    
    cv2.imshow('Original Image', image) # Display the original image



    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Converts the color image to grayscale

    cv2.imshow('Grayscale image', grayscale_image)   # Display grayscale image on a seperate pop-up window

    cv2.imwrite('grayscale_image.jpg', grayscale_image) # Write the grayscale image into the local directory





    blurred_image = cv2.GaussianBlur(grayscale_image, (3,3), 0)  #Apply gaussian blur 

    cv2.imshow('Blurred image', blurred_image)  # Display blurred image on seperate pop-up window

    cv2.imwrite('blurred_image.jpg', blurred_image) # Write the blurred image into the local directory



    edges = cv2.Canny(blurred_image, 50, 150)   # Perform canny edge detection

    cv2.imshow('Canny Edge Detection', edges) # Display the edge detected image in a seperate pop-up window 

    cv2.imwrite('edge_detected_image.jpg', edges) # Write the edge detected image into the local directory



    cv2.waitKey(0)  # Wait for any key press to close the window

    cv2.destroyAllWindows() # Close all windows 

