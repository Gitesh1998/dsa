#ifndef VLIST_H
#define VLIST_H

#include "video.h"

class Vlist {
public:
  Vlist() { m_head = NULL; }
  void insert(Vlist &vlist, string title, string url, string comment, float length, int rating);
  void print(Vlist &vlist);
  int length(Vlist &vlist); 
  bool lookup(Vlist &vlist, string searchStr);
  bool remove(Vlist &vlist, string searchStr);
  ~Vlist();

private:
  class Node {
  public:
    Node(Video *video, Node *next) { m_video = video; m_next = next; }
    Video *m_video;
    Node *m_next;
  };
  Node *m_head;
};
#endif
