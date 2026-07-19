// interop_bridge/memory_bus/mod.rs
pub mod shm_manager;

pub fn initialize_memory_bus(capacity_gb: usize) {
    // Hooks the global shared memory block to prevent CPU-GPU copy bottlenecks
    println!("[INTEROP] Initializing zero-copy memory bus at {} GB capacity.", capacity_gb);
    let _bus = shm_manager::SharedMemoryManager::allocate("a3_i3_global_bus", capacity_gb * 1_000_000_000);
}
