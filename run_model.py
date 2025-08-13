from ultralytics import YOLO

model_best = YOLO("./runs/detect/train/weights/best.pt") # Melhor treino
model_last = YOLO("./runs/detect/train/weights/last.pt") # Último treino


# model = YOLO("yolo11n.pt")

results = model_last("./teste.mp4", show=True, save=True)