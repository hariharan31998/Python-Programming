#include <stdio.h>

int main(void) 
{
	char str[30];
	gets(str);
	for(int i=0;str[i]!='\0';i=i+3)
	{
		printf("%c",str[i]);
	}
	return 0;
}
