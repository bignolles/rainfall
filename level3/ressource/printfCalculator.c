#include <inttypes.h>
#include <stdio.h>
#include <string.h>

int		main(int argc, char **argv)
{
	char	s1[5];
	char	s2[5];
	long	val1;
	long	val2;

	if (argc == 2 && strlen(argv[1]) == 8)
	{
		strncpy(s1, argv[1], 4);
		strncpy(s2, argv[1] + 4, 4);
		s1[4] = '\0';
		s2[4] = '\0';
		val1 = strtol(s1, NULL, 16);
		val2 = strtol(s2, NULL, 16);
		if (val1 > val2)
		{
			printf("part2: %ld / %ld\npart1: %ld\n", val2, val2 - 8, val1 - val2);
		}
		else
		{	
			printf("part1: %ld / %ld\npart2: %ld\n", val1, val1 - 8, val2 - val1);
		}
	}
	return (0);
}
