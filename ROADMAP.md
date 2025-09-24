# Project Roadmap

This project follows a dual-track approach. For each milestone, we will build the main application component and a corresponding shell script for learning.

### Milestone 1: Hardware Detection
- **1A (Python):** Create `get_hardware_specs()` in `main.py` using `psutil` and structured output from `nvidia-smi`.
- **1B (Shell):** Create `shell_equivalents/detect_hardware.sh` using `lscpu`, `free`, and text parsing.

### Milestone 2: Running an LLM via Docker
- **2A (Docker/Shell):** Create a `docker-compose.yml` file. Update `run_benchmark.sh` to manage the service.
- **2B (Python/Shell):** Implement programmatic control in `main.py` using the Docker SDK. Compare with simple shell commands in `shell_equivalents/manage_docker.sh`.

### Milestone 3: The Benchmarking Engine
- **3A (Python):** Create `run_benchmark()` in `main.py` using the `requests` library to measure latency and throughput from a streaming API.
- **3B (Shell):** Create `shell_equivalents/query_api.sh` using `curl` and `jq` to hit a simple API endpoint.

### Milestone 4: Integration and Structured Logging
- **4A (Python):** Orchestrate the full workflow in `main.py` and log results safely to `results.csv` using `pandas`.
- **4B (Shell):** Demonstrate simple, brittle logging in `run_benchmark.sh` using `echo` and `>>`.
