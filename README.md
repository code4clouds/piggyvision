# PiggyVision

This is a sample application on how to use Azure Custom Vision with a webcam to recognize objects.

## Goal

The project has photo sets of two guinea pigs that I used to classify my subjects (Coco and Cleo) and identify which one am I holding in front of the webcam.

## Requirements
- Python 3.x
- OpenCV libraries

## Usage
- Train the Custom Vision AI using the picture in the image folder using the [Azure Custom Vision](https://www.customvision.ai/)
- You will need to fill the following environmental variables for the application to work:

```
VISION_PREDICTION_KEY=""
VISION_ENDPOINT=""
VISION_PROJECT_ID=""
VISION_PUBLISHED_ITERATION_NAME=""
```

## References
- [What is Azure Custom Vision?](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/home)
- [Quickstart: Create an object detection project with the Custom Vision Python SDK](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/python-tutorial-od)