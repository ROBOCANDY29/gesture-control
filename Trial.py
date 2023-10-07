# Importing Libraries 
import cv2 
import mediapipe as mp 

# Used to convert protobuf message to a dictionary. 
from google.protobuf.json_format import MessageToDict 
import pyautogui

from pynput.keyboard import Key,Controller
keyboard = Controller()


cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width, screen_height=pyautogui.size()

index_y=0


# Initializing the Model 
mpHands = mp.solutions.hands 
hands = mpHands.Hands( 
	static_image_mode=False, 
	model_complexity=1,
	min_detection_confidence=0.75, 
	min_tracking_confidence=0.75, 
	max_num_hands=2) 

# Start capturing video from webcam 
cap = cv2.VideoCapture(0) 
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width, screen_height=pyautogui.size()

index_y=0

while True: 
	# Read video frame by frame 
	success, img = cap.read() 

	# Flip the image(frame) 
	img = cv2.flip(img, 1) 

	# Convert BGR image to RGB image 
	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

	# Process the RGB image 
	results = hands.process(imgRGB) 

	# If hands are present in image(frame) 
	if results.multi_hand_landmarks: 

		# Both Hands are present in image(frame) 
		if len(results.multi_handedness) == 2: 
				# Display 'Both Hands' on the image 
			cv2.putText(img, 'Both Hands', (250, 50), 
						cv2.FONT_HERSHEY_COMPLEX, 
						0.9, (0, 255, 0), 2) 

		# If any hand present 
		else: 
			for i in results.multi_handedness: 
				
				# Return whether it is Right or Left Hand 
				label = MessageToDict(i)['classification'][0]['label'] 

				if label == 'Left':
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

				if label == 'Right': 
					
					# Display 'Left Hand' 
					# on left side of window 
					cv2.putText(img, label+' Hand', (460, 50), 
								cv2.FONT_HERSHEY_COMPLEX, 
								0.9, (0, 255, 0), 2) 

	# Display Video and when 'q' 
	# is entered, destroy the window 
	cv2.imshow('Image', img) 
	if cv2.waitKey(1) & 0xff == ord('q'): 
		break
