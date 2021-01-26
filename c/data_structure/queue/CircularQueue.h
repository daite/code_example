#ifndef __C_QUEUE_H__
#define __C_QUEUE_H__

#define TRUE 1
#define FALSE 0
#define QUE_LEN 100

typedef struct _cQueue 
{
    int front;
    int rear;
    int queArr[QUE_LEN];
}Queue;

void QueueInit(Queue *q);
int QIsEmpty(Queue *q);

void Enqueue(Queue *q, int data);
int Dequeue(Queue *q);
int QPeek(Queue *q);

#endif
