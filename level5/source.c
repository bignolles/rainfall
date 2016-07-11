void	o(void)
{
	system("/bin/sh");
	_exit(1);
}

void	n(void)
{
	char	buffer[520];

	fgets(buffer, 512, stdin);
	printf(buffer);
	exit(1); // global offset table -> jmp *0x8049838
}

int		main(int argc, char **argv)
{
	n();
}
