#include <string.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    char data[10];
    struct node *link;
}node;

typedef struct clinkedList {
    node* head;
}clinkedList;

clinkedList* createcList(void)
{
    clinkedList* l = (clinkedList*)malloc(sizeof(clinkedList));
    l->head = NULL;
    return l;
}

void insertFirstNode(clinkedList* l, char* x)
{
    node* n = (node*)malloc(sizeof(node));
    strcpy(n->data, x);
    if(l->head == NULL)
    {
       l->head = n;
       n->link = l->head;
    }
    else
    {
        node* temp = l->head;
        while(temp->link != l->head)
        {
            temp = temp->link;
        }
        temp->link = n;
        n->link = l->head;
        l->head = n;
    }
}

void deleteNode(clinkedList* l, node* n)
{
    if (l->head == NULL) return;
    else if (n == NULL) return;
    else
    {   
        node* temp = l->head;
        while(temp->link != n)
        {
            temp = temp->link;
        }
        temp->link = n->link;
        if (n == l->head)
        {
            l->head = n->link;
        }
        free(n);
    }
}

// insert node after pre;
void insertNodeToMiddle(clinkedList*l, node* pre, char* x)
{
    node* n = (node*)malloc(sizeof(node));
    strcpy(n->data, x);
    if(l == NULL)
    {
        l->head = n;
        n->link = n;
    }
    else
    {
        n->link = pre->link;
        pre->link = n;
    }

}

void freecList(clinkedList* l)
{
    node* temp = l->head;
    if (temp == NULL) return;
    do {
        free(temp);
        printf("freed %s\n", temp->data);
        temp = temp->link;
    }while(temp != l->head);
}

void printcList(clinkedList* l)
{
    node* temp = l->head;
    printf("[");
    do{
        printf("%s", temp->data);
        temp = temp->link;
        if (temp != l->head) printf(", ");
    }while(temp != l->head);
    printf("]\n");
}

int main(void)
{
    clinkedList* l = createcList();
    insertFirstNode(l, "tom");
    insertFirstNode(l, "julian");
    insertFirstNode(l, "chris");
    printcList(l); // [chris, julian, tom]
    deleteNode(l, l->head); 
    printcList(l); // [julian, tom]
    insertNodeToMiddle(l, l->head, "john");
    printcList(l); // [julian, john, tom]
    freecList(l);
    return 0;
}


