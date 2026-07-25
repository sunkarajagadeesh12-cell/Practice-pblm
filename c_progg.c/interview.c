//1)

// #include<stdio.h>
// int main() {
// int x = printf("Hello"); //printf always return the number of character in the program
// printf("%d",x);
// return 0;
// }
//therefore  it will return the number of character which is 5

#include<stdio.h>
int main() {
int total = 0, i;
for(i = 1 ; i<=365 ; i++) {
    total =  total + i;
}
printf("%d",total);

return 0;

}

/*
#include <stdio.h>

int main() {

    int total = 0, i;

    for(i = 1; i <= 365; i++) {
        total = total + i;
    }

    printf("%d", total);

    return 0;
}
    */