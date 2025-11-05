#include<stdio.h>
#include<stdlib.h>

int main(void){
    
    //initialize vars
    char first[20];
    char last [20];

    //prompt user to input first and last name and use scanf() to store those to initiliazed vars
    printf("Enter your first neme:");
    scanf("%s",&first);
    printf("Enter your last name");
    scanf("%s",&last);

    //print the welcome message!
    printf("Helllo %s %s!",first,last);
}