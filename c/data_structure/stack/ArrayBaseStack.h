#ifndef __AB_STACK_H__
#define __AB_STACK_H__

#define TRUE 1
#define FALSE 0
#define STACK_LEN 100

typedef struct _arraystack 
{
    int stackArr[STACK_LEN];
    int topIndex;
} Stack;

void StackInit(Stack *stack);
int SISEmpty(Stack *stack);
void SPush(Stack *stack, int data);
int SPop(Stack *stack);
int SPeek(Stack *stack);
#endif