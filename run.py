from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2
import time
import numpy as np
model=YOLO('yolov8m-seg.pt')
model.predict(source="0",show=True,save=True)
cap=cv2.VideoCapture(0)
while cap.isOpened():
       st=time.perf_counter()
       ret,frame=cap.read()
       if not ret:
              break
       results=model(frame)
       et=time.perf_counter()
       fps=1/np.round(et-st,2)
       cv2.imshow('results',frame)


