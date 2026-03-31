#include <stdio.h>

int main(){
	int a,b,cnt=0;
	scanf("%d %d",&a,&b);
	printf("%d.",a/b);
	a%=b;
	while(a!=0){
		a*=10;
		printf("%d",a/b);
		a%=b;
		cnt++;
		if(cnt>=32)break;
	}
	return 0;
}