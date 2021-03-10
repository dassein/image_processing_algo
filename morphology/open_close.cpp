#include<opencv2/opencv.hpp>
#include<iostream>

using namespace std;
using namespace cv;

void test() {
    Mat img = imread("./img_open.png");
    if (img.empty()) {
        cout << "image not exist" <<endl;
    }
    // BGR -> gray
    Mat img_gray;
    cvtColor(img, img_gray, CV_BGR2GRAY);
    namedWindow("gray open");
    imshow("gray open", img_gray);
    // opening
    Mat element(5, 5, CV_8U, Scalar(1));
    Mat img_open;
    morphologyEx(img_gray, img_open, MORPH_OPEN, element);
    namedWindow("open");
    imshow("open", img_open);
    //
    img = imread("./img_close.png");
    if (img.empty()) {
        cout << "image not exist" <<endl;
    }
    // BGR -> gray
    cvtColor(img, img_gray, CV_BGR2GRAY);
    namedWindow("gray close");
    imshow("gray close", img_gray);
    // closing
    Mat img_close;
    morphologyEx(img_gray, img_close, MORPH_CLOSE, element);
    namedWindow("close");
    imshow("close", img_close);
    return;
}

int main() {
    test();
    waitKey(0);
    return 0;
}