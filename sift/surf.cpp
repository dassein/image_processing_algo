/**example script for usage of SURF method in opencv
 * note: SURF is the quick implementation of SIFT
 * (Speeded Up Robust Feature)
 * reference: https://zhuanlan.zhihu.com/p/104449009
 **/
// mkdir ./build
// cd ./build
// cmake ..
// make
// make install
// cd ..
// rm -rf ./build
#include<opencv2/opencv.hpp>
#include<opencv2/xfeatures2d.hpp>
using namespace std;
using namespace cv;

void test() {
    Mat img1 = imread("sift_match_1.png");
    Mat img2 = imread("sift_match_2.png");
    if (img1.empty() || img2.empty()) { cout << "image not exists" << endl; }

    // SIFT
    int num_keypoint = 100; // number of key points 
    vector<KeyPoint> keypoints; // each keypoint stores a vector whose 
                                // length = num_hist^2 * num_orientation = 4^2 * 8 = 128
    //Ptr<Feature2D> f2d = SIFT::create(num_keypoint);
    Ptr<Feature2D> f2d = xfeatures2d::SURF::create(num_keypoint);
    //cv::Ptr<Feature2D> f2d = ORB::create(num_keypoint);


    //-- Step 1: Detect the keypoints:
    vector<KeyPoint> keypoints_1, keypoints_2;    
    f2d->detect( img1, keypoints_1 );
    f2d->detect( img2, keypoints_2 );

    //-- Step 2: Calculate descriptors (feature vectors)    
    Mat descriptors_1, descriptors_2;    
    f2d->compute( img1, keypoints_1, descriptors_1 );
    f2d->compute( img2, keypoints_2, descriptors_2 );

    //-- Step 3: Matching descriptor vectors using BFMatcher :
/*     BFMatcher matcher;
    std::vector< DMatch > matches;
    matcher.match( descriptors_1, descriptors_2, matches ); */
    //-- Step 3: Matching descriptor vectors with a FLANN based matcher
    // Since SIFT is a floating-point descriptor NORM_L2 is used
    Ptr<DescriptorMatcher> matcher = DescriptorMatcher::create(DescriptorMatcher::FLANNBASED);
    vector< vector<DMatch> > knn_matches;
    matcher->knnMatch( descriptors_1, descriptors_2, knn_matches, 2 );
    //-- Filter matches using the Lowe's ratio test
    const float ratio_thresh = 0.7f;
    vector<DMatch> good_matches;
    for (size_t i = 0; i < knn_matches.size(); i++)
    {
        if (knn_matches[i][0].distance < ratio_thresh * knn_matches[i][1].distance)
        {
            good_matches.push_back(knn_matches[i][0]);
        }
    }

    //-- save images with keypoints
    Mat img1_keypoint, img2_keypoint;
    drawKeypoints(img1, keypoints, img1_keypoint);
    drawKeypoints(img2, keypoints, img2_keypoint);
    imwrite("surf_match_1+keypoint.png", img1_keypoint);
    imwrite("surf_match_2+keypoint.png", img2_keypoint);

    //-- Draw matches
    Mat img_matches;
    drawMatches( img1, keypoints_1, img2, keypoints_2, good_matches, img_matches, Scalar::all(-1),
                 Scalar::all(-1), vector<char>(), DrawMatchesFlags::NOT_DRAW_SINGLE_POINTS );
    imwrite("surf_match_c++.png", img_matches);
    //-- Show detected matches
    namedWindow("SURF match", CV_WINDOW_AUTOSIZE);
    imshow("SURF Matches", img_matches);
}

int main() {
    test();
    waitKey(0);
    return 0;
}