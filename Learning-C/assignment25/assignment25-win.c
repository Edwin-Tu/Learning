#include <stdio.h>
#include <io.h>
#include <sys/stat.h>
#include <fcntl.h>

int main (void){
    int filedescriptor;

    filedescriptor = open("testfile.txt",O_WRONLY| O_CREAT, _S_IREAD | _S_IWRITE);

    if (filedescriptor < 0){
        printf("The open operation failed...");
        return -1;
    }else{
        ("The ipen operation succeeded!");
    }

    int writertn;

    writertn = write(filedescriptor, "Writing test data to the file",30);

    if(writertn != 30){
        printf("The write operation failed...");
        return -1;
    }else{
        printf("The write operation succeeded!");
    }

    if(close(filedescriptor) != 0){
        printf("The close operation failed...");
        return -1;
    }

    return 0;
}