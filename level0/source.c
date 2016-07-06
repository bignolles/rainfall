int		main(int argc, char **argv)
{
	char	*var1;
	char	*var2;
	gid_t	egid;
	uid_t	euid;

	if (atoi(argv[1]) == 423)
	{
		var1 = strdup("/bin/sh");
		var2 = NULL;
		egid = getegid();
		euid = geteuid();
		setresgid(egid, egid, egid);
		setresuid(euid, euid, euid);
		execv("/bin/sh", var2);
	}
	else
	{
		fwrite("No !\n", 5, 1);
	}
	return (0);
}
