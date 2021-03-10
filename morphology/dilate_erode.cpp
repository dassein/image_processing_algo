#include<opencv2/opencv.hpp>
#include<iostream>

using namespace std;
using namespace cv;

void test() {
    Mat img = imread("./binary.png");
    if (img.empty()) {
        cout << "image not exist" <<endl;
    }
    // display image
    namedWindow("image");
    imshow("image", img);
    // BGR -> gray
    Mat img_gray;
    cvtColor(img, img_gray, CV_BGR2GRAY);
    namedWindow("image gray");
    imshow("image gray", img_gray);
    // erosion with default 3 by 3 Structuring element
    Mat img_erode; 
    erode(img_gray, img_erode, Mat());
    namedWindow("erode");
    imshow("erode", img_erode);
    // dilation with default 3 by 3 Structuring element
    Mat img_dilate; 
    dilate(img_gray, img_dilate, Mat());
    namedWindow("dilate");
    imshow("dilate", img_dilate);
    return;
}

int main() {
    test();
    waitKey(0);
    return 0;
}