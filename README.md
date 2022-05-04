# CVWebService

CVWebService implement some computer vision models and deploy them on Web as services.

## Usage

```shell
git clone https://github.com/Adenialzz/CVWebService.git
cd CVWebService
```

### yolov3 
```shell
wget https://pjreddie.com/media/files/yolov3.weights -P yolov3/yolov3_models/
wget https://pjreddie.com/media/files/yolov3-tiny.weights -P yolov3/yolov3_models/

python app.py
```

### Faster-RCNN 

```shell
mkdir mmdetection/checkpoints/
wget https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth -P mmdetection/checkpoints/

python app.py
```
