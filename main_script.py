import cv2
import mediapipe as mp
import pydirectinput
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

time.sleep(0.5)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def is_finger_up(hand_landmarks, finger_tip_index, finger_pip_index):
    return hand_landmarks.landmark[finger_tip_index].y < hand_landmarks.landmark[finger_pip_index].y

print("Start cuy!")
time.sleep(3)

status_stir = "Lurus"   
status_gerak = "Diam"

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(img_rgb)

    dead_zone_percent = 0.20
    left_boundary = width * (0.5 - dead_zone_percent / 2)
    right_boundary = width * (0.5 + dead_zone_percent / 2)

    cv2.line(img, (int(left_boundary), 0), (int(left_boundary), height), (0, 255, 255), 2)
    cv2.line(img, (int(right_boundary), 0), (int(right_boundary), height), (0, 255, 255), 2)

    status_stir = "Lurus"
    status_gerak = "Diam"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            wrist_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * width

            if wrist_x < left_boundary:
                pydirectinput.press('a')
                status_stir = "Belok Kiri"
            elif wrist_x > right_boundary:
                pydirectinput.press('d')
                status_stir = "Belok Kanan"

            index_up = is_finger_up(hand_landmarks, mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.INDEX_FINGER_PIP)
            middle_up = is_finger_up(hand_landmarks, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP)
            ring_up = is_finger_up(hand_landmarks, mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_PIP)
            pinky_up = is_finger_up(hand_landmarks, mp_hands.HandLandmark.PINKY_TIP, mp_hands.HandLandmark.PINKY_PIP)

            if index_up and middle_up and ring_up and pinky_up:
                pydirectinput.keyDown('s')
                pydirectinput.keyUp('w')
                status_gerak = "Mundur / Rem"
            elif not index_up and not middle_up and not ring_up and not pinky_up:
                pydirectinput.keyDown('w')
                pydirectinput.keyUp('s')
                status_gerak = "Maju"
            else:
                pydirectinput.keyUp('w')
                pydirectinput.keyUp('s')
                status_gerak = "Diam"

    else:
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('s')

    font = cv2.FONT_HERSHEY_SIMPLEX
    pos_stir = (20, 50)
    pos_gerak = (20, 90)
    font_scale = 1
    font_color = (0, 0, 255)
    line_type = 2

    cv2.putText(img, f"Stir: {status_stir}", pos_stir, font, font_scale, font_color, line_type)
    cv2.putText(img, f"Gerak: {status_gerak}", pos_gerak, font, font_scale, font_color, line_type)

    cv2.imshow("DEBUG", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

pydirectinput.keyUp('w'); pydirectinput.keyUp('s'); pydirectinput.keyUp('a'); pydirectinput.keyUp('d')
cap.release()
cv2.destroyAllWindows()