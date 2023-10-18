#include <iostream>
using namespace std;

#include "video.h"
#include "vlist.h"

const int MAX = 100;


// Pass vlist object 
// return nothing
void read_input(Vlist vlist)
{

    string cmd = "";
    while (getline(cin, cmd))
    {
        // if cmd is insert then insert in list
        if (cmd == "insert")
        {
            string title, url, comment;
            float length;
            int rating;
            getline(cin, title);
            getline(cin, url);
            getline(cin, comment);
            cin >> length;
            cin >> rating;
            cin.ignore();

            //calling vlist insert function to create object on vlist 
            vlist.insert(vlist, title, url, comment, length, rating);
        }
        else if (cmd == "print")
        {
            // print video objects which present in vlist
            vlist.print(vlist);
        }
        else if (cmd == "length")
        {
            // get length of nodes which present on vlist object
            int len = vlist.length(vlist);
            cout << len << endl;
        }
        else if (cmd == "lookup")
        {
            string searchStr;
            getline(cin, searchStr);
            // call function lookup on nodes of vlist for printing video object
            bool isExist = vlist.lookup(vlist, searchStr);
            // check title exist or not on nodes of vlist
            if (!isExist)
            {
                cerr << "Title <" << searchStr << "> not in list." << endl;
            }
        }
        else if (cmd == "remove")
        {
            string searchStr;
            getline(cin, searchStr);
            // call function remove on nodes of vlist for deleting node object
            bool isExist = vlist.remove(vlist, searchStr);
            // check title exist or not on nodes of vlist for remove
            if (!isExist)
            {
                cerr << "Title <" << searchStr << "> not in list, could not delete." << endl;
            }
        }
        else
        {
            cerr << "<" << cmd << ">" << " is not a legal command, giving up." << endl;
            exit(1);
        }
    }
}

int main()
{
    Vlist vlist;
    read_input(vlist);
    return 0;
}