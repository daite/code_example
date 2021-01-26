#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    char data[10];
    struct node *link;
}node;

typedef struct linkedList {
    node* head;
}linkedList;

//create empty linkedlist
linkedList* createLinkedList(void)
{
    linkedList* l = (linkedList*)malloc(sizeof(linkedList));
    l->head = NULL;
    return l;
}

// free linkedlist
void freelinkedList(linkedList* l)
{
    node* p;
    while(l->head != NULL)
    {
        p = l->head;
        l->head = p->link;
        printf("freed : %s\n", p->data);
        free(p);
        p = NULL;
    }
}

// print linkedlist
void printLinkedList(linkedList* l)
{
    node* p = l->head;
    printf("[");
    while (p != NULL)
    {
        printf("%s", p->data);
        p = p->link;
        if (p != NULL)
        {
            printf(", ");
        }
    }
    printf("]\n");
}

//insert first node
// before: l -> [chris, tom]
//  after: l -> [david, chris, tom]
void insertFirstNode(linkedList* l, char* x)
{
    node* temp;
    node* n = (node*)malloc(sizeof(node));
    temp = l->head;
    l->head = n;
    n->link = temp;
    strcpy(n->data, x);
}

//insert middle node
//insert a new node after pre
void insertMiddleNode(linkedList* l, node* pre, char* x)
{
    node* n = (node*)malloc(sizeof(node));
    strcpy(n->data, x);
    if ((l == NULL) || (pre == NULL))
    {
        l->head = n;
        n->link = NULL;
    }
    else
    {
        node *temp;
        temp = pre->link;
        n->link = temp;
        pre->link = n;
    }
}

//insert last node
void insertLastNode(linkedList* l, char* x)
{   
    node* n = (node*)malloc(sizeof(node));
    strcpy(n->data, x);
    if (l->head == NULL)
    {
        l->head = n;
        n->link = NULL;
    }
    else
    {
        // find which node has null link;
        node* temp;
        temp = l->head;
        while(temp->link != NULL)
        {
            temp = temp->link;
        }
        temp->link = n;
        n->link = NULL;
    }
}

// main function
int main(void)
{
    linkedList* l = createLinkedList();
    node* chris = (node*)malloc(sizeof(node));
    node* tom = (node*)malloc(sizeof(node));

    l->head = chris;
    strcpy(chris->data, "chris");
    chris->link = tom;

    strcpy(tom->data, "tom");
    tom->link = NULL;

    insertFirstNode(l, "david"); // [david,chris,tom]
    insertMiddleNode(l, l->head, "kim"); // [david, kim, chris, tom]
    insertLastNode(l, "julian"); // [david, kim, chris, tom, julian]

    printLinkedList(l);
    freelinkedList(l);
    
    return 0;
}
