#include <string.h>
#include <ctype.h>
#include "ListBaseStack.h"

int EvalRPNExp(char exp[])
{
    // 3 2 4 * +;
    int expLen = strlen(exp);
    int idx, op1, op2;
    char value;


    Stack stack;
    StackInit(&stack);

    for(idx=0; idx<expLen; idx++)
    {   
        value = exp[idx];
        if(isdigit(value))
        {
            SPush(&stack, exp[idx] - '0');
        }
        else
        {
            switch (value)
            {
                case '*':
                op2 = SPop(&stack);
                op1 = SPop(&stack);
                SPush(&stack, op1 * op2);
                break;
                case '+':
                op2 = SPop(&stack);
                op1 = SPop(&stack);
                SPush(&stack, op1 + op2);
                break;
                case '-':
                op2 = SPop(&stack);
                op1 = SPop(&stack);
                SPush(&stack, op1 - op2);
                break;
                case '/':
                op2 = SPop(&stack);
                op1 = SPop(&stack);
                SPush(&stack, op1 / op2);
                break;
            }
        }
    }
    return SPop(&stack);
}