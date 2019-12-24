import numpy as np 

def hist(img):
    hist = np.zeros((256, )).astype(int) # 0~255
    for i in img:
        for j in i:
            hist[j] += 1
    return hist

def acc_hist(hist):
    acc_hist = []
    cumsum = 0
    for e in hist:
        cumsum += e
        acc_hist.append(cumsum)
    return acc_hist

if __name__ == "__main__":
    import cv2
    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    hist = hist(img_gray)
    # print(hist)
    import matplotlib.pyplot as plt
    import numpy as np
    # plt.stem([i for i in range(256)], hist, use_line_collection=True)
    plt.bar([i for i in range(256)], hist)
    plt.show()
    plt.savefig('./output_images/chap3_3_hist.jpg')
    hist_acc = acc_hist(hist)
    # plt.stem([i for i in range(256)], hist_acc, use_line_collection=True)
    plt.bar([i for i in range(256)], hist_acc)
    plt.show()
    plt.savefig('./output_images/chap3_3_acc_hist.jpg')