// hardware_accel/kernels/matrix_mul.cu
__global__ void fast_matrix_mul(const float* A, const float* B, float* C, int N) {
    // Custom CUDA kernel for accelerating ANI deterministic math solvers
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    
    if (row < N && col < N) {
        float val = 0.0f;
        for (int i = 0; i < N; ++i) {
            val += A[row * N + i] * B[i * N + col];
        }
        C[row * N + col] = val;
    }
}
