"""
导入科学计算的包，用于数据打包
"""
import os
import cv2
import numpy as np


# 加载图片函数
def Get_X_face():
    # 2、遍历文件夹
    dirs = os.listdir("x_face")
    # 创建一个变量，用于存储数据
    x = []  # 存储图片信息   存储所有图片
    y = []  # 存储图片分类
    for j, dir in enumerate(dirs):
        # print(j,dir)
        for i in range(0, 12):
            img = cv2.imread("x_face/%s/%d.jpg" % (dir, i))
            img = cv2.cvtColor(img, code=cv2.COLOR_RGB2GRAY)
            x.append(img)
            y.append(j)
    return [x, y, dirs]


def face_first():
    # 1、加载图片
    x, y, dirs = Get_X_face()
    # print(dirs)
    # 先矩阵序列化进行打乱数据，以同样的方式
    x = np.asarray(x)
    y = np.asarray(y)
    #     模拟数据
    index = [i for i in range(0, len(y))]
    # print(index)打乱数据
    np.random.shuffle(index)
    # print(index)
    #     根据打乱的下标 打乱图片数据
    x = x[index]
    y = y[index]
    #     打乱数据开始数据训练
    x_train = x[:len(x)]  # 提取出要训练的数据，预留10 不加入数据中
    y_train = y[:len(y)]
    # 测试数据
    x_test = x[len(x) - 10:]  # 提取出10个测试数据
    y_test = y[len(y) - 10:]
    # 创建训练场地
    model = cv2.face.EigenFaceRecognizer_create()
    # 进行训练
    model.train(x_train, y_train)
    # 训练结果
    # for face_01 in x_test:
    #     result = model.predict(face_01)
    #     print("对比结果", result)
    #     print("检测出人物： ", dirs[result[0]])
    img = cv2.imread("x_face/wbb/12.jpg")
    img = cv2.cvtColor(img, code=cv2.COLOR_RGB2GRAY)
    result = model.predict(img)
    print(result)
    print(dirs[result[0]])

    ##############################
    video = cv2.VideoCapture(0)
    face_data = cv2.CascadeClassifier("Include/haarcascade_frontalface_alt.xml")
    while True:
        flag, img = video.read()
        if flag:
            face = face_data.detectMultiScale(img)
            for x, y, w, h in face:
                cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255])
                new_face = img[y:y + h, x:x + w]
                new_face = cv2.cvtColor(new_face, cv2.COLOR_RGB2GRAY)
                new_face = cv2.resize(new_face, dsize=(200, 200))
                result = model.predict(new_face)
                # print("检测到的数据:+++",result)
                print(dirs[result[0]])
                print(dirs[result[0]])

                if result[1] > 50:
                    cv2.putText(img, "NO", (x, y), cv2.FONT_ITALIC, 3, color=[0, 255, 0])
                else:
                    cv2.putText(img, dirs[result[0]], (x, y), cv2.FONT_ITALIC, 3, color=[0, 255, 0])
                cv2.imshow("LSF", img)
                cv2.waitKey(10)
            pass
        if dirs[result[0]] == 'wbb':
            cv2.waitKey(2000)
            return "wbb"

    cv2.destroyAllWindows()
    video.relesse()


if __name__ == '__main__':
    result = face_first()
    print("欢迎%s登录" % result)
