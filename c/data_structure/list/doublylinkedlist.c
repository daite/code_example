#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    struct node *llink;
    char data[10];
    struct node *rlink;
}node;

typedef struct dlinkedList{
    node* head;
}dlinkedList;

dlinkedList* createdlinkedList(void)
{
    dlinkedList* l = (dlinkedList*)malloc(sizeof(dlinkedList));
    l->head = NULL;
    return l;
}

void printList(dlinkedList* l)
{
    printf("[");
    node* n = l->head;
    while(n != NULL)
    {
        printf("%s", n->data);
        n = n->rlink;
        if (n != NULL) printf(",");
    }
    printf("]\n");
}

void freeList(dlinkedList* l)
{
    if (l == NULL) return;
    else
    {
       while(l->head != NULL)
       {
           free(l->head);
           printf("freed %s\n", l->head->data);
           l->head = l->head->rlink;
       }
    }
}

void insertNode(dlinkedList* l, node* pre, char* x)
{
    node* p = (node*)malloc(sizeof(node));
    strcpy(p->data, x);
    if (l->head == NULL)
    {
        p->llink = NULL;
        p->rlink = NULL;
        l->head = p;
    }
    else
    {
        p->rlink = pre->rlink;
        p->llink = pre;
        pre->rlink = p;
        if(p->rlink != NULL)
        {
            p->rlink->llink = p;  
        }
    }
}

void deleteNode(dlinkedList* l, node* p)
{
    if(l->head == NULL) return;
    else if (p == NULL) return;
    else
    {
        p->llink->rlink = p->rlink;
        p->rlink->llink = p->llink;
        free(p);
    }
}

node* searchNode(dlinkedList* l, char* x)
{
    node* temp;
    temp = l->head;
    while(temp != NULL)
    {
        if(strcmp(temp->data, x) == 0) return temp;
        else
        {
            temp = temp->rlink;
        }
    }
    return temp;
}

int main(void)
{
    dlinkedList* l = createdlinkedList();
    node* chris = (node*)malloc(sizeof(node));
    l->head = chris;
    strcpy(chris->data, "chris");
    chris->llink = NULL;

    node* tom = (node*)malloc(sizeof(node));
    strcpy(tom->data, "tom");
    chris->rlink = tom;
    tom->llink = chris;

    node* julian = (node*)malloc(sizeof(node));
    strcpy(julian->data, "julian");
    tom->rlink = julian;
    julian->llink = tom;
    julian->rlink = NULL;

    printList(l);
    node *p = searchNode(l, "tom");
    insertNode(l, p, "john");
    printList(l);
    deleteNode(l, searchNode(l, "john"));
    printList(l);
    freeList(l);

    return 0;
}
