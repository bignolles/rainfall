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
		if (strstr(buff, "reset") == buff) //Idem
		{
			free(*ptr1);
		}
		if (strstr(buff, "service") == buff) //Ditto
		{
			*ptr2 = strdup(buff + 7);
		}
		if (strstr(buff, "login") == buff) //Tout pareil
		{
			if (ptr1[32] != NULL)
			{
				system("/bin/sh");
			}
			else
			{
				fwrite("Password:\n", 10, 1, stdout);
			}
		}
	}
}
