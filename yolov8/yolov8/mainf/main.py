from ultralytics import YOLO
import torch

model = YOLO(r'C:\Users\hp\Desktop\yolov8\runs\detect\train\weights\best.pt')  # load a custom model
model.to('cuda')
source=r'C:\Users\hp\Desktop\yolov8\mainf\image\Fuente0parte_amistoso_6_26.jpg'
# Validate the model

cuda = torch.cuda.is_available()



if __name__ == '__main__':
    # Use the model
    model.train(data=r"C:\Users\hp\Desktop\yolov8\mainf\config.yaml", epochs=30, imgsz=640, batch=1)  # train the model
    metrics = model.val(imgsz=640, batch=2)  # no arguments needed, dataset and settings remembered
    metrics.box.map    # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps
    model.predict(source, save=True, imgsz=640,save_txt=True)
    # Export the model
    model.export(format='onnx')