#include <stdio.h>

int main() {
  //a fixed size (static) array initiated with variables
    int y[] = {1,2,3,4,5};

    //getting the number of elements by dividing the total size of the
    //array (in bytes) by the size of one element (in bytes).
    int length_x = sizeof(y) / sizeof(y[0]);

    printf("Array-Based List \n");
    printf("Size of the array in bytes: %d\n", sizeof(y));
    printf("Size of one element in bytes: %d\n", sizeof(y[0]));

    //printing the contents of the array
    for (int i = 0; i < length_x; i++){
      printf("Element %d contains: %d\n", y[i]-1, y[i]);
    }
}
