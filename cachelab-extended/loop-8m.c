#include <stdio.h>

int main() {
    static int arr[8000000];
    int offset = 0, step = 1, tmp = 0;
    for (int i = 0; i < 1000000; i ++) {
        /* printf("%d ", arr[i]); */
        tmp += arr[offset];
        offset += step;
    }
    return 0;
}
