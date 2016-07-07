void	p(void)
{
	char	*s;
	void	*return_addr;

	fflush(stdout);
	gets(s);
	return_addr = __builtin_return_address(0);
	if ((return_addr & 0xb0000000) != 0)
	{
		printf("%p\n", return_addr);
		exit(1);
	}
	puts(s, stdout);
	strdup(s);
}

int		main(int argc, char **argv)
{
	p();
}
