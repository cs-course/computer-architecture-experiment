#include <immintrin.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define N 32
typedef int32_t Matrix[N][N];

// 使用AVX2指令集优化的矩阵转置
void transpose_avx2(Matrix src, Matrix dst) {
    // 每次处理8x8块（AVX2寄存器为256位，可容纳8个int32）
    for (int i = 0; i < N; i += 8) {
        for (int j = 0; j < N; j += 8) {
            // 加载8x8块到8个AVX2寄存器
            __m256i row0 = _mm256_loadu_si256((__m256i*)&src[i+0][j]);
            __m256i row1 = _mm256_loadu_si256((__m256i*)&src[i+1][j]);
            __m256i row2 = _mm256_loadu_si256((__m256i*)&src[i+2][j]);
            __m256i row3 = _mm256_loadu_si256((__m256i*)&src[i+3][j]);
            __m256i row4 = _mm256_loadu_si256((__m256i*)&src[i+4][j]);
            __m256i row5 = _mm256_loadu_si256((__m256i*)&src[i+5][j]);
            __m256i row6 = _mm256_loadu_si256((__m256i*)&src[i+6][j]);
            __m256i row7 = _mm256_loadu_si256((__m256i*)&src[i+7][j]);

            // 转置8x8块
            __m256i t0 = _mm256_unpacklo_epi32(row0, row1);
            __m256i t1 = _mm256_unpackhi_epi32(row0, row1);
            __m256i t2 = _mm256_unpacklo_epi32(row2, row3);
            __m256i t3 = _mm256_unpackhi_epi32(row2, row3);
            __m256i t4 = _mm256_unpacklo_epi32(row4, row5);
            __m256i t5 = _mm256_unpackhi_epi32(row4, row5);
            __m256i t6 = _mm256_unpacklo_epi32(row6, row7);
            __m256i t7 = _mm256_unpackhi_epi32(row6, row7);

            // 重组排列
            __m256i v0 = _mm256_shuffle_epi32(t0, _MM_SHUFFLE(3,1,2,0));
            __m256i v1 = _mm256_shuffle_epi32(t1, _MM_SHUFFLE(3,1,2,0));
            __m256i v2 = _mm256_shuffle_epi32(t2, _MM_SHUFFLE(3,1,2,0));
            __m256i v3 = _mm256_shuffle_epi32(t3, _MM_SHUFFLE(3,1,2,0));
            __m256i v4 = _mm256_shuffle_epi32(t4, _MM_SHUFFLE(3,1,2,0));
            __m256i v5 = _mm256_shuffle_epi32(t5, _MM_SHUFFLE(3,1,2,0));
            __m256i v6 = _mm256_shuffle_epi32(t6, _MM_SHUFFLE(3,1,2,0));
            __m256i v7 = _mm256_shuffle_epi32(t7, _MM_SHUFFLE(3,1,2,0));

            // 交换高低128位
            __m256i final0 = _mm256_permute2x128_si256(v0, v4, 0x20);
            __m256i final1 = _mm256_permute2x128_si256(v1, v5, 0x20);
            __m256i final2 = _mm256_permute2x128_si256(v2, v6, 0x20);
            __m256i final3 = _mm256_permute2x128_si256(v3, v7, 0x20);
            __m256i final4 = _mm256_permute2x128_si256(v0, v4, 0x31);
            __m256i final5 = _mm256_permute2x128_si256(v1, v5, 0x31);
            __m256i final6 = _mm256_permute2x128_si256(v2, v6, 0x31);
            __m256i final7 = _mm256_permute2x128_si256(v3, v7, 0x31);

            // 存储转置后的数据
            _mm256_storeu_si256((__m256i*)&dst[j+0][i], final0);
            _mm256_storeu_si256((__m256i*)&dst[j+1][i], final1);
            _mm256_storeu_si256((__m256i*)&dst[j+2][i], final2);
            _mm256_storeu_si256((__m256i*)&dst[j+3][i], final3);
            _mm256_storeu_si256((__m256i*)&dst[j+4][i], final4);
            _mm256_storeu_si256((__m256i*)&dst[j+5][i], final5);
            _mm256_storeu_si256((__m256i*)&dst[j+6][i], final6);
            _mm256_storeu_si256((__m256i*)&dst[j+7][i], final7);
        }
    }
}

// 验证函数
void verify(const Matrix src, const Matrix dst) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (src[i][j] != dst[j][i]) {
                printf("验证失败 @ [%d][%d]\n", i, j);
                exit(1);
            }
        }
    }
    printf("转置验证成功!\n");
}

int main() {
    // 初始化矩阵
    Matrix src, dst;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            src[i][j] = i * N + j;  // 填充唯一值
        }
    }

    // 执行转置
    transpose_avx2(src, dst);

    // 验证结果
    verify(src, dst);
    return 0;
}