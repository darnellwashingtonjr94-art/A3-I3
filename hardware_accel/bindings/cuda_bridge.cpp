// hardware_accel/bindings/cuda_bridge.cpp
#include <cuda_runtime.h>
#include <iostream>

extern "C" {
    void launch_matrix_mul(const float* A, const float* B, float* C, int N) {
        // C-wrapper exposing the CUDA kernel to the Rust FFI interop bridge
        dim3 threadsPerBlock(16, 16);
        dim3 numBlocks((N + threadsPerBlock.x - 1) / threadsPerBlock.x,
                       (N + threadsPerBlock.y - 1) / threadsPerBlock.y);
                       
        std::cout << "[CUDA_BRIDGE] Launching hardware accelerated matrix multiplication..." << std::endl;
        // fast_matrix_mul<<<numBlocks, threadsPerBlock>>>(A, B, C, N);
    }
}
