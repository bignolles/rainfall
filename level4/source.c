void	p(char *s)
{
	printf(s);
}

void	n(void)
{
	char		buff[520];
	static int	m = 0;

	fgets(buff, 512, stdin);
	p(buff);
	if (m == 16930116)
		system("/bin/cat /home/user/level5/.pass");
}

int		main(int argc, char **argv)
{
	n();
}
