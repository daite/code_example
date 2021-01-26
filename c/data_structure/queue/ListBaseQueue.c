#include <stdio.h>
#include <stdlib.h>
#include "ListBaseQueue.h"

void QueueInit(Queue *q)
{
    q->front = NULL;
    q->rear = NULL;
}
int QIsEmpty(Queue *q)
{
    if(q->front == NULL)
    {
        return TRUE;
    }
    return FALSE;
}

void Enqueue(Queue *q, int data)
{
    Node *newNode = (Node*)malloc(sizeof(Node));
    if(QIsEmpty(q))
    {
        q->front = newNode;
        q->rear = newNode;
    }
    //new node
    newNode->data = data;
    newNode->next = NULL;

    q->rear->next = newNode;
    q->rear = newNode;

}
int Deque(Queue *q)
{
    if(QIsEmpty(q))
    {
        printf("Empty queue...\n");
        exit(-1);
    }
    Node *delNode = q->front;
    int data = q->front->data;
    q->front = q->front->next;
    free(delNode);
    return data;

}
int QPeek(Queue *q)
{
    if(QIsEmpty(q))
    {
        printf("Empty queue...\n");
        exit(-1);
    }
    return q->front->data;
}