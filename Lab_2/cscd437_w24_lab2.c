#include <stdio.h>
#include <stdlib.h>

const int MAX = 100;

void foo(void)
{
    int a[5] = {100, 200, 300, 400, 500};
	double d = 3.14159;
    int *b = calloc(32, sizeof(int));
    int *c = malloc(32);
    int i;
	char ltr = 'a';

    printf("1: a = %p, b = %p, c = %p, d = %p, i = %p, MAX=%p\n", a, &b, &c, &d, &i, &MAX);
    printf("2: b = %p, c = %p\n", b, c);

    c = a;
    c = (int *) ((char *) c + 1);
    *c = 800;
    printf("3: a[0] = %d, a[1] = %d, a[2] = %d, a[3] = %d\n",
	   a[0], a[1], a[2], a[3]);

 

}// end function


int main(int ac, char **av)
{
    int x = 12;
	double val = 4.9567;
	double *dptr = &val;
	int array[] = {10,20,30,40,50,60};
	double val2 = 3.14159;
	int y = 99;
	double * dptr2 = &val2;
	int *ptr2 = &y;
	char *word = (char*)calloc(10, sizeof(char));
	int *ptr = &x;

	printf("x: %p\nptr: %p\nval: %p\ndptr: %p\narray: %p\narray[5]: %p\nval2: %p\ny:%p\ndptr2: %p\nptr2: %p\nword: %p\n", &x, &ptr, &val, &dptr, &array[0], &array[5], &val2, &y, &dptr2, &ptr2, &word);
	printf("word: %p\n", word);

    foo();
   
    return 0;
   
}// end main

