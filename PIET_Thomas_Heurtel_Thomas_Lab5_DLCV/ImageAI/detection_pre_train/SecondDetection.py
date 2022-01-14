from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()

custom_objects = detector.CustomObjects(car=True)
detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects, 
                    input_image=os.path.join(execution_path , "test1.jpeg"), 
                    output_image_path=os.path.join(execution_path , "image3custom.jpg"), 
                    minimum_percentage_probability=30)
for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )