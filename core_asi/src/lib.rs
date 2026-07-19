// core_asi/src/lib.rs
pub mod optimizer;
pub mod meta_monitor;
pub mod recompilation;

pub fn initialize_meta_layer() {
    let monitor = meta_monitor::MetaMonitor::init();
    let opt = optimizer::RecursiveOptimizer::new();
    println!("[ASI_INIT] Sub-systems online. Performance monitoring actively hooked.");
}
