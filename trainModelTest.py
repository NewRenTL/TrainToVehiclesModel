import torch

from ultralytics import YOLO

#print(torch.cuda.is_available())

#model = YOLO("yolov8n.pt")

#model.train(data="datase.yaml",epochs=30,)


#Testing with a video

model = YOLO("./Models/V2/modelReady/best.pt")

results = model(source = "traffic.mp4",show=True,conf=0.1,save = True)

#yolo task=detect mode=train epochs=100 data=dataset.yaml model=yolov8n.pt imgsz=640 batch=10 amp=False