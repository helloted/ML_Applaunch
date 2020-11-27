#coding=utf-8
import sys,getopt,os
import cv2

def log_video_info(i_video):
    cap = cv2.VideoCapture(i_video)
    if not cap.isOpened():
        log = i_video + " 该输入路径视频不存在，请检查"
        print(log)
    # 帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 分辨率-宽度
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 分辨率-高度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 总帧数
    frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cap.release()
    # 时长，单位s
    duration = frame_counter / fps

    print '视频信息:'
    print ('总时长:'+str(round(duration, 2) )+'s')
    print ('帧数:' + str(frame_counter) +' 帧率:'+str(fps))
    print ('宽:' + str(width) +' 高:' + str(height))

def make_dir(folder):
    feature_dir = os.path.join(os.getcwd(), folder)
    if not os.path.exists(feature_dir):
        os.makedirs(feature_dir) 

def make_all_folder():
    make_dir('mark_data/0_pre') # 桌面前
    make_dir('mark_data/1_home') # 桌面状态
    make_dir('mark_data/2_icon_click') # 点击icon
    make_dir('mark_data/3_default_show') # 默认启动图
    make_dir('mark_data/4_ad_show') # 广告页
    make_dir('mark_data/5_first_screen') # 首页
    make_dir('mark_data/6_finish') # 完成

def cut_video(i_video,o_video):
    print 'cuting...'
    videoCap= cv2.VideoCapture(i_video)
    if not videoCap.isOpened():
        log = i_video + " 该输入路径视频不存在，请检查"
        print(log)
    success, frame = videoCap.read()
    count = 0
    while success:
        if cv2.waitKey(1) == 27:
            break
        count += 1
        success, frame = videoCap.read()
        cv2.imwrite(os.path.join(o_video, 'o_' + str(count) + '.jpg'), frame)

    # cv2.destroyAllWindows()
    videoCap.release()
    print 'cut finish'

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print '请输入这样的格式:python 1_mark_data.py train.mp4'
    else:
        inputfile = sys.argv[1]
        log_video_info(inputfile)
        make_all_folder()
        cut_video(inputfile,'mark_data')