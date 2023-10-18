#include <iostream>
#include <string>
using namespace std;

const int MAX = 100;

#include "vlist.h"

// Insert video object with node on vlist
// Inputs are vlist address, title string, url string, comment string, length float, rating integer 
void Vlist::insert(Vlist &vlist, string title, string url, string comment, float length, int rating)
{
    Video *video = new Video(title, url, comment, length, rating);

    // if head is null then created new node object and assign to head
    if (vlist.m_head == NULL)
    {
        vlist.m_head = new Node(video, NULL);
        return;
    }
    Node *current = vlist.m_head;

    // if title alphabetically comes before head then insert on head.
    if ((current->m_video->getTitle().compare(title)) > 0)
    {
        Node *newNode = new Node(video, vlist.m_head);
        vlist.m_head = newNode;
        return;
    }
    else if (current->m_next == NULL && !((current->m_video->getTitle().compare(title)) != 0))
    {
        Node *newNode = new Node(video, NULL);
        vlist.m_head->m_next = newNode;
        return;
    }

    // insert newly created video object on correct alphabetically order
    while (current->m_next != NULL)
    {
        if ((current->m_next->m_video->getTitle().compare(title)) > 0)
        {
            if ((current->m_next->m_video->getTitle().compare(title)) == 0) return;
            Node *newNode = new Node(video, NULL);
            newNode->m_next = current->m_next;
            current->m_next = newNode;
            return;
        }
        current = current->m_next;
    }

    // if title alphabetically comes before at the end of vlist then insert at end.
    Node *newNode = new Node(video, NULL);
    current->m_next = newNode;
    return;
}


// Print video object which present on vlist.
// input vlist address
void Vlist::print(Vlist &vlist)
{
    Node *current = vlist.m_head;
    // traverse through nodes and print video object
    while (current != NULL)
    {
        current->m_video->print();
        current = current->m_next;
    }
    return;
}

// Get length of nodes which exist on vlist
// Input vlist address
// Return length of total nodes which present on vlist as integer
int Vlist::length(Vlist &vlist)
{
    int len = 0;
    Node *current = vlist.m_head;
    // traverse through nodes and count length
    while (current != NULL)
    {
        len++;
        current = current->m_next;
    }
    return len;
}

// Search nodes whose video's title match with searchStr
// Input vlist address and searchStr as string for searching title
// Return true or false according to result
bool Vlist::lookup(Vlist &vlist, string searchStr)
{
    Node *current = vlist.m_head;

    // traverse through nodes for searching node
    while (current != NULL)
    {
        if (current->m_video->getTitle() == searchStr)
        {
            current->m_video->print();
            return true;
        }
        current = current->m_next;
    }
    return false;
}

// Remove nodes whose video's title match with searchStr
// Input vlist address and searchStr as string for searching title
// return true or false according to result
bool Vlist::remove(Vlist &vlist, string searchStr)
{
    Node *current = vlist.m_head;
    // check if vlist is empty 
    if (current == NULL)
    {
        return false;
    }

    // check if searchStr present on head
    if (current->m_video->getTitle() == searchStr)
    {
        Node *temp = current;
        m_head = current->m_next;
        delete temp;
        return true;
    }

    // remove node whose title matches with searchStr
    // traverse through nodes for removing object
    while (current->m_next != NULL)
    {
        if (current->m_next->m_video->getTitle() == searchStr)
        {
            Node *temp = current->m_next;
            current->m_next = current->m_next->m_next;
            delete temp;
            return true;
        }
        current = current->m_next;
    }

    return false;
}


// Destructor for vlist object
Vlist::~Vlist() {
    Node *current = this->m_head;
    while (current != NULL) {
        Node *temp = current;
        current = current->m_next;
        delete temp->m_video;
        delete temp;
    }
    this->m_head = NULL;
    return;
}