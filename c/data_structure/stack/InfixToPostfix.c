#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "ListBaseStack.h"

int GetOpPriority(char op)
{
    switch(op)
    {
        case '*':
        case '/':
            return 5;
        case '+':
        case '-':
            return 3;
        case '(':
            return 1;
    }
    return -1;
}

int ComparePriorityOp(char op1, char op2)
{
    int op1Pri = GetOpPriority(op1);
    int op2Pri = GetOpPriority(op2);
    if(op1Pri > op2Pri)
    {
        return 1;
    }
    else if(op1Pri < op2Pri)
    {
        return -1;
    }
    return 0;   
}

void ConvToRPNExp(char exp[])
{
    Stack stack;
    int expLen = strlen(exp);
    char *convExp = (char*)malloc(expLen);
    int i, idx = 0;
    char tok, popOp;

    memset(convExp, 0, sizeof(char)*expLen);
    StackInit(&stack);

    for(i=0; i<expLen; i++)
    {
        tok = exp[i];
        if(isdigit(tok))
        {
            convExp[idx++] = tok;
        }
        else
        {
            switch(tok)
            {
                case '(':
                    SPush(&stack, tok);
                    break;
                case ')':
                    while(1)
                    {
                        popOp = SPop(&stack);
                        if(popOp == '(')
                            break;
                        convExp[idx++] = popOp;
                    }
                    break;
                case '+': case '-':
                case '*': case '/':
                    while(!SIsEmpty(&stack) && 
                    ComparePriorityOp(SPeek(&stack), tok) >= 0)
                    convExp[idx++] = SPop(&stack);
                    SPush(&stack, tok);
                    break;
            }
        } 
    }
    while(!SIsEmpty(&stack))
        convExp[idx++] = SPop(&stack);
    strcpy(exp, convExp);
    free(convExp);
}