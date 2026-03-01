import cv2
import time
from ultralytics import YOLO

# ===============================
# LOAD YOLO MODEL
# ===============================
model = YOLO("yolov8n.pt")

# Vehicle class IDs (COCO dataset)
VEHICLE_CLASSES = [2, 3, 5, 7]  # car, motorcycle, bus, truck

# ===============================
# CONGESTION CLASSIFIER
# ===============================
def classify_congestion(vehicle_count):
    if vehicle_count <= 5:
        return "LOW", 20
    elif vehicle_count <= 15:
        return "MEDIUM", 40
    else:
        return "HIGH", 60


# ===============================
# USE DOWNLOADED VIDEO FILE
# ===============================
cap = cv2.VideoCapture("traffic.mp4")

if not cap.isOpened():
    print("❌ Error: Could not open video file.")
    exit()

print("🚦 Smart Traffic System Started...")
print("Press Q to exit")

while True:
    start_time = time.time()

    ret, frame = cap.read()

    # If video ends, restart from beginning
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Run YOLO detection
    results = model(frame, conf=0.4, verbose=False)

    vehicle_count = 0

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])

            if cls_id in VEHICLE_CLASSES:
                vehicle_count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = model.names[cls_id]

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0), 2)

    # Classify congestion
    level, green_time = classify_congestion(vehicle_count)

    # Choose color based on congestion
    if level == "LOW":
        color = (0, 255, 0)
    elif level == "MEDIUM":
        color = (0, 165, 255)
    else:
        color = (0, 0, 255)

    # Draw traffic light circle
    cv2.circle(frame, (600, 100), 30, color, -1)

    # FPS calculation
    fps = 1 / (time.time() - start_time)

    # Display Info
    cv2.putText(frame, f"Vehicles: {vehicle_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2)

    cv2.putText(frame, f"Congestion: {level}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, color, 2)

    cv2.putText(frame, f"Green Signal Time: {green_time} sec",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 0), 2)

    cv2.putText(frame, f"FPS: {int(fps)}",
                (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (200, 200, 200), 2)

    cv2.imshow("AI Smart Traffic System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()