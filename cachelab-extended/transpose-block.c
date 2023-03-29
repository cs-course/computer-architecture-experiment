#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define N 32
#define BLOCK_SIZE 8

/* Markers used to bound trace regions of interest */
volatile char MARKER_START, MARKER_END;

void transpose(int matrix[N][N]) {
    for (int i = 0; i < N; i += BLOCK_SIZE) {
        for (int j = 0; j < N; j += BLOCK_SIZE) {
            for (int ii = i; ii < i + BLOCK_SIZE; ii++) {
                for (int jj = j; jj < j + BLOCK_SIZE; jj++) {
                    // if (ii != jj) {
                    if (ii < jj) {
                        int temp = matrix[ii][jj];
                        matrix[ii][jj] = matrix[jj][ii];
                        matrix[jj][ii] = temp;
                    }
                }
            }
        }
    }
}

int main() {
    static int matrix[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            matrix[i][j] = i * N + j;
        }
    }

    /* Record marker addresses */
    FILE* marker_fp = fopen(".marker", "w");
    assert(marker_fp);
    fprintf(marker_fp, "%llx %llx", 
            (unsigned long long int) &MARKER_START,
            (unsigned long long int) &MARKER_END );
    fclose(marker_fp);

    MARKER_START = 33; /* access marker to generate a trace record */

    transpose(matrix);

    MARKER_END = 34; /* access marker again */

    // for (int i = 0; i < N; i++) {
    //     for (int j = 0; j < N; j++) {
    //         printf("%d ", matrix[i][j]);
    //     }
    //     printf("\n");
    // }

    return 0;
}
