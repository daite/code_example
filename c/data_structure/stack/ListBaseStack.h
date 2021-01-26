#ifndef __LB_STACK_H__
#define __LB_STACK_H__
#define TRUE 1
#define FALSE 0

typedef struct _node 
{
    int data;
    struct _node *next;
} Node;

typedef struct _listStack 
{
    Node *head;
} Stack;

void StackInit(Stack *stack);
int SIsEmpty(Stack *stack);
void SPush(Stack *stack, int data);
int SPop(Stack *stack);
int SPeek(Stack *stack);

#endif