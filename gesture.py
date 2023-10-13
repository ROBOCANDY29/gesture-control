import cv2
import mediapipe as mp
import pyautogui

from pynput.keyboard import Key, Controller


def smthg(rgb_frame, frame_height, frame_width, frame):
    keyboard = Controller()

    # from mediapipe.tasks import python
    # from mediapipe.tasks.python import vision

    # base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
    # options = vision.GestureRecognizerOptions(base_options=base_options)
    # recognizer = vision.GestureRecognizer.create_from_options(options)
    # results = []

    WRIST = 0
    INDEX_FINGER_PIP = 6
    INDEX_FINGER_TIP = 8
    MIDDLE_FINGER_MCP = 9
    MIDDLE_FINGER_PIP = 10
    MIDDLE_FINGER_TIP = 12
    RING_FINGER_MCP = 13
    RING_FINGER_PIP = 14
    RING_FINGER_TIP = 16
    PINKY_MCP = 17
    PINKY_PIP = 18
    PINKY_TIP = 20

    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()

    index_y = 0
    flag = 1

    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                if id == 16:  # ring
                    cv2.circle(img=frame, center=(x, y),
                               radius=10, color=(0, 255, 255))
                    ring_x = screen_width/frame_width*x
                    ring_y = screen_height/frame_height*y

                if id == 8:  # index finger tip
                    cv2.circle(img=frame, center=(x, y),
                               radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                    # pyautogui.moveTo(index_x, index_y)

                if id == 4:  # thumb tip
                    cv2.circle(img=frame, center=(x, y),
                               radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y-thumb_y))

                    if abs(index_y-thumb_y) < 30:
                        if abs(middle_y-thumb_y) < 30:
                            keyboard.press(Key.media_volume_mute)
                            keyboard.release(Key.media_volume_mute)
                            print('click')
                            # pyautogui.click()
                            pyautogui.sleep(2)
                            flag = 0
                            break

                        keyboard.press(Key.media_volume_up)
                        keyboard.release(Key.media_volume_up)
                        # pyautogui.click()
                        # pyautogui.sleep(1)
                        print('click')
                        flag = 0
                        break

                if id == 12:  # middle finger tip
                    cv2.circle(img=frame, center=(x, y),
                               radius=10, color=(0, 255, 255))
                    middle_x = screen_width/frame_width*x
                    middle_y = screen_height/frame_height*y
                    print('outside', abs(index_y-thumb_y))  # why?
                    if abs(middle_y-thumb_y) < 30:

                        if abs(index_y-thumb_y) < 30:
                            keyboard.press(Key.media_volume_mute)
                            keyboard.release(Key.media_volume_mute)
                            print('click')
                            # pyautogui.click()
                            pyautogui.sleep(2)
                            flag = 0
                            break

                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                        # pyautogui.click()
                        # pyautogui.sleep(1)
                        print('click')
                        flag = 0
                        break

                # if abs(middle_y-thumb_y)<30 and abs(index_y-thumb_y)<30:

                #          keyboard.press(Key.media_volume_mute)
                #          keyboard.release(Key.media_volume_mute)
                #          print('click')
                #          #pyautogui.click()
                #          pyautogui.sleep(2)
