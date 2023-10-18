#include <iostream>
using namespace std;

#include "pqueue.h"

PQueue::PQueue() {
    n_head = NULL;
}

// enqueue customer according to its priority
void PQueue::enqueue(Cust *cust, int priority)
{
    Node *newNode = new Node(cust, priority, NULL);
    if (!n_head || priority < n_head->n_priority)
    {
        newNode->n_next = n_head;
        n_head = newNode;
    }
    else
    {
        Node *current = n_head;
        while (current->n_next && priority >= current->n_next->n_priority)
        {
            current = current->n_next;
        }
        newNode->n_next = current->n_next;
        current->n_next = newNode;
    }
    return;
}

// dequeue first customer
bool PQueue::dequeue(Cust*& cust)
{
    if (!n_head)
    {
        return false;
    }
    Node *temp = n_head;
    n_head = n_head->n_next;
    cust = temp->n_cust;
    delete temp;
    return true;
}

// check queue is empty or not
bool PQueue::isEmpty()
{
    return n_head == NULL;
}

// get first priority of customer
bool PQueue::getFirstPriority(int &priority)
{
    if (!n_head) return false;
    priority = n_head->n_priority;
    return true;
}

// get size of queue
int PQueue::getSize() {
    int size = 0;
    Node *current = n_head;
    while (current) {
        size++;
        current = current->n_next;
    }
    return size;
}


// print whole queue
void PQueue::print(ostream &os) {
    Node *current = n_head;
    while (current != NULL) {
        current->n_cust->print(os);
        current = current->n_next;
    }
    return;
}

// delete all elements from queue
PQueue::~PQueue()
{
    Cust* cust;
    while (this->n_head)
    {
        dequeue(cust);
    }
}