P2OUT		.field	0x40004c03
P2DIR		.field	0x40004c05
COUNTERMAX	.field	0x0000FFFF

	.global main

main:
	LDR		R0,		P2DIR			;Set Port 1.1 to Output
	MOV		R7,		#0x7
	STRB	R7,		[R0]
	LDR		R0,		P2OUT			;Prepare address of Port 1

	LDR		R7,		COUNTERMAX		;Prepare Counter
	MOV		R1,		#0100010111010001b
	MOVT	R1,		#1000101110100010b


loop:
	SUB		R7,		#0x1			;Subtract one from counter

	CBNZ	R7,		skip			;Restart loop if the counter is not zero
	LDR		R7,		COUNTERMAX		;Reset Timer

	ROR		R1,		R1,		#0x1
	AND		R2,		R1,		#0x00000007	;Toggle LED
	STRB	R2,		[R0]

skip:
	b loop

stop:
	b 	stop

	.end
