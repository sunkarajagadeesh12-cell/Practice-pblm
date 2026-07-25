#include <stdio.h>
#include <string.h>

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