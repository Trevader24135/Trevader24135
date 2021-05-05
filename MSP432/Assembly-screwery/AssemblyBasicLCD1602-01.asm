P4DIR		.field	0x40004C25
P4OUT		.field	0x40004C23
P6DIR		.field	0x40004C45
P6OUT		.field	0x40004C43
	.global main



main:
prepIORegs:
	MOV		R0,		#0x00	;R0 <- 0
	LDR		R8,	P4OUT		;initialize P4 register output to 0
	STRB	R0,		[R8]
	LDR		R8,	P6OUT		;initialize P6 register output to 0
	STRB	R0,		[R8]

	MOV		R0,		#0xFF	;set P4 to output
	LDR		R8,	P4DIR
	STRB	R0,		[R8]
	LDR		R8,	P4OUT		;R8 containts P4OUT

	MOV		R0,		#0x03	;set P6.1-2 to output. 0 is E, 1 is RS
	LDR		R9,	P6DIR
	STRB	R0,		[R9]
	LDR		R9,	P6OUT		;R9 containts P6OUT

	BL		clearRS			;set function to 8 data lines
	MOV		R0,		#0x0030
	BL		sendR0
	BL		sendR0
	BL		sendR0

	MOV		R0,		#0x01	;clear display
	BL		sendR0
	MOV		R0,		#0x01	;clear display
	BL		sendR0
	MOV		R0,		#0x00	;clear display
	BL		sendR0
	MOV		R0,		#0x00	;clear display
	BL		sendR0

	BL		setRS			;set RS to 1 to write characters

	MOV		R0,		#0x48
	BL		sendR0

	B		stop

setRS:								;set the RS line high
	LDR		R0,		[R9]
	ORR		R0,		R0,		#0x2
	STRB	R0,		[R9]
	BX		LR

clearRS:							;set the RS line low
	LDR		R11,		[R9]
	AND		R11,		R11,		#0xFD
	STRB	R11,		[R9]
	BX		LR

flashE:								;set the E line high, then low again
	LDR		R11,		[R9]
	EOR		R11,		R11,		#0x1
	STRB	R11,		[R9]
	EOR		R11,		R11,		#0x1
	STRB	R11,		[R9]
	BX		LR

sendR0:
	STRB	R0,		[R8]
	MOV		R12,	LR
	BL		flashE
	BX		R12

stop:
	B	stop
	.end
