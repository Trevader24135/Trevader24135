#include "msp.h"
#include <stdint.h>
#include <stdio.h>



/**
 * main.c
 */

void main(void)
{
	WDT_A->CTL = WDT_A_CTL_PW | WDT_A_CTL_HOLD;		// stop watchdog timer

	int integer;
	int i;
	char string[10];

	printf("Enter a String:\n");

	scanf("%s", string);
	integer = atoi(string);

    printf("your number is: %d\n", integer);

	while(1) {

	}
}

