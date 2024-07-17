import cv2
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

#------------ FOR READING VIDEOS ---------------
#VIDEO_PATH = 'infrared_video_grey.avi'
#cap = cv2.VideoCapture(VIDEO_PATH)

# helper function to show px visually
def draw_center_square(frame, center_x, center_y, half_size, color):
    top_left = (center_x - half_size, center_y - half_size)
    bottom_right = (center_x + half_size, center_y + half_size)
    cv2.rectangle(frame, top_left, bottom_right, color, 2)
    cv2.line(frame, (center_x - 10, center_y), (center_x + 10, center_y), color, 2)
    cv2.line(frame, (center_x, center_y - 10), (center_x, center_y + 10), color, 2)

current_top_left= (0, 0)
current_bottom_right = (1200, 800) #frame size from resizing in other 

#while cap.isOpened():
def make_face_detection(frame_bw, face_part):
    global current_top_left, current_bottom_right
    #ret, frame = cap.read()
    #if not ret:
    #    break
    frame = cv2.cvtColor(frame_bw, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(frame)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
        # get the coordinates of nose tip
           # get the coordinates of nose tip
            nose_tip = face_landmarks.landmark[1]  # Nose tip index
            nose_x, nose_y = int(nose_tip.x * frame.shape[1]), int(nose_tip.y * frame.shape[0])

            # cross and label for nose tip
            cv2.line(frame, (nose_x - 10, nose_y), (nose_x + 10, nose_y), (0, 255, 0), 2)
            cv2.line(frame, (nose_x, nose_y - 10), (nose_x, nose_y + 10), (0, 255, 0), 2)
            cv2.putText(frame, 'Nose Tip', (nose_x + 5, nose_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # estimate coordinates for nose holes based on the nose tip
            nose_hole_distance_x = 30  # horizontal distance from nose tip to nose hole
            nose_hole_distance_y = 20  # vertical distance from nose tip to nose hole
            left_nose_x, left_nose_y = nose_x - nose_hole_distance_x, nose_y + nose_hole_distance_y
            right_nose_x, right_nose_y = nose_x + nose_hole_distance_x, nose_y + nose_hole_distance_y

            # calculate the top left and bottom right coordinates for the combined rectangle
            top_left_x = min(left_nose_x, right_nose_x) - 20
            top_left_y = min(left_nose_y, right_nose_y) - 20
            bottom_right_x = max(left_nose_x, right_nose_x) + 20
            bottom_right_y = max(left_nose_y, right_nose_y) + 20

            # move the rectangle down by a certain amount (e.g., 10 pixels)
            move_down_by = 10
            top_left_y += move_down_by
            bottom_right_y += move_down_by

            # draw the combined rectangle
            #cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 2)

            current_top_left = (top_left_x, top_left_y)
            current_bottom_right = (bottom_right_x, bottom_right_y)
            if(face_part == "nose"):
                return current_top_left, current_bottom_right #TODO: ENABLE FOR NOSE

            # draw rectangles around the estimated nose holes
            nose_hole_size = 40
            cv2.rectangle(frame, (left_nose_x - nose_hole_size // 2, left_nose_y - nose_hole_size // 2),
                          (left_nose_x + nose_hole_size // 2, left_nose_y + nose_hole_size // 2), (0, 0, 255), 2)
            cv2.rectangle(frame, (right_nose_x - nose_hole_size // 2, right_nose_y - nose_hole_size // 2),
                          (right_nose_x + nose_hole_size // 2, right_nose_y + nose_hole_size // 2), (0, 0, 255), 2)
            # draw squares around the nose holes
            # half of the side length of the square that includes 100 pixels
            nose_hole_half_size = 5  
            draw_center_square(frame, left_nose_x, left_nose_y, nose_hole_half_size, (0, 255, 255))
            draw_center_square(frame, right_nose_x, right_nose_y, nose_hole_half_size, (0, 255, 255))

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

            x_distance = max_mouth_x - min_mouth_x
            y_distance = max_mouth_y - min_mouth_y

            current_top_left = (min_mouth_x + x_distance//3,  min_mouth_y + y_distance//3)
            current_bottom_right = (max_mouth_x - x_distance//3, max_mouth_y - y_distance//3)
            
            cv2.rectangle(frame, current_top_left, current_bottom_right, (255, 0, 0), 2)

            # # reduce CPU load
            # time.sleep(0.1)

    return current_top_left, current_bottom_right
    # cv2.imshow('Mouth and Nose Detection', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     pass

# cap.release()
cv2.destroyAllWindows()
