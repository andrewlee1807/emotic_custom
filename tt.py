# import cv2
#
# # define a video capture object
# vid = cv2.VideoCapture(0)
#
# while (True):
#
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
#
#     # to be used.
#     font = cv2.FONT_HERSHEY_SIMPLEX
#
#     # Use putText() method for
#     # inserting text on video
#     cv2.putText(frame,
#                 'TEXT ON VIDEO',
#                 (50, 50),
#                 font, 1,
#                 (0, 255, 255),
#                 2,
#                 cv2.LINE_4)
#
#     # Display the resulting frame
#
#
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # After the loop release the cap object
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()

import tqdm


