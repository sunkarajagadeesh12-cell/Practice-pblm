#include <stdio.h>
/*#include <string.h>

struct Student {
    char name[100];
    int roll;
};

int main() {
    struct Student s[5];

    printf("Enter details of 5 students:\n\n");

    for(int i = 0; i < 5; i++) {

        printf("Enter full name of student %d: ", i + 1);
        fflush(stdin);                  
        fgets(s[i].name, 100, stdin);    // read full name
        s[i].name[strcspn(s[i].name, "\n")] = '\0'; 
        printf("Enter roll number of student %d: ", i + 1);
        scanf("%d", &s[i].roll);
        getchar();  

        printf("\n");
    }

    printf("\n----- Student List -----\n\n");
    for(int i = 0; i < 5; i++) {
        printf("Student %d -> Name: %s | Roll No: %d\n",
               i + 1, s[i].name, s[i].roll);
    }

    return 0;
}
*/
/*int main() {
    int num1,num2,sai;
    printf("Enter the values of num1 and num2\n");
    scanf("%d %d",&num1,&num2);
    sai=num1;
    num1=num2;
    num2=sai;
    printf("the value of num1 and num2 is %d %d\n",num1,num2);
    return 0;
}*/

/*#include <stdio.h>

int main() {
    int num,i;
    int fact;
    printf("Enter a number: ");
    scanf("%d", &num);

    for(i=1;i<=num;i++){
     fact= fact*i;
    }
    printf("factorial of %d = %lld\n,fact,num");
return 0;
*/
/*#include <stdio.h>

int main() {
int  n,t,r,s = 0;
printf("enter the value of n:");
scanf("%d",&n);
t = n;
while(t) {
    r = t % 10;
    s += r *r *r;
    t /= 10;
}
if(s==n) {
    printf("it is an amstrong value");
}
else {
 printf("it is not an amstrong value");
}
return 0;
}
*/
/*int main() {
    int n, t, r, s = 0;
    scanf("%d", &n);
    t = n;
    while (t) {
        r = t % 10;
        s += r * r * r;
        t /= 10;
    }
    if (s == n) printf("Armstrong");
    else printf("Not Armstrong");
    return 0;
}
*/
/*#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "hello";
    char str2[] = "hello";
    printf("%d\n",strcmp(str1,str2));
    return 0;
}*/
/*#include <stdio.h>
int factorial(int n){
    if(n==0){
        return 1;
    }
    else {
        return n*factorial(n-1);
    } 
}
    int main() {

        int num = 5;
        printf("The factorial is %d",factorial(num));
        return 0;
    }
*/
/*#include <stdio.h>

int main() {
    int a[2][2], b[2][2], c[2][2], i, j;

    printf("Enter elements of first matrix:\n");
    for(i=0;i<2;i++)
        for(j=0;j<2;j++)
            scanf("%d",&a[i][j]);

    printf("Enter elements of second matrix:\n");
    for(i=0;i<2;i++)
        for(j=0;j<2;j++)
            scanf("%d",&b[i][j]);

    for(i=0;i<2;i++)
        for(j=0;j<2;j++)
            c[i][j]=a[i][j]+b[i][j];

    printf("Sum of matrices:\n");
    for(i=0;i<2;i++){
        for(j=0;j<2;j++)
            printf("%d ",c[i][j]);
        printf("\n");
    }
    return 0;
}
*/
/*#include <stdio.h>

int main() {
    int a[10], n, i, max;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter array elements:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);

    max = a[0];
    for(i = 1; i < n; i++)
        if(a[i] > max)
            max = a[i];

    printf("Largest element = %d", max);
    return 0;
}
*/
/*#include <stdio.h>

int main() {
    char str[100];
    int i, count = 0;

    printf("Enter a string: ");
    fgets(str, 100, stdin);

    for(i = 0; str[i] != '\0'; i++) {
        if(str[i] == ' ')
            count++;
    }

    printf("Number of spaces = %d", count);
    return 0;
}
*/
#include <stdio.h>

int main() {
    int a[5], i, sum = 0;

    printf("Enter 5 elements:\n");
    for(i = 0; i < 5; i++)
        scanf("%d", &a[i]);

    for(i = 0; i < 5; i++)
        sum += a[i];

    printf("Sum = %d", sum);
    return 0;
}
