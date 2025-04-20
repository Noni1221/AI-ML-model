import math
import pyautogui
import cv2

def process_hand_control(hand_results, mp_draw, frame, screen_w, screen_h):
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_draw.HAND_CONNECTIONS)

            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            index_x = int(index_tip.x * screen_w)
            index_y = int(index_tip.y * screen_h)

            pyautogui.moveTo(index_x, index_y)

            distance = math.hypot(
                (index_tip.x - thumb_tip.x),
                (index_tip.y - thumb_tip.y)
            )

            if distance < 0.03:
                pyautogui.click()
