P2OUTREG	.field	0x40004c03
P2DIRREG	.field	0x40004c05

	.global main

main:
	LDR	R0, P2DIRREG
	MOV R1, #0x7
	STR R1, [R0]

	LDR	R0, P2OUTREG
	MOV R1, #0x0

loop:
	EOR R1, R1, #0x7
	STRB R1, [R0]
	b loop

stop:
	b 	stop

	.end
