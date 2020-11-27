#coding=utf-8
from sklearn.externals import joblib
from PIL import Image
import numpy as np
import os
from sklearn import svm
import re

img_w = 0
img_h = 0

def pre_train_datas():
    global img_w
    global img_h
    label_list = []
    image_list = []
    image_classes = os.listdir("mark_data")
    for classes in image_classes:
        image_dir = os.getcwd() + '/mark_data/' + classes
        if not os.path.isdir(image_dir):
            continue
        for image_path in os.listdir(image_dir)[:-1]:
            if image_path.endswith(".jpg"):
                img = Image.open(image_dir+"/"+image_path)
                # 获得图像尺寸:
                img_w, img_h = img.size
                # img = img.crop((0, 40, img_w, img_w*1.5+40)) 
                # 缩放:
                img.thumbnail((img_w//10, img_h//10))
                image_list.append(np.asarray(img).flatten())
                label_list.append(classes)
    return image_list, label_list

def training_model():
    train_img, train_label = pre_train_datas()

    linear_svc = svm.LinearSVC()
    linear_svc.fit(train_img, train_label)
    model_name = 'model/' + str(img_w) + '_' + str (img_h) + '_model'
    joblib.dump(linear_svc, model_name)


if __name__ == "__main__":
    training_model()