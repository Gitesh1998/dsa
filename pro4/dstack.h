#ifndef DSTACK_H
#define DSTACK_H

class Dstack
{
public:
    Dstack() { m_head = nullptr; }
    void push(double value);
    bool pop(double &value);
    int size();
    bool empty();
    ~Dstack();

private:
    class Node
    {
    public:
        Node(double data, Node *next)
        {
            this->m_data = data;
            this->m_next = next;
        }
        Node *m_next;
        double m_data;
        int size = 0;
    };
    Node *m_head;
};

#endif