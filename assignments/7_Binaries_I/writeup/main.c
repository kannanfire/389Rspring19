/*
 * Name: Adhithya Kannan
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Adhithya Kannan
 */

/* your code goes here */

#import <stdio.h>

int main() {
	int b = 0x1ceb00da;
    int a = 0xfeedface;
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    b ^= a;
    a ^= b;
    b ^= a;
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    return 0; 
}
