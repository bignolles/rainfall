class N
{
	private:
		int		_mInt;
		char	_annotation[104]; // obj1 -> 0x0804a00c
	public:
		N(int a)
		{
			this->_mInt = a;
		}
		setAnnotation(char *s)
		{
			memcpy(annotation, s, strlen(s));
		}
};

int		main(int argc, char *argv[])
{
	N	*obj1;
	N	*obj2;

	if (argc <= 1)
		exit(1);
	obj1 = new N(5); // 0x804a008
	obj2 = new N(6); // 0x804a078
	obj1->setAnnotation(argv[1]);
}
