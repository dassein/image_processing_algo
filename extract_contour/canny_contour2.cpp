#include<opencv2/opencv.hpp>
#include<iostream>
#include<string>

using namespace std;
using namespace cv;

const int THR = 100;     // threshold
const int THR_MAX = 255;

void get_contour(Mat& img_in, Mat& img_out) {
    Mat img_canny = Mat::zeros(img_in.size(), CV_8UC3);  //初始化;
    img_out = Mat::zeros(img_in.size(), CV_8UC3);
    vector<vector<Point>> vector_contour;
    vector<Vec4i> hierachy;
    // Canny: find contour of gray image
    Canny(img_in, img_canny, THR, THR * 2, 3, false);
    findContours(img_canny, // 输入图像，非0的像素被看成1,0的像素值保持不变，8-bit
                vector_contour, // vector of all contour objects
                hierachy,   // 该图的拓扑结构，可选，该轮廓发现算法正是基于图像拓扑结构实现
                RETR_TREE,  // 轮廓返回模式
                CHAIN_APPROX_SIMPLE, //发现方法
                Point(0, 0)); //轮廓像素的位移 默认(0, 0)没有位移
    // draw all contour objects
    RNG rng(12345); // random seed for color of each contour object
    for (size_t i = 0; i < vector_contour.size(); i++) {
        Scalar color_contour(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255)); // specific color of contour
        drawContours(img_out, //draw contour objects on "img_out"
            vector_contour,   //全部发现的轮廓对象
            i,                //轮廓NO.
            color_contour,    //绘制时的颜色
            2,                //绘制线宽
            8,                //线的类型 LINE_8
            hierachy,         //拓扑结构图
            0,                //最大层数，0只绘制当前，1表示绘制当前及其内嵌的轮廓
            Point(0, 0));     //轮廓位移，可选   
    }
    return;
}

void test() {
    Mat img_in, img_out;
    // read image
    img_in = imread("./coins.jpg");
    if (img_in.empty()) {
        cout << "image not exist" << endl;
    }
    // get contour on "img_out"
    get_contour(img_in, img_out);
    // display "img_in", "img_out"
    namedWindow("img_in", CV_WINDOW_AUTOSIZE);
    imshow("img_in", img_in);
    namedWindow("img_out", CV_WINDOW_AUTOSIZE);
    cout << img_out.size() << endl;
    imshow("img_out", img_out);
    return;
}

int main(){
    test();
    waitKey(0);
    return 0;
}