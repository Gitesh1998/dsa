#ifndef VIDEO_H
#define VIDEO_H

#include <string>
using namespace std;

// class for Video object
class Video
{
    // function which can access by video object
public:
    Video(string title, string url, string comment, float length, int rating);
    bool compareRatings(Video *otherVideo);
    bool compareLengths(Video *otherVideo);
    bool compareTitles(Video *otherVideo);
    bool compare(Video *otherVideo, string sort);
    void print();

    // video object private member
private:
    string m_title;
    string m_url;
    string m_comment;
    float m_length;
    int m_rating;
};

#endif
