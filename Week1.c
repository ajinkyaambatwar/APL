#include<stdio.h>

int main()
{
  int n=1;
  int nold=1;
  printf("1,%d\n",n );
  printf("2,%d\n",nold );
  int k=3;
  int new;
  while(k<11){
    new=n+nold;
    nold=n;
    n=new;
    printf("%d, %d\n",k,new);
    k++;
  }


}
