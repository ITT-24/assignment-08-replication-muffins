import cv2
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

VIDEO_PATH = 'infrared_video_grey.avi'
cap = cv2.VideoCapture(VIDEO_PATH)

# set to 100 -> shoudl be enough for meassuring
def get_center_square_pixels(center_x, center_y, half_size):
    pixels = [(x, y) for x in range(center_x - half_size, center_x + half_size)
              for y in range(center_y - half_size, center_y + half_size)]
    return pixels[:100]

# helper function to show px visually
def draw_center_square(frame, center_x, center_y, half_size, color):
    top_left = (center_x - half_size, center_y - half_size)
    bottom_right = (center_x + half_size, center_y + half_size)
    cv2.rectangle(frame, top_left, bottom_right, color, 2)
    cv2.line(frame, (center_x - 10, center_y), (center_x + 10, center_y), color, 2)
    cv2.line(frame, (center_x, center_y - 10), (center_x, center_y + 10), color, 2)

# get the coordinates for further calculations -> here we should be able to add calculations
def print_pixels_around_center(frame, center_x, center_y, half_size):
    pixels = get_center_square_pixels(center_x, center_y, half_size)
    for pixel in pixels:
        px_id = frame[pixel[1], pixel[0]]
        print(f"Pixel at ({pixel[0]}, {pixel[1]}): {px_id}")


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    result = face_mesh.process(frame)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            # get the coordinates of nose tip
            nose_tip = face_landmarks.landmark[1]  # Nose tip index
            nose_x, nose_y = int(nose_tip.x * frame.shape[1]), int(nose_tip.y * frame.shape[0])

            # cross and label for  nose tip
            cv2.line(frame, (nose_x - 10, nose_y), (nose_x + 10, nose_y), (0, 255, 0), 2)
            cv2.line(frame, (nose_x, nose_y - 10), (nose_x, nose_y + 10), (0, 255, 0), 2)
            cv2.putText(frame, 'Nose Tip', (nose_x + 5, nose_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # square around nose tip
            nose_half_size = 5
            """ draw_center_square(frame, nose_x, nose_y, nose_half_size, (0, 255, 255)) """

            print("Nose Tip Square:")
            print_pixels_around_center(frame, nose_x, nose_y, nose_half_size)

            # estimate coordinates for nose holes based on the nose tip
            nose_hole_distance_x = 30  # horizontal distance from nose tip to nose hole
            nose_hole_distance_y = 20  # vertical distance from nose tip to nose hole
            left_nose_x, left_nose_y = nose_x - nose_hole_distance_x, nose_y + nose_hole_distance_y
            right_nose_x, right_nose_y = nose_x + nose_hole_distance_x, nose_y + nose_hole_distance_y

            # draw rectangles around the estimated nose holes
            nose_hole_size = 40
            cv2.rectangle(frame, (left_nose_x - nose_hole_size // 2, left_nose_y - nose_hole_size // 2),
                          (left_nose_x + nose_hole_size // 2, left_nose_y + nose_hole_size // 2), (0, 0, 255), 2)
            cv2.rectangle(frame, (right_nose_x - nose_hole_size // 2, right_nose_y - nose_hole_size // 2),
                          (right_nose_x + nose_hole_size // 2, right_nose_y + nose_hole_size // 2), (0, 0, 255), 2)
            cv2.line(frame, (left_nose_x - 10, left_nose_y), (left_nose_x + 10, left_nose_y), (0, 255, 0), 2)
            cv2.line(frame, (left_nose_x, left_nose_y - 10), (left_nose_x, left_nose_y + 10), (0, 255, 0), 2)
            cv2.line(frame, (right_nose_x - 10, right_nose_y), (right_nose_x + 10, right_nose_y), (0, 255, 0), 2)
            cv2.line(frame, (right_nose_x, right_nose_y - 10), (right_nose_x, right_nose_y + 10), (0, 255, 0), 2)

            # draw squares around the nose holes
            # half of the side length of the square that includes 100 pixels
            nose_hole_half_size = 5  
            draw_center_square(frame, left_nose_x, left_nose_y, nose_hole_half_size, (0, 255, 255))
            draw_center_square(frame, right_nose_x, right_nose_y, nose_hole_half_size, (0, 255, 255))

            # print pixel IDs around the nose holes
            print("Left Nose Hole Square:")
            print_pixels_around_center(frame, left_nose_x, left_nose_y, nose_hole_half_size)

            print("Right Nose Hole Square:")
            print_pixels_around_center(frame, right_nose_x, right_nose_y, nose_hole_half_size)

            # coordinates for mouth
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

            mouth_top_left = (min_mouth_x, min_mouth_y)
            mouth_bottom_right = (max_mouth_x, max_mouth_y)
            cv2.rectangle(frame, mouth_top_left, mouth_bottom_right, (255, 0, 0), 2)

            # calculate the center of the mouth square
            mouth_center_x = (min_mouth_x + max_mouth_x) // 2
            mouth_center_y = (min_mouth_y + max_mouth_y) // 2

            # draw a cross 
            cv2.line(frame, (mouth_center_x - 10, mouth_center_y), (mouth_center_x + 10, mouth_center_y), (0, 255, 0), 2)
            cv2.line(frame, (mouth_center_x, mouth_center_y - 10), (mouth_center_x, mouth_center_y + 10), (0, 255, 0), 2)
            cv2.putText(frame, 'Mouth', (mouth_center_x + 5, mouth_center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # draw square around the central 100 pixels of the mouth
            # half of the side length of the square that includes 100 pixels
            mouth_half_size = 5  
            draw_center_square(frame, mouth_center_x, mouth_center_y, mouth_half_size, (0, 255, 255))

            print("Mouth Square:")
            print_pixels_around_center(frame, mouth_center_x, mouth_center_y, mouth_half_size)

            # reduce CPU load
            time.sleep(0.1)

    cv2.imshow('Mouth and Nose Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
