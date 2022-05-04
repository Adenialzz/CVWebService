from CVServiceModels.BaseCVServiceModel import BaseCVServiceModel

import torch
import mmcv
from mmdet.apis import init_detector, inference_detector

class FasterRcnnGeneralDetection(BaseCVServiceModel):
    def __init__(self):
        self.config = 'mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
        self.checkpoint = 'mmdetection/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.detector = init_detector(self.config, self.checkpoint, self.device)


    def run(self, path, **kwargs):
        img = mmcv.imread(path)

        thr = kwargs.get('thr', 0.85)
        out_file = kwargs.get('out_file', None)

        result = inference_detector(self.detector, img)
        self.detector.show_result(img, result, thr, out_file=out_file)
        return result

    def post_run(self):
        pass

if __name__ == "__main__":
    model = FasterRcnnGeneralDetection()
    image_path = 'assets/test.jpg'
    kwargs = {
        'thr': 0.85,
        # 'out_file': 'test.jpg'
    }
    res = model.run(image_path, **kwargs)
    print(res)


