#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/* Markers used to bound trace regions of interest */
volatile char MARKER_START, MARKER_END;

int main() {
    static int arr[8192];
    int offset = 0, step = 2, tmp = 0;

    /* Record marker addresses */
    FILE* marker_fp = fopen(".marker", "w");
    assert(marker_fp);
    fprintf(marker_fp, "%llx %llx", 
            (unsigned long long int) &MARKER_START,
            (unsigned long long int) &MARKER_END );
    fclose(marker_fp);

    MARKER_START = 33; /* access marker to generate a trace record */

    for (int i = 0; i < 1024; i ++) {
        /* printf("%d ", arr[i]); */
        tmp += arr[offset];
        offset += step;
    }

    MARKER_END = 34; /* access marker again */

    return 0;
}
