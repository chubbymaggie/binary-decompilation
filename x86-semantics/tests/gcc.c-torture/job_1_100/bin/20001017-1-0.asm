strchr:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	nop
	movq	-8(%rbp), %rax
	movzbl	(%rax), %edx
	movl	-12(%rbp), %eax
	cmpb	%al, %dl
	je	L6
	movq	-8(%rbp), %rax
	leaq	1(%rax), %rdx
	movq	%rdx, -8(%rbp)
	movzbl	(%rax), %eax
	testb	%al, %al
	jne	L3
	movl	$0, %eax
	jmp	L1
L3:
	movq	-8(%rbp), %rax
	jmp	L1
L6:
L1:
	popq	%rbp
	ret
exit:
	pushq	%rbp
	movq	%rsp, %rbp
	movl	%edi, -4(%rbp)
	movq $-1, %rax
	jmp %rax
	
	popq	%rbp
	ret
abort:
	pushq	%rbp
	movq	%rsp, %rbp
	movq $-1, %rax
	jmp %rax
	
	popq	%rbp
	ret
bug:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$48, %rsp
	movq	%rdi, -8(%rbp)
	movl	%esi, %eax
	movl	%edx, -16(%rbp)
	movl	%ecx, -20(%rbp)
	movl	%r8d, -24(%rbp)
	vmovsd	%xmm0, -32(%rbp)
	movq	%r9, -40(%rbp)
	vmovsd	%xmm1, -48(%rbp)
	movb	%al, -12(%rbp)
	movq	40(%rbp), %rax
	cmpq	-8(%rbp), %rax
	je	L9
	call	abort
L9:
	leave
	ret
.globl _start
_start:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$48, %rsp
	movabsq	$4619567317775286272, %rdx
	leaq	-16(%rbp), %rsi
	movabsq	$4616189618054758400, %rax
	leaq	-48(%rbp), %rdi
	pushq	$8
	leaq	-48(%rbp), %rcx
	pushq	%rcx
	pushq	$6
	leaq	-32(%rbp), %rcx
	pushq	%rcx
	pushq	$5
	vmovq	%rdx, %xmm1
	movq	%rsi, %r9
	vmovq	%rax, %xmm0
	movl	$3, %r8d
	movl	$2, %ecx
	movl	$1, %edx
	movl	$66, %esi
	call	bug
	addq	$40, %rsp
	movl	$0, %eax
	leave
	ret