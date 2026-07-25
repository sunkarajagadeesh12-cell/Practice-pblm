#include<stdio.h>
int main() {
    int num1,num2,sai;
    printf("Enter the values of num1 and num2\n");
    scanf("%d %d",&num1,&num2);
    sai=num1;
    num1=num2;
    num2=sai;
    printf("the value of num1 and num2 is %d %d\n",num1,num2);
    return 0;
}