# Makefile
.PHONY: build clean run test

build:
	@echo "Compiling Core ASI and Interop FFI bindings..."
	cd interop_bridge && cargo build --release
	cd core_asi && cargo build --release
	@echo "A3-I3 System Built Successfully."

test:
	@echo "Running functional engine verifications..."
	cd core_asi && cargo test
	python3 -m unittest discover -s core_agi/tests -p "*_test.py"

clean:
	rm -rf interop_bridge/target core_asi/target
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Build artifacts purged."

run: build
	cd core_agi && python3 main.py
