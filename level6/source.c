void	n(void)
{
	system("/bin/cat /home/user/level7/.pass");
}

void	m(void)
{
	puts("Nope");
}

int		main(int argc, char **argv)
{
	void	*ptr1;
	void	(*ptr2)(void);

	ptr1 = malloc(64);
	ptr2 = malloc(4);
	ptr2 = m;
	strcpy(malloc1, argv[1]);
	ptr2();
}
