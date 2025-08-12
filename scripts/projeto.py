from ultralytics import YOLO

model_seg = YOLO("yolo11n-seg.pt")
model_pose = YOLO("yolo11n-pose.pt")
model_detc = YOLO("yolo11n.pt")

path1 = "./video.mp4"
path2 = "./video2.mp4"

results = model_pose(path2, show=True, save=True)
