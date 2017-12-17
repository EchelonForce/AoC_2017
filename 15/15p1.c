#include <stdio.h>  

#define GEN_A_FACTOR (16807)
#define GEN_B_FACTOR (48271)

#define uint64 unsigned __int64
#define sint64 signed __int64
#define uint32 unsigned __int32
#define sint32 signed __int32
#define uint16 unsigned __int16
#define sint16 signed __int16
#define uint8 unsigned __int8
#define sint8 signed __int8

uint64 gen_next_val( uint64 prev, uint64 factor );

int main()  
    {  
    printf("GEN_A_FACTOR = %d\n", GEN_A_FACTOR);  
    printf("GEN_B_FACTOR = %d\n", GEN_B_FACTOR);  

    uint64 genA_start = 277;
    uint64 genB_start = 349;

    printf("genA_start = %lld\n", genA_start);  
    printf("genB_start = %lld\n", genB_start);  

    uint64 genA_latest = genA_start;
    uint64 genB_latest = genB_start;

    uint64 num_iters = 40000000;
    uint64 matches = 0;

    for( uint64 i = 0; i< num_iters; i++ )
        {
        genA_latest = gen_next_val( genA_latest, GEN_A_FACTOR );
        genB_latest = gen_next_val( genB_latest, GEN_B_FACTOR );
        //printf("i = %lld\n", i);  
        //printf("genA_latest = %lld\n", genA_latest);  
        //printf("genB_latest = %lld\n", genB_latest);  
      

        if( (uint16)genA_latest == (uint16)genB_latest )
            {
            matches++;
            //printf( "matches = %lld", matches );
            }
        }

    printf( "matches = %lld", matches );

    return 0;  
    }   

uint64 gen_next_val( uint64 prev, uint64 factor )
    {
    uint64 next = prev*factor%2147483647;
    return next;
    }
