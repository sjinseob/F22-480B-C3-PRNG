#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char plain[] = "255044462d312e350a25d0d4c5d80a34";
char cypher[] = "d06bf9d0dab8e8ef880660d2af65aa82";
char IV[] = "09080706050403020100A2B2C2D2E2F2";

void main(){
    char key[16]; 
    int idx = 0;
    for(int i = 1523999329; i <= 1523999339; i++){ //the 2 hour window on 2018 04 17 before 23:08:49  //1524006529
        srand(i);
        printf("%d", i);
        //printf("%s", key);
        printf("\n");
        for(int j = 0; j< 16; j++){
            key[j] = rand()%256;
            printf("%.2x", (unsigned char)key[j]);
    }
    // Try the decrypt with the key here
    }
    
}