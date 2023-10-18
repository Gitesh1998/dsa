#include <iostream>
#include <string>
using namespace std;

#include "video.h"

// constructor
Video::Video(string title, string url, string comment, float length, int rating)
{
    m_title = title;
    m_url = url;
    m_comment = comment;
    m_length = length;
    m_rating = rating;
}

// comparing videos rating and returning boolean value
bool Video::compareRatings(Video *otherVideo)
{
    return this->m_rating < otherVideo->m_rating;
}

// comparing videos rating and returning boolean value
// otherVideo: video object
// return boolean 
bool Video::compareLengths(Video *otherVideo)
{
    return this->m_length > otherVideo->m_length;
}

// comparing videos rating and returning boolean value
// otherVideo: video object
// return boolean
bool Video::compareTitles(Video *otherVideo)
{
    // comparing 2 string lexicographically
    int compareResult = this->m_title.compare(otherVideo->m_title);
    return compareResult > 0;
}

// comparing videos rating and returning boolean value
// otherVideo: video object
// sort: Sort parameter for sorting video object
// return boolean 
bool Video::compare(Video *otherVideo, string sort)
{
    if (sort == "rating")
    {
        return Video::compareRatings(otherVideo);
    }
    else if (sort == "length")
    {
        return Video::compareLengths(otherVideo);
    }
    else if (sort == "title")
    {
        return Video::compareTitles(otherVideo);
    }
    cout << "Incorrect sort string" << endl;
    return -1;
}

// printing video object
// return void 
void Video::print()
{
    string ratingCount = "";
    for (int i = 0; i < m_rating; i++)
    {
        ratingCount += "*";
    }

    cout << m_title << ", " << m_url << ", " << m_comment << ", " << m_length << ", " << ratingCount << endl;
}