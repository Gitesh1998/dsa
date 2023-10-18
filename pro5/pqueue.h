#ifndef PQUEUE_H
#define PQUEUE_H

#include "cust.h"

class PQueue
{
public:
    PQueue();
    void enqueue(Cust *cust, int priority);
    bool dequeue(Cust*& cust);
    bool isEmpty();
    bool getFirstPriority(int &priority);
    int getSize();
    void print(ostream &os);
    ~PQueue();

private:
private:
    class Node
    {
    public:
        Node(Cust *cust, int priority, Node *next)
        {
            n_cust = cust;
            n_priority = priority;
            n_next = next;
        }
        Cust *n_cust;
        int n_priority;
        Node *n_next;
    };
    Node *n_head;
};

#endif
