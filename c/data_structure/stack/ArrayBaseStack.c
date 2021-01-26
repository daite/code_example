#include <stdio.h>
#include <stdlib.h>
#include "ArrayBaseStack.h"

void StackInit(Stack *stack)
{
    stack->topIndex = -1;
}
int SISEmpty(Stack *stack)
{
    if(stack->topIndex == -1)
    {
        return TRUE;    
    }
    return FALSE;
}
void SPush(Stack *stack, int data)
{   
    int next = stack->topIndex + 1;
    (stack->stackArr)[next] = data;
    stack->topIndex = next;
}
int SPop(Stack *stack)
{
    if(SISEmpty(stack))
    {
        printf("Empty stack!\n");
        exit(-1);
    }
    int current = stack->topIndex;
    int value = stack->stackArr[current];
    stack->topIndex = current - 1;
    return value;

}
int SPeek(Stack *stack)
{
    if(SISEmpty(stack))
    {
        printf("Empty stack!\n");
        exit(-1);
    }
    int current = stack->topIndex;
    return stack->stackArr[current];
}

