#include<opencv2/opencv.hpp>
#include<iostream>
#include<string>
using namespace std;
using namespace cv;

const double PI = 3.1415926;

class LineFinder {
private:
    vector<Vec4i> vector_line; // vector of 被检测直线的端点
    double delta_rho, delta_theta; // resolution parameters of "accumulator"
    int vote_min; // minimal vote number to determine a line
    double len_min; // minimal length of a line
    double gap_max; // maximal gap on a line
public:
    LineFinder() : delta_rho(1), delta_theta(CV_PI / 180), 
                    vote_min(10), len_min(0.), gap_max(0.) { }
    void set_resolution(double d_rho, double d_theta) {
        delta_rho = d_rho; delta_theta = d_theta;
    }
    void set_vote_min(int v_min) { vote_min = v_min; }
    void set_len_gap( double l_min, double g_max ) { 
        len_min = l_min; gap_max = g_max; 
    }
    // find lines with hough transform on binary img
    vector<Vec4i> find_lines(Mat& img_binary) {
        vector_line.clear();
        HoughLinesP(img_binary,  // input binary  image
                    vector_line,// output vector of 被检测直线的端点
                    delta_rho, delta_theta, vote_min, len_min, gap_max); // parameters
        return vector_line;
    }
    // draw lines on image instance
    void draw_lines(Mat& img_instance) {
        Scalar color = Scalar(255, 255, 255); // white color
        vector<Vec4i>::const_iterator iter = vector_line.begin();
        while (iter != vector_line.end()) {
            Point p1( (*iter)[0], (*iter)[1] ); // (x, y) of 1st point
            Point p2( (*iter)[2], (*iter)[3] ); // (x, y) of 2nd point
            line(img_instance, p1, p2, color);  // draw line of p1,p2 on "img_instance" with white color
            iter++;
        }
    }
};

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
    Mat img_contour;
    Canny(img_gray, img_contour, 125, 350); // meaning of 125, 350
    // display contour
    namedWindow("Canny: contour of gray image", CV_WINDOW_AUTOSIZE);
    imshow("Canny: contour of gray image", img_contour);
    // line detection with hough transform
    LineFinder f; // set param of hough transform line detection
    f.set_len_gap(100, 20);
    f.set_vote_min(60);
    vector<Vec4i> v_line = f.find_lines(img_contour);
    // draw lines on original image
    f.draw_lines(img);
    namedWindow("lines with Hough", CV_WINDOW_AUTOSIZE);
    imshow("lines with Hough", img);
    return;
}

int main() {
    test();
    waitKey(0);
    return 0;
}