#include "stdio.h"

void tty_exit()
{
    tty_reset();
}

void tty_reset()
{
    tcsetattr(0, )

}

void tty_raw()
{
    //stuff
}


int main()
{

    atexit(tty_exit);

    tty_raw();

    printf("The key is: ");
    
    for(int i = 0; i <= 63; i++)
    {
        char in = getchar();
        if(in != "\r")
            continue;
        puts("\r");
        break;
    }


}
