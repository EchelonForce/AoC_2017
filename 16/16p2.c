#include <stdio.h>  

void gen_next_val( char * buf );
void exchange( char * buf, int a, int b );
void spin( char * buf, int s );
void swap( char * buf, char a, char b );

int main( )  
    {  
    int num_iters = 1000000000;

    char buf [] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', '\0' };
    char bufa [] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', '\0' };
    printf( "input:  %s\n", buf );

    int found_repeat = 0;

    //Just run the dance moves until a repeat of the original pattern occurs.
    for( int i = 0; i< num_iters && found_repeat==0 ; i++ )
        {
        gen_next_val( buf );

        if( i % 1000 == 0 && i !=0 )
            {
            printf( "i = %d\n", i );
            }
        //printf( "result = %s\n", buf );
        
        if( strcmp(buf, bufa) == 0 )
            {
            printf( "repeat at = %d\n", i );
            found_repeat = i; 
            break;
            }
        
        }
 
    // If the pattern repeats, only do the last (remainder) iterations.
    if( found_repeat > 0 )
        {
        int remainder = num_iters%(found_repeat+1);
        printf( "remainder [%d %% %d] =  %d\n", num_iters, found_repeat, remainder );

        for( int i = 0; i< remainder; i++ )
            {
            gen_next_val( buf );
            }
        }

    printf( "output: %s\n", buf );

    return 0;  
    }   

void exchange( char * buf, int a, int b )
    {
    char t = buf[a];
    buf[a] = buf[b];
    buf[b] = t;
    // printf( "result: %s\n", buf );
    }

void spin( char * buf, int s )
    {
    static char temp_buf [17];
    temp_buf[16] = '\0';

    for( int i = 0; i<16; i++ )
        {
        temp_buf[i] = buf[(16-s+i)%16];
        //printf( "temp_buf = %s\n", temp_buf );
        }
    memcpy( buf, temp_buf, 16 );
    }

void swap( char * buf, char a, char b )
    {
    int a_idx = -1;
    int b_idx = -1;
    for( int i =0; i<16; i++ )
        {
        if( buf[i] == a )
            {
            a_idx = i;
            if( b_idx != -1 )
                break;
            }
        if( buf[i] == b )
            {
            b_idx = i;
            if( a_idx != -1 )
                break;
            }
        }
    exchange( buf, a_idx, b_idx );
    }

void gen_next_val( char * buf )
    {
    // Include the generated dance move code. See 16p2_gen_c_code.py
    #include "input.c_code"
    }