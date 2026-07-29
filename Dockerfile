# Dockerfile
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

# Install Rust toolchain and Python environment
RUN apt-get update && apt-get install -y curl python3-pip make \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"
WORKDIR /opt/a3_i3_engine

COPY . .

# Set Python path to ensure internal packages/modules are discoverable
ENV PYTHONPATH=/opt/a3_i3_engine

# Compile the ASI Rust core and FFI bindings via the workspace member
RUN cargo build --release -p interop_bridge

# Install AGI Orchestrator dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "core_agi/main.py"]
