# Importing required libraries
import cv2

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

print("Press 'q' to quit.")

# Variable to track if a face was detected
face_detected = False

while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()
    
    # Check if the frame was successfully captured
    if not ret:
        print("Failed to capture video. Exiting...")
        break
    
    # Convert the frame to grayscale (required for face detection)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=6)
    
    # Check if faces are detected and update the status
    if len(faces) > 0:
        face_detected = True  # Set the flag to True if a face is detected
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the frame
    cv2.imshow("Face Detection", frame)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()

# Output the detection result to the terminal
if face_detected:
    print("A face was detected during the session.")
else:
    print("No face was detected during the session.")
