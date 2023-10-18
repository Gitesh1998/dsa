#include <iostream>
#include <string>
using namespace std;

#include "dstack.h"

// push node from stack
// input double value
void Dstack::push(double value) {
    if (this->empty()) {
        Node *newNode = new Node(value, this->m_head);
        this->m_head = newNode;
        return;
    }
    this->m_head = new Node(value, this->m_head);
    return;
}

// pop node from stack
// input address of double value
bool Dstack::pop(double &value) {
    if (this->empty()) {
        return false;
    }
    Node *temp = this->m_head;
    this->m_head = this->m_head->m_next;
    value = temp->m_data;
    delete temp;
    return true;
}

// get size of stack
// return size as int
int Dstack::size() {
    int size = 0;
    Node *current = this->m_head;
    while (current != nullptr) {
        current = current->m_next;
        size++;
    }
    return size;
}

// check stack is empty or not
// return true if stack is empty
bool Dstack::empty() {
    if (this->m_head == nullptr) {
        return true;
    }
    return false;
}

// deleting all nodes from stack which created on heap
Dstack::~Dstack() {
    Node *current = this->m_head;
    while (current != nullptr) {
        Node *temp = current;
        current = current->m_next;
        delete temp;
    }
    this->m_head = nullptr;
    return;
}