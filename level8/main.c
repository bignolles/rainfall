int	main()
{
	void	**ptr1;
	void	**ptr2;
	char	buff[BUFF_SIZE + 1];

	while (fgets(buff, 128, stdin))
	{
		printf("%p, %p\n", *ptr1, *ptr2);
		if (strstr(buff, "auth ") == buff) //Pas un vrai strstr, mais vous m'avez compris
		{
			*ptr1 = malloc(4);
			if (strlen(buff + 5) <= 30) //pas un vrai strlen
			{
				strcpy(*ptr1, buff + 5);
			}
		}
		if (strstr(buff, "reset") == buff)
		{
			free(*ptr1);
		}
		if (strstr(buff, "service") == buff)
		{
			*ptr2 = strdup(buff + 7);
		}
		if (strstr(buff, "login") == buff)
		{
			if (ptr1[32] == NULL)
			{
				system("/bin/sh");
			}
		}
	}
}
