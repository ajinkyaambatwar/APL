#include<stdio.h>
#include<math.h>
#define pi 3.1415926535
int main()
{
  float n[1000];
  n[0]=0.2;
  float alpha = pi;
  int k=1;
  float num;
  while(k<1000){
    num = (n[k-1]+alpha)*100;
    int num_temp = num;
    n[k] = num-num_temp;
    k++;
  }
  int i;
  for(i=0;i<1000;i++){
    printf("%d - %.4f \n",i,n[i]);
  }
}
