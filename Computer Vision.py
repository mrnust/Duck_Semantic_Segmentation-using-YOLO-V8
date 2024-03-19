

#  Object detection  (  Vehicle Number Plate Detection )-----------------------------------------

# from ultralytics import YOLO

# # Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch

# # Use the model
# model.train(data="config.yaml", epochs=30)  # train the model












# Image classification ( Cat and Dog classification) ---------------------------------------


# from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n-cls.pt")  # build a new model from scratch

# Use the model
# model.train(data="C:/Users/HP/Desktop/Python/Dog and Cat Image classifier", epochs=20)  # train the model

# model.train(data="D:\Datasets for Computer vision projects/Dog and Cat Image classifier", epochs=20)  # train the model
#








#semantic Segmentation ( duck semantic segmentation)---------------------------------------

# from ultralytics import YOLO

# # Load a model

# model = YOLO('yolov8n-seg.pt')  # load a pretrained model (recommended for training)

# # Train the model
# results = model.train(data='config.yaml', epochs=2)





#Quadruped keypoints detection ---------------------------------------------------------------

# from ultralytics import YOLO

# # Load a model

# model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)

# # Train the model
# results = model.train(data='config.yaml', epochs=25)





# kitti data set------------------------------------------------------------------------------


from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # build a new model from scratch

# Use the model
model.train(data="config.yaml", epochs=20)  # train the model




#using yolo v9



from ultralytics import YOLO

# Load a model
model = YOLO('yolov9c.pt') # build a new model from scratch

# Use the model
model.train(data="config.yaml", epochs=40,batch=1)  # train the model






