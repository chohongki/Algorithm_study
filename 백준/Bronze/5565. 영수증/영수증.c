#include <stdio.h>

int main()
{
	int price,n,i,sum=0;
	scanf("%d",&price);
	for (i=0;i<9;i++)
	{
		scanf("%d",&n);
		sum+=n;
	}
	printf("%d",price-sum);
	return 0;
}
