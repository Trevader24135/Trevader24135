P2OUT		.field	0x40004c03
P2DIR		.field	0x40004c05
COUNTERMAX	.field	0x0000FFFF

	.global main

main:

memclear:
	MOV		R9,		#0xF000			;R9 stores top of cleared memory
	MOVT	R9,		#0x2000
	MOV		R0, 	#0				;R0 stores  blank bits
	MOV 	R1, 	#0x0100			;R1 is the current memory pointer
	MOVT	R1,		#0x2000

memclearloop:
	STR		R0,		[R1]			;store R0s zeros in R1s memory
	ADD		R1,		R1,		#0x4	;increment R1 by a word length
	CMP		R1,		R9				;compare to see if R1 has exceeded top of memory
	BMI		memclearloop			;loop if it has not exceeded top of memory, else move on

prepare:
	MOV 	R0, 	#0x0100			;R0 is the current memory pointer
	MOVT	R0,		#0x2000
	MOV		R1,		#0x0001			;prepare first digits of fib. sequence
	MOV		R2,		#0x0001

fibloop:
	ADDS		R3,		R1,		R2	;generate the next number of the fib sequence
	STR		R3,		[R0]			;store the new fib number
	BVS		stop					;stop when overflow is detected
	ADD		R0,		R0,		#0x4	;move to the next memory location
	MOV		R1,		R2				;shift registers to prepare for next generation
	MOV		R2,		R3
	CMP		R0,		R9				;compare current memory location to prevent exceeding allocated space
	BMI		fibloop					;loop if memory has not been exceeded
	B stop							;exit if memory has been exceeded

stop:
	B	stop

	.end
