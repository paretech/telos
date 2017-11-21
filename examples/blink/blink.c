//***************************************************************************************
// MSP430 Timer Blink LED Demo - Timer A Software Toggle P1.0 & P1.6
//
// Description; Toggle P1.0 and P1.6 by xor'ing them inside of a software loop. 
// Since the clock is running at 1Mhz, an overflow counter will count to 8 and then toggle
// the LED. This way the LED toggles every 0.5s. 
// ACLK = n/a, MCLK = SMCLK = default DCO 
//
// Built with MSP430mcu
//***************************************************************************************
#include <msp430f1611.h>
// #include <io.h>


#define pin4mask  (0x01 << 4)

int main(void) {
    /* Hold the watchdog timer so it doesn't reset our chip */
    WDTCTL = WDTPW + WDTHOLD;

    /* Configure all pins on port 1 as output pins */
    P5DIR = 0xff;

    /* Set pin 6 high.  Basically, this command sets any combination
     * of the pins on port 1 high.  Pin 0 is 2^0, pin 1 is 2^2, etc.
     * Values can be binary or'd together. Other pins are low.
     */
    P5OUT = pin4mask;

    /* infinite loop */
    for( ; ; ) {
        /* The following two lines implement a very crude delay loop.
         * The actual length of the delay can vary significantly.
         * This approach may not work with all compilers.
         */
        volatile int i;
        for( i = 0; i < 20000; i++ );

        /* Toggle the state of pin 6 on port 1 by exclusive or'ing with
           the mask that represents that pin. */
        P5OUT = P5OUT ^ pin4mask;
    }
}