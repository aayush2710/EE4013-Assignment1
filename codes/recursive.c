#include <stdio.h>

void recursive(int n) {

    if(n == 0) {
      return;
    }
    long long int Sum = 0;
    for(int i=0;i<7*n;i++){ 
        Sum+=i;
    }
    recursive(n/2);
    recursive(2*n/5);
}

int  main() {
   int i = 12;
   recursive(10);
   return 0;
}