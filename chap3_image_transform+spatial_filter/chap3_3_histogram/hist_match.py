import numpy as np 

def match_hist(pdf_acc, pdf_acc_reference): # len(pdf_acc) == ln(pdf_acc_reference)
    correspond = [len(pdf_acc)-1]
    for ii in range(len(pdf_acc_reference)-2, -1, -1):
        jj = correspond[0]  # index of acc_pdf => ii of acc_pdf_reference
        while True:
            if (jj <= 0) or (pdf_acc[jj] <= pdf_acc_reference[ii]):
                correspond.insert(0, jj)
                break
            jj -= 1
    return correspond

def match_img(img, inv_correspond): # inv_correspond: use pdf_acc_reference -> to fit pdf_acc
    H, W = img.shape[0], img.shape[1]
    img_matched = np.zeros((H, W)).astype(int) # 0~255
    for i in range(H):
        for j in range(W):
            img_matched[i][j] = inv_correspond[ img[i][j] ]
    return img_matched


if __name__ == "__main__":
    import cv2
    from hist import hist, acc_hist
    import matplotlib.pyplot as plt

    img_gray = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    H, W = img_gray.shape[0], img_gray.shape[1]

    hist = hist(img_gray)
    # plt.bar([i for i in range(256)], hist)
    # plt.show()
    # plt.savefig('./output_images/chap3_3_hist.jpg')
    # plt.close()
    hist_acc = acc_hist(hist)
    # plt.bar([i for i in range(256)], hist_acc)
    # plt.show()
    # plt.savefig('./output_images/chap3_3_acc_hist.jpg')
    # plt.close()
    pdf_acc = list(map(lambda x: x/( H * W ), hist_acc))
    pdf_acc_reference = [(i+1)/256 for i in range(256)]
    correspond = match_hist(pdf_acc, pdf_acc_reference) # use pdf_acc -> to fit pdf_acc_reference
    pdf_acc_match = list(map(lambda ind: pdf_acc[ind], correspond)) # pdf_acc[correspond]
    # print(correspond)
    plt.bar([i for i in range(256)], pdf_acc_match)
    plt.show()
    plt.savefig('./output_images/chap3_3_match_hist.jpg')
    plt.close()

    inv_correspond = match_hist(pdf_acc_reference, pdf_acc) # use pdf_acc_reference -> to fit pdf_acc
    img_matched = match_img(img_gray, inv_correspond)
    cv2.imwrite('./output_images/chap3_3_match_img.jpg', img_matched)
    plt.imshow(img_matched, cmap='gray') # show in gray scale
    plt.show()
    plt.savefig('./output_images/chap3_3_match_img_plt.jpg') # not grayscale
    plt.close()