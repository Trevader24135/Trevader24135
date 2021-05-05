#include "msp.h"
#include <stdint.h>
#include <stdio.h>



/**
 * main.c
 */

void main(void)
{
	WDT_A->CTL = WDT_A_CTL_PW | WDT_A_CTL_HOLD;		// stop watchdog timer

	int i;
	char string[10];

	printf("Enter a String!:\n");

	scanf("%s", string);

	for (i = 0; i < sizeof(string), string[i] != 0; i++){
	    printf("decimal: %d | hex: %x\n", string[i], string[i]);
	}

	while(1) {

	}
}

