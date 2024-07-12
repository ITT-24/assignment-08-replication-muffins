import cv2
import mediapipe as mp
import time


mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

VIDEO_ID = 2
cap = cv2.VideoCapture(VIDEO_ID)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # process the frame and get the face landmarks
    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            # get the coordinates of the nose tip
            nose_tip = face_landmarks.landmark[1]  # Nose tip index
            nose_x, nose_y = int(nose_tip.x * frame.shape[1]), int(nose_tip.y * frame.shape[0])

            # get the coordinates for the mouth
            mouth_indices = [61, 291, 78, 308, 191, 415, 80, 81, 82, 13, 312, 311, 310, 415]
            mouth_coords = [(int(face_landmarks.landmark[idx].x * frame.shape[1]),
                             int(face_landmarks.landmark[idx].y * frame.shape[0])) for idx in mouth_indices]

            min_mouth_x = min([coord[0] for coord in mouth_coords])
            max_mouth_x = max([coord[0] for coord in mouth_coords])
            min_mouth_y = min([coord[1] for coord in mouth_coords])
            max_mouth_y = max([coord[1] for coord in mouth_coords])

            # extend the mouth rectangle vertically
            vertical_extension = 20
            min_mouth_y -= vertical_extension
            max_mouth_y += vertical_extension

            # draw a square around the nose
            nose_square_size = 60
            nose_top_left = (nose_x - nose_square_size // 2, nose_y - nose_square_size // 2)
            nose_bottom_right = (nose_x + nose_square_size // 2, nose_y + nose_square_size // 2)
            cv2.rectangle(frame, nose_top_left, nose_bottom_right, (0, 255, 0), 2)

            print(f"Nose Square Coordinates:\n  Top Left: {nose_top_left}\n  Bottom Right: {nose_bottom_right}")

            # draw a square around the mouth
            mouth_top_left = (min_mouth_x, min_mouth_y)
            mouth_bottom_right = (max_mouth_x, max_mouth_y)
            cv2.rectangle(frame, mouth_top_left, mouth_bottom_right, (255, 0, 0), 2)

            print(f"Mouth Square Coordinates:\n  Top Left: {mouth_top_left}\n  Bottom Right: {mouth_bottom_right}\n")

            # reduce cpu load
            time.sleep(0.01)

    cv2.imshow('Mouth and Nose Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
