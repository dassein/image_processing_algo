#include<opencv2/opencv.hpp>
#include<iostream>
using namespace cv;
using namespace std;
void test() {
    Mat img = imread("extract_line.png"); 
    if (img.empty()) {
        cout << "image not exist" << endl;
    }
    Mat img_gray;
    cvtColor(img, img_gray, CV_BGR2GRAY);

    Mat img_binary;
    adaptiveThreshold(~img_gray, img_binary, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 15, -2); //~grayImg注意这里灰度先取反
    imshow("image_binary", img_binary);

    Mat hline = getStructuringElement(MORPH_RECT, Size(img.cols / 16, 1), Point(-1, -1));  //horizontal line
    Mat vline = getStructuringElement(MORPH_RECT, Size(1, img.rows / 16), Point(-1, -1));   //vertical line
    Mat kernel = getStructuringElement(MORPH_RECT, Size(3,3), Point(-1, -1));  // line from all directions

    Mat img_open;
    morphologyEx(img_binary, img_open, CV_MOP_OPEN, vline);  // change last param:  hline, vline, kernel
    // post-process
    blur(img_open, img_open, Size(3, 3), Point(-1, -1));
    bitwise_not(img_open, img_open);  //background -> white
    imshow("open", img_open);
}

int main() {
    test();
    waitKey(0);
    return 0;
}