#include "CircularQueue.h"
#include <stdlib.h>
#include <stdio.h>

void QueueInit(Queue *q)
{
    q->front = 0;
    q->rear = 0;
}
int QIsEmpty(Queue *q)
{
    if(q->front == q->rear)
    {
        return TRUE;
    }
    return FALSE;
}

int NextPosIdx(int pos)
{
    if(pos == QUE_LEN-1)
    {
        return 0;
    }
    return pos + 1;
}

void Enqueue(Queue *q, int data)
{
    if(NextPosIdx(q->rear) == q->front)
    {
        printf("Queue is full\n");
        exit(-1);
    }
    q->rear = NextPosIdx(q->rear);
    q->queArr[q->rear] = data;
}
int Dequeue(Queue *q)
{
    if(QIsEmpty(q))
    {
        printf("Queue is empty\n");
        exit(-1);
    }
    q->front = NextPosIdx(q->front);
    return q->queArr[q->front];
}
int QPeek(Queue *q)
{
    if(QIsEmpty(q))
    {
        printf("Queue is empty\n");
        exit(-1);
    } 
    return q->queArr[NextPosIdx(q->front)];
}