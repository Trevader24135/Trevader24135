.text
P2OUTREG	.field	0x40004c03
P2DIRREG	.field	0x40004c05

	.align 2
	.global main
	
main:
	;LDR	R0, P2OUTREG
	;LDR R1, [R0]
	;ORR R1, R1, R3
	;STR R1, [R0]
	
	LDR	R0, P2DIRREG
	LDR R2, [R0]
	ORR R2, R2, #0x00000001
	STR R2, [R0]
	
stop:
	b 	stop
	
	.end