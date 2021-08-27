#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define giris 8
// TAHA ERARSLAN 19010011066



int main(){

	int s,k,a;
	int yildiz,bosluk;
	bosluk=giris-1;

	yildiz=1;
	bosluk=giris;

    //T HARFI
    
	for(a=0;a<giris;a++)
	{
		printf(" *");
	}
	printf("\n");
	for(k=0;k<giris;k++){
	
		for(s=0;s<bosluk;s++){
			printf(" ");
		
		}	
		for(s=0;s<yildiz;s++){
			printf("*");
		}
		printf("\n");
	
		}
    printf("\n");
	printf("\n");
	//A HARFI

    for(a=0; giris>a; a++)
    {
        for(k=0; giris>k; k++)
        {
            if(a==0)
            {
                printf(" *");
            }
            else if(a==giris/2)
            {
                printf(" *");
            }
            else
            {
                if(k==0 || k==giris-1)
                {
                    printf(" *");
                }
                else
                {
                    printf("  ");
                }
            }
        }
        printf("\n");
    }
    printf("\n");
	printf("\n");
    //H HARFI

    for(a=0; giris>a; a++)
    {
        for(k=0; giris>k; k++)
        {
        	if(a==giris/2)
            {
                printf(" *");
            }
            else
            {
                if(k==0 || k==giris-1)
                {
                    printf(" *");
                }
                else
                {
                    printf("  ");
                }
            }
        }
        printf("\n");
    }
    printf("\n");
    printf("\n");
    //A HARFI

    for(a=0; giris>a; a++)
    {
        for(k=0; giris>k; k++)
        {
            if(a==0)
            {
                printf(" *");
            }
            else if(a==giris/2)
            {
                printf(" *");
            }
            else
            {
                if(k==0 || k==giris-1)
                {
                    printf(" *");
                }
                else
                {
                    printf("  ");
                }
            }
        }
        printf("\n");
    }
    printf("\n");
    printf("\n");
	    //E
	for(a=0; giris>a; a++)
    {
        for(k=0; giris>k; k++)
        {
            if(a==0)
            {
                printf(" *");
            }
            else 	if(a==giris-1)
            {
                printf(" *");
            }
			else if(a==giris/2)
            {
                printf(" *");
            }
            else
            {
                if(k==0 || k==(giris-1)+3)
                {
                    printf(" *");
                }
                else
                {
                    printf("  ");
                }
            }
		
		}
        printf("\n");
    }
    printf("\n");
	printf("\n");
	
		//R HARFI

    for(a=0; giris>a; a++)
    {
        for(k=0; giris>k; k++)
        {
            if(a==0)
            {
                printf(" *");
            }
            else if(a==giris/2)
            {
                printf("* ");
            }
            else
		    {
                if(k==0 || k==giris-1)
                {
                    printf(" *");
                }
                else
                {
                    printf("  ");
                }
            }
        }
        printf("\n");
    }
    printf("\n");
	printf("\n");
			//A HARFI

    for(a=0; giris>a; a++)
    {
        for(k=0; giris>k; k++)
        {
            if(a==0)
            {
                printf(" *");
            }
            else if(a==giris/2)
            {
                printf(" *");
            }
            else
            {
                if(k==0 || k==giris-1)
                {
                    printf(" *");
                }
                else
                {
                    printf("  ");
                }
            }
        }
        printf("\n");
    }
    printf("\n");
	printf("\n");
			//R HARFI

    for(a=0; giris>a; a++)
    {
        for(k=0; giris>k; k++)
        {
            if(a==0)
            {
                printf(" *");
            }
            else if(a==(giris/2))
            {
                printf("* ");
            }
            else
            {
                if(k==0 || k==giris-1)
                {
                    printf(" *");
                }
                else
                {
                    printf("  ");
                }
            }
        }
        printf("\n");
    }
    printf("\n");
	printf("\n");
	
	
		// S HARFI

 for(a=1;a<=(giris*2)-1;a++)
 {
     for(k=1;k<=giris+2;k++)
     {
         if((a==1 && (k!=1 && k!=giris+2)) || ((a==giris && (1<k && k!=giris+2)) ) || (a==(giris*2)-1 && (1<k && k!=giris+2)) || (a!=1 && (a<giris && k<2)) || (giris<a && a<(giris*2)-1) && k==giris+2)
         {
             printf(" *");
         }
         else
            printf("  ");
     }
     printf("\n");
 }

printf("\n");
printf("\n");		
	//L HARFI
    for(a=0; a<giris; a++)
    {
        for(k=0; k<giris+1; k++)
        {
            if(k==0)
            {
                printf(" *");
                printf("\n");
            }
            else if(a==giris-1)
            {
                printf(" *");
            }
        }
    }
    printf("\n");
	printf("\n");
			//A HARFI

    for(a=0; giris>a; a++)
    {
        for(k=0; giris>k; k++)
        {
            if(a==0)
            {
                printf(" *");
            }
            else if(a==giris/2)
            {
                printf(" *");
            }
            else
            {
                if(k==0 || k==giris-1)
                {
                    printf(" *");
                }
                else
                {
                    printf("  ");
                }
            }
        }
        printf("\n");
    }
    printf("\n");
	printf("\n");	
	
	//N
    for(a=0; a<giris; a++)
    {
        for(k=0; k<giris; k++)
        {
            if(k==0)
            {
                printf(" *");

            }
            else if(k==giris-1)
            {
                printf(" *");

            }
            else
            {
                if(a==k)
                {
                    printf(" *");
                }
                else
                {
                    printf("  ");
                }
            }
        }
        printf("\n");
    }
    printf("\n");
    
    

    return 0;
    
}
