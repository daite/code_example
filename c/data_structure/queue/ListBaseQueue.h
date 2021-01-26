#ifndef __LB_QUEUE_H__
#define __LB_QUEUE_H__

#define TRUE 1
#define FALSE 0

typedef struct _node 
{
    int data;
    struct _node *next;
} Node;

typedef struct _lQueue 
{
    Node *front;
    Node *rear;
} Queue;

void QueueInit(Queue *q);
int QIsEmpty(Queue *q);

void Enqueue(Queue *q, int data);
int Deque(Queue *q);
int QPeek(Queue *q);

#endif