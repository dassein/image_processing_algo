/**
 * mkdir build && cd build
 * cmake ..
 * make
 * make install
 **/
#include<opencv2/opencv.hpp>
#include<iostream>
#include<string>

using namespace std;
using namespace cv;
void test() {
    // read image
    Mat img = imread("./road.jpg");
    if (img.empty()) {
        cout << "image not exist" << endl;
    }
    // display image
    namedWindow("image", CV_WINDOW_AUTOSIZE);
    imshow("image", img);
    // BGR -> gray
    Mat img_gray;
    cvtColor(img, img_gray, CV_BGR2GRAY);
    // Canny: find contour of gray image
    Mat contour;
    Canny(img_gray, contour, 125, 350); // meaning of 125, 350
    // diplay contour
    namedWindow("Canny: contour of gray image", CV_WINDOW_AUTOSIZE);
    imshow("Canny: contour of gray image", contour);
    return;
}

int main() {
    test();
    waitKey(0);
    return 0;
}