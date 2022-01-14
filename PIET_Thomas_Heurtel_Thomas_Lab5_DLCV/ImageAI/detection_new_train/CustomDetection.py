from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("detection_model-ex-021--loss-0017.681.h5") 
detector.setJsonPath("detection_config.json")
detector.loadModel()
detections, objects_path = detector.detectObjectsFromImage(input_image="jordan5.jpg", output_image_path="jordan_detected5.jpg", minimum_percentage_probability=30,  extract_detected_objects=True)

for eachObject, eachObjectPath in zip(detections, objects_path):
    print(eachObject["name"] , " : " , eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("Object's image saved in " + eachObjectPath)
    print("--------------------------------")
