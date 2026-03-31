import cv2
import time
import os

# ==============================
# INITIAL SETUP
# ==============================

# Create folder to store captured images
output_folder = "captures"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Start webcam
cap = cv2.VideoCapture(0)

# Cooldown settings (seconds)
cooldown = 5
last_capture_time = 0

# Frame counter (for debugging / logs)
frame_count = 0

print("[INFO] System started. Monitoring for unauthorized access...")

# ==============================
# MAIN LOOP
# ==============================

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to access webcam.")
        break

    frame_count += 1

    # Convert to grayscale (required for detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Display number of detected faces
    cv2.putText(frame, f"Faces Detected: {len(faces)}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 2)

    # Process each detected face
    for (x, y, w, h) in faces:

        # Draw bounding box
        cv2.rectangle(frame,
                      (x, y),
                      (x + w, y + h),
                      (0, 0, 255), 2)

        # Label as "Unknown User"
        cv2.putText(frame,
                    "Unknown User",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255), 2)

        # Time-based capture logic
        current_time = time.time()

        if current_time - last_capture_time > cooldown:
            timestamp = int(current_time)

            filename = os.path.join(
                output_folder,
                f"intruder_{timestamp}.jpg"
            )

            # Save image
            cv2.imwrite(filename, frame)

            print(f"[ALERT] Intruder detected. Image saved: {filename}")

            last_capture_time = current_time

            # Display capture notification on screen
            cv2.putText(frame,
                        "CAPTURED",
                        (x, y + h + 25),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255), 2)

    # Show live feed
    cv2.imshow("Unauthorized Access Monitor", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        print("[INFO] Exiting system...")
        break

# ==============================
# CLEANUP
# ==============================

cap.release()
cv2.destroyAllWindows()