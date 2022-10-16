#include <stdio.h>
#include <stdlib.h>
#define LEN 32 // 128 bits

int main(){
    unsigned char *key = (unsigned char *) malloc(sizeof (unsigned char)* LEN);
    FILE* numbers = fopen("task5_nums.txt","w+");
    FILE* random = fopen("/dev/urandom", "r");
    fread(key, sizeof(unsigned char)*LEN, 1, random);
    fwrite(key, sizeof(unsigned char)*LEN, 1, numbers);
    fclose(random);
    fclose(numbers);
}
