void	v()
{
	static int	m = 0;
	char		buff[520];

	fgets(buff, 512, stdin);
	printf(buff);
	if (m == 64)
	{
		fgets("Wait what?!\n", 12, 1, stdout);
		system("/bin/sh");
	}

}

int		main(int argc, char **argv)
{
	v();
}
