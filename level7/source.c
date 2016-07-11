#include <stdlib.h>
#include <time.h>
#include <stdio.h>

char	c[80];

void	m(void)
{
	time_t	t;

	t = time(NULL);
	printf("%s - %d\n", c, t);
}

int		main(int argc, char **argv)
{
	void	*ptr1;
	void	*ptr2;
	void	*ptr3;
	void	*ptr4;
	FILE	*f;

	ptr1 = malloc(8);
	((int*)ptr1)[0] = 1;
	ptr2 = malloc(8);
	*(void**)(ptr1 + 4) = ptr2;
	ptr3 = malloc(8);
	((int*)ptr3)[0] = 2;
	ptr4 = malloc(8);
	*(void**)(ptr3 + 4) = ptr4;
	strcpy(ptr1 + 4, argv[1]);
	strcpy(ptr3 + 4, argv[2]);
	f = fopen("/home/user/level8/.pass", "r");
	fgets(c, 68, f);
	puts("~~");
}
