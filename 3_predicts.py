#coding=utf-8
import cv2
from sklearn.externals import joblib
from PIL import Image
import numpy as np
import os
from sklearn import svm
import re

def check_video(i_video):
    videoCap= cv2.VideoCapture(i_video)
    if not videoCap.isOpened():
        log = i_video + " 该输入路径视频不存在，请检查"
        print(log)
    
    width = int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    model_name = 'model/' + str(width) + '_' + str(height) + '_model'
    clf = joblib.load(model_name)
    success = True
    start = 0.0
    end = 0.0
    count = 0
    while success:
        success, frame = videoCap.read()
        count += 1
        if success:
            milliseconds = videoCap.get(cv2.CAP_PROP_POS_MSEC)
            img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))  
            # img = img.crop((0, 40, img_w, img_w*1.5+40)) 
            #     # 缩放:
            img.thumbnail((width//10, height//10))
            a = np.array(img).reshape(1, -1)
            predicts = clf.predict(a)
            print predicts
            if predicts[0] == '2_icon_click' and start == 0:
                start = milliseconds
            if predicts[0] == '6_finish' and end == 0:
                end = milliseconds
    duration = end - start
    print '本次启动时间:' + str(int(duration)) + 'ms'


if __name__ == "__main__":
    check_video('test.mp4')