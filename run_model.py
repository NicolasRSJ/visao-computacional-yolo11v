from ultralytics import YOLO

model_best = YOLO("./runs/detect/train/weights/best.pt") # Melhor modelo do treino
model_last = YOLO("./runs/detect/train/weights/last.pt") # Último modelo do treino

# model = YOLO("yolo11n.pt")

results = model_last("./teste.mp4", show=True, save=True)