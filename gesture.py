import cv2
import mediapipe as mp
import pyautogui

from pynput.keyboard import Key,Controller
keyboard = Controller()


cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width, screen_height=pyautogui.size()

index_y=0

while(True):
    ret, frame= cap.read()
    frame=cv2.flip(frame, 1)
    frame_height, frame_width, _ =frame.shape
    rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks=hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)

                if id==8:#index finger tip
                    cv2.circle(img=frame,center=(x,y), radius=10, color=(0,255,255))
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_height*y
                    # pyautogui.moveTo(index_x, index_y)

                if id==4: #thumb tip
                    cv2.circle(img=frame,center=(x,y), radius=10, color=(0,255,255))
                    thumb_x=screen_width/frame_width*x
                    thumb_y=screen_height/frame_height*y
                    print('outside', abs(index_y-thumb_y))
                    
                    if abs(index_y-thumb_y)<30:
                        
                        if abs(middle_y-thumb_y)<30:
                            keyboard.press(Key.media_volume_mute)
                            keyboard.release(Key.media_volume_mute)
                            print('click')
                            #pyautogui.click()
                            pyautogui.sleep(2)
                        
                        keyboard.press(Key.media_volume_up)
                        keyboard.release(Key.media_volume_up)
                        #pyautogui.click()
                        #pyautogui.sleep(1)
                        print('click')
                        
                if id==12:#middle finger tip
                    cv2.circle(img=frame,center=(x,y), radius=10, color=(0,255,255))
                    middle_x=screen_width/frame_width*x
                    middle_y=screen_height/frame_height*y
                    print('outside', abs(index_y-thumb_y))#why?

                    if abs(middle_y-thumb_y)<30:
                        
                        if abs(index_y-thumb_y)<30:
                            keyboard.press(Key.media_volume_mute)
                            keyboard.release(Key.media_volume_mute)
                            print('click')
                            #pyautogui.click()
                            pyautogui.sleep(2)
                        
                        
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                        #pyautogui.click()
                        #pyautogui.sleep(1)
                        print('click')
                    
                # if abs(middle_y-thumb_y)<30 and abs(index_y-thumb_y)<30:
                        
                #          keyboard.press(Key.media_volume_mute)
                #          keyboard.release(Key.media_volume_mute)
                #          print('click')
                #          #pyautogui.click()
                #          pyautogui.sleep(2)
                        
                    
                    
                    
                      

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    
    
    
     

