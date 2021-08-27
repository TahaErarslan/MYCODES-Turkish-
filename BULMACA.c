#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*TAHA ERARSLAN
19010011066*/

int main (){
	
	int m,n,a,b,i,j,c;
	int sayac=0;
	char giris[40];
	char *p,*p2;
	int k=0;
	printf("SADECE YUKARIDAN ASSAGI CALISIYOR\n");
	printf(" BOYUT GIRINIZ (mxn)\n Boyut (m) : ");
	scanf("%d",&m);
	printf("\n Boyut (n) : ");
	scanf("%d",&n);
	char dizi[m][n];
	p=&dizi[0][0];	
	p2=&giris[0];
	for(a=0;a<m;a++)
	{
		for(b=0;b<n;b++)
		{
			*(p+a+b*n)= 'A' + rand()%26;
		}
	}
	for(a=0;a<m;a++)
	{
		printf("\n");
		for(b=0;b<n;b++)
		{
				printf(" %c ",*(p+a+b*n));
		}
		printf("\n");
	
		
	}
	printf("\n");
	printf("ARANACAK KELIME : ");		
	scanf("%s",p2);
	int bul=0;
	printf("kelime uzunluk %d\n",strlen(p2));
	//yukardan asaðý arama 
	for (a=0; a<m;a++){
		for (b=0;b<n;b++){
		k=0;
		sayac=0;
	    while(*(p+(a*n+b+k))==*(p2+k)){
		sayac++;
		k++;
	    if(strlen(p2)==sayac){
	    printf("bulundu satir indis: %d, sutun indis %d\n",b,a);
	    bul++;
	    break;
		}
		}
	}
    }
    printf("%d kere bulundu",bul);


	return 0;
}
