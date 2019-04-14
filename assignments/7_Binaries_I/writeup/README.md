# Writeup 7 - Binaries I

Name: Adhithya
Section:0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
printf("your code here");

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

```

### Part 2 (10 Pts)

This code is an XOR swap.
