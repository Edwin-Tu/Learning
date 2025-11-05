#include <stdio.h>
#include <stdlib.h>

int main(void){
    //initialize vars
    char *first;
    char *last;

    //prompt user to inpur first and last name and use scanf() to store those to the initiliazed vars
    printf("Enter your first name:");
    scanf("%s",&first);
    printf("Enter your last name:");
    scanf("%s",&last);

    //print the welcome message!
    printf("Hello, %s %s!\n",&first,&last);
    free(first);
    free(last);
}