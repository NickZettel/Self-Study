#include <stdio.h>


/* Write a C program that
1.Asks the user for two integers (let’s call them a and b).
2.Prints the sum, difference, product, and quotient of a and b 
(e.g., “Sum: X, Difference: Y, Product: Z, Quotient: W”).
3.Checks if b is not zero before dividing (to avoid a divide-by-zero 
crash—C won’t save you here!).
4.Uses a for loop to print all even numbers from 1 to a (inclusive, 
if a is positive). If no even numbers exist, say so.
5.Bonus: Add a while loop to keep asking for a new a and b 
until the user enters 0 for both numbers to exit. */

int main() {
    while (1==1){
        printf("Hello \n");
        printf("Please enter an integer! \n");
        fflush(stdout);
        int a;
        scanf("%i",&a);
        printf("Thanks, now another one!\n");
        fflush(stdout);
        int b;
        scanf("%i",&b);
        if (a == 0 && b == 0){
            break;
        }
        printf("sum %i, difference %i, product %i, division ",a+b,a-b,a*b);
        if (b == 0){
            printf("not possible");
        }
        else{
            printf("%.3f", (float)a/b);
        }

        printf("\nNow for all even numbers from 1 to your first number\n");
        for (int i = 0; i <= a; i++){
            if (i % 2 == 0){
                printf("%i ", i);
            }
        }
    
    }
    printf("exiting");

    return 0;
}
