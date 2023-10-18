#include <iostream>
#include <string>
using namespace std;

#include "video.h"

const int MAX = 100;

int main()
{
    Video *video[MAX] = {NULL};
    int videoCount = 0;

    // define variable for sorting parameter.
    string sortPara = "";
    getline(cin, sortPara);

    // check sort parameter correct or not.
    if (sortPara == "")
    {
        // if sorting parameter is emtpy then print video array as it is
        for (int i = 0; i < videoCount; i++)
        {
            video[i]->print();
        }
        return 0;
    }
    else if (!(sortPara == "rating" || sortPara == "length" || sortPara == "title"))
    {
        cerr << sortPara << " is not a legal sorting method, giving up." << endl;
        return 1;
    }

    string title;
    string url;
    string comment;
    float length;
    int rating;

    // get video object from user input
    while (getline(cin, title))
    {
        getline(cin, url);
        getline(cin, comment);
        cin >> length;
        cin >> rating;

        // if video object crosses 100 count then return with error
        if (videoCount > 99)
        {
            cerr << "Too many videos, giving up." << endl;
            return 1;
        }

        video[videoCount] = new Video(title, url, comment, length, rating);
        videoCount++;
        cin.ignore();
    }

    // sorting video object according sort parameter
    for (int last = videoCount - 1; last > 0; last--)
    {
        for (int cur = 0; cur < last; cur++)
        {
            // Swap the object pointers in the array.
            if (video[cur]->compare(video[cur + 1], sortPara))
            {
                Video *temp = video[cur];
                video[cur] = video[cur + 1];
                video[cur + 1] = temp;
            }
        }
    }

    // print video object after sorting
    for (int i = 0; i < videoCount; i++)
    {
        video[i]->print();
    }

    // delete alloacted video object
    for (int i = 0; i < videoCount; i++)
    {
        delete video[i];
    }

    // Exit the program with a success status.
    return 0;
}
