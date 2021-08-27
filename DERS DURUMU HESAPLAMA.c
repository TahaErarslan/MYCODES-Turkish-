#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Dersler
{

	char ders[50];
	float vizenotu;
	float finalnotu;

}dersler;
typedef struct Ogrenci
{
	int numara;
	char ad[50];
	char soyad[50];
	int derssay;
dersler *dersler;
}ogrenciler,*ogrenci;




void DurumGoster(int ogrencisay,struct Ogrenci *n){
	float toplam=0;
	int i,k;

	for(k=0;k<ogrencisay;k++){

		printf("%d. OGRENCI\n %d %s %s \n",k+1,(n+k)->numara,(n+k)->ad,(n+k)->soyad);
for(i=0;i<(n+k)->derssay;i++)
{
	toplam=(((n+k)->dersler+i)->vizenotu)*0.4+(((n+k)->dersler+i)->finalnotu)*0.6;
	if(toplam<60)
	{
		printf("%s DERSINDEN KALDINIZ NOTUNUZ : %.2f \n",((n+k)->dersler+i)->ders,toplam);
			toplam=0;}
	else
	{
			printf("%s DERSINDEN GECTINIZ NOTUNUZ : %.2f \n",((n+k)->dersler+i)->ders,toplam);
	toplam=0;}



}

}

}

void Listele(struct Ogrenci *a,int b)
{
	int j,i;
for(j=0;j<b;j++){
printf("%d %s %s\n",(a+j)->numara,(a+j)->ad,(a+j)->soyad);
for(i=0;i<(a+j)->derssay;i++){
printf("DERS : %s VIZE NOTU : %.2f FINAL NOTU : %.2f\n",((a+j)->dersler+i)->ders,((a+j)->dersler+i)->vizenotu,((a+j)->dersler+i)->finalnotu);

}
}
}

int main() {
int ogrencisay,i,j,k,o,l;

printf("GIRILECEK OGRENCI SAYISI : ");
scanf("%d", &ogrencisay);
ogrenciler *ogrenci=(ogrenciler*)malloc(ogrencisay*sizeof(ogrenciler));
for(i=0;i<ogrencisay;i++){

	printf("%d .OGRENCI BILGILERI  \n",i+1);
	printf("NUMARA,AD,SOYAD : ");
	scanf("%d %s %s",&(ogrenci+i)->numara,(ogrenci+i)->ad,(ogrenci+i)->soyad);

	printf("%d .OGRENCI DERS BILGILERI \n",i+1);
	printf("DERS SAYISINI GIRINIZ : \n");
	scanf("%d",&(ogrenci+i)->derssay);
	(ogrenci+i)->dersler=(dersler*)malloc((ogrenci+i)->derssay*sizeof(dersler));

	for(j=0;j<(ogrenci+i)->derssay;j++)
	{

	printf("DERS ADI,VIZE NOTU,FINAL NOTU : ");
	scanf("%s %f %f",((ogrenci+i)->dersler+j)->ders,&((ogrenci+i)->dersler+j)->vizenotu,&((ogrenci+i)->dersler+j)->finalnotu);


	}
}
printf("MENU : \n 1. DURUM GOSTER\n 2. LISTELE\n 3. CIKIS\n ");
scanf("%d",&k);

while(k!=3){

switch(k){

case(1):


DurumGoster(ogrencisay,ogrenci);
printf("\n");

break;
case (2):
Listele(ogrenci,ogrencisay);
printf("\n");
break;


}
printf("MENU : \n 1. DURUM GOSTER\n 2. LISTELE\n 3. CIKIS\n ");
scanf("%d",&k);
}
return 0;
}
