#include <stdio.h>
#include <stdlib.h>
#include "ListBaseStack.h"

void StackInit(Stack *stack)
{
    stack->head = NULL;
}
int SIsEmpty(Stack *stack)
{
    if(stack->head == NULL)
    {
        return TRUE;
    }
    return FALSE;
}
void SPush(Stack *stack, int data)
{
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = stack->head;
    stack->head = newNode; // TOP of stack;

}
int SPop(Stack *stack)
{
    if(SIsEmpty(stack))
    {
        printf("Empty stack!\n");
        exit(-1);
    }
    int currentData = stack->head->data;
    Node* currentNode = stack->head;
    stack->head = stack->head->next;
    free(currentNode);
    return currentData;
}
int SPeek(Stack *stack)
{
    if(SIsEmpty(stack))
    {
        printf("Empty stack!\n");
        exit(-1);
    }
    return stack->head->data;
}