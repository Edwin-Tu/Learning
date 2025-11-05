#include <stdio.h>
#include <io.h>
#include <sys/stat.h>
#include <fcntl.h>

int main (void){
    int filedescriptor;

    filedescriptor = open("estfile.txt",O_WRONLY | O_CREAT, _S_IREAD | _S_IWRITE);

    if (filedescriptor < 0){
        printf("The open operation failed...");
        return -1;
    }else{
        printf("The open operation succeeded!");
        return 0;
    }
}