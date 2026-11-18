#include<stdio.h>
int main(){
    float a[100];
    int i,n;
    float temp;

    printf("Enter the size of array:");
    scanf("%d",&n);
    printf("Enter the percentage of students:\n");
    for(i=0;i<n;i++){
        printf("Enter the percentage of %d Student:",i+1);
        scanf("%f",&a[i]);

    }
    printf("Unsorted array is :");
    
    for(i=0;i<n;i++){
        printf("%f ",a[i]);
    }
    
    printf("\n");
    for(i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            //Swaping 
            if(a[j]>a[j+1]){
                temp = a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }

    printf("Sorted percentage of students :");
    for(i=0;i<n;i++){
        printf("%.2f ",a[i]);
    }
    
    printf("Top  percentages of students : ");
    printf("\n");
    for(i= n-1;i>=n-5 && i>=0 ;i--){
        printf("Top %d Percentage: %.2f\n", n - i, a[i]);
    }

}

