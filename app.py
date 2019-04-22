import cv2
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import _thread
import time
import os


def main():
  while(True):
    # time.sleep(5)
    print('Taking Picture')
    camera_port = 0 
    ramp_frames = 30 
    camera = cv2.VideoCapture(camera_port)
    def get_image():
      retval, im = camera.read()
      return im 
    for i in range(ramp_frames):
      temp = camera.read()

    camera_capture = get_image()
    filename = "webcam-picture.png"
    cv2.imwrite(filename,camera_capture)
    del(camera)

    PREDICTION_KEY = os.environ.get('VISION_PREDICTION_KEY')
    ENDPOINT = os.environ.get('VISION_ENDPOINT')
    PROJECT_ID = os.environ.get('VISION_PROJECT_ID')
    predictor = CustomVisionPredictionClient(PREDICTION_KEY, endpoint=ENDPOINT)
    publish_iteration_name = os.environ.get('VISION_PUBLISHED_ITERATION_NAME')

    # Open the sample image and get back the prediction results.
    with open("webcam-picture.png", mode="rb") as test_data:
      results = predictor.classify_image(PROJECT_ID, publish_iteration_name, test_data)

    # Display the results.    
    for prediction in results.predictions:
        print(str(prediction))
    time.sleep(25)

main()
