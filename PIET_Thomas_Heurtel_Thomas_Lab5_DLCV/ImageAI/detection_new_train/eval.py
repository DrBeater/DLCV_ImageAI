from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="dataset_jordan1")
trainer.evaluateModel(model_path="dataset_jordan1/models", json_path="dataset_jordan1/json/detection_config.json", iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)
