#include<stdio.h>
#include<stdlib.h>
#define PIE 3.14

int main(void){
    //initialize variable
    float radius;
    //get user input and store it
    printf("Enter the radius of your circle:");
    scanf("%f",&radius);

    //do the math
    float area;
    area= PIE * (radius*radius);
    printf("The area of your circle is %f",area);
}