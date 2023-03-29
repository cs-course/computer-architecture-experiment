#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/* Markers used to bound trace regions of interest */
volatile char MARKER_START, MARKER_END;

int main() {
    static int matrix[32][32];
    int i, j;

    // initialize matrix
    for (i = 0; i < 32; i++) {
        for (j = 0; j < 32; j++) {
            matrix[i][j] = i * 32 + j;
        }
    }

    // print original matrix
    // printf("Original Matrix:\n");
    // for (i = 0; i < 32; i++) {
    //     for (j = 0; j < 32; j++) {
    //         printf("%d ", matrix[i][j]);
    //     }
    //     printf("\n");
    // }

    /* Record marker addresses */
    FILE* marker_fp = fopen(".marker", "w");
    assert(marker_fp);
    fprintf(marker_fp, "%llx %llx", 
            (unsigned long long int) &MARKER_START,
            (unsigned long long int) &MARKER_END );
    fclose(marker_fp);

    MARKER_START = 33; /* access marker to generate a trace record */

    // transpose matrix
    for (i = 0; i < 32; i++) {
        for (j = i + 1; j < 32; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    MARKER_END = 34; /* access marker again */

    // print transposed matrix
    // printf("Transposed Matrix:\n");
    // for (i = 0; i < 32; i++) {
    //     for (j = 0; j < 32; j++) {
    //         printf("%d ", matrix[i][j]);
    //     }
    //     printf("\n");
    // }

    return 0;
}
