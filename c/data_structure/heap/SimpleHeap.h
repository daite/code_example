#ifndef __SIMPLE_HEAP_H__
#define __SIMPLE_HEAP_H__

#define TRUE 1
#define FALSE 0

#define HEAP_LEN 100

typedef struct _heaapElem 
{
    char pr;
    int data;
} HeapElem;

typedef struct _heap 
{
    int numOfData;
    HeapElem heapArr[HEAP_LEN];
} Heap;


void HeapInit(Heap* ph);
int HIsEmpty(Heap* ph);
void HInsert(Heap* ph, int data, int pr);
int HDelete(Heap* ph);

#endif
