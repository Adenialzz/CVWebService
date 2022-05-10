# CVWebService

CVWebService implement some computer vision models and deploy them on Web as services.

## clone this repo

```shell
git clone https://github.com/Adenialzz/CVWebService.git
cd CVWebService
```

## setting port forward (optional)

Forwarding the intranet port to the public network through frp (requires a ECS with public IP).
See this [blog](https://blog.csdn.net/weixin_44966641/article/details/124578063) for detailed steps of setting port foward. Both ECS server and local client need to be configured.

After the server configuration is completed, configure on the local client:
```shell
wget https://github.com/fatedier/frp/releases/download/v0.42.0/frp_0.42.0_linux_amd64.tar.gz
tar xf frp_0.42.0_linux_amd64.tar.gz && rm frp_0.42.0_linux_amd64.tar.gz
mv frp_0.42.0_linux_amd64/ frp/
vi frp/frpc.ini
'''
[common]
server_addr = xx.xxx.xxx.xx
server_port = 7000
token = xxxxxx

[CVWebService]
type = tcp
local_ip = 0.0.0.0
local_port = 7100
remote_port = 7200
# ...
'''
cd frp/
nohup ./frpc -c frpc.ini 2>&1 > frpc.log &
cd ..
```

## run service


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
