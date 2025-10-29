# Project Roadmap

A revised roadmap reflecting the project's evolution towards a more dynamic and intelligent tool.

### Milestone 1: Hardware Profiling Engine (✅ Completed)
- **1A (Python):** Develop a robust script to detect CPU, RAM, Disk (including type/model), and NVIDIA GPU specifications.
- **1B (Shell):** Create a parallel shell script for educational comparison.
- **1C (Validation):** Successfully run the scripts on the target `llm-server` VM with GPU passthrough to validate the logic against real hardware.

### Milestone 2: Dynamic Recommendation Engine (⏳ In Progress)
- **2A (API Discovery):** Identify and test the public API used by the Ollama website to search for models.
- **2B (Data Integration):** Write a Python function to call this API, parse the JSON response, and extract relevant model data (name, size, parameters).
- **2C (Table Generation):** Refactor the recommendation logic to use the live API data. The function will compare hardware specs against each discovered model's requirements and generate a formatted table using the `tabulate` library.

### Milestone 3: Performance Benchmarking Engine (Up Next)
- **3A (Streaming Client):** Implement a streaming client in `benchmark_ollama.py` to process the API response token-by-token.
- **3B (Metric Calculation):** Use the streaming data to accurately measure and calculate Time-to-First-Token (Latency) and Tokens-per-Second (Throughput).
- **3C (Structured Logging):** Save benchmark results to a structured format like CSV, including the hardware specs for that run.

### Milestone 4: Application Containerization (Future)
- **4A (Dockerfile):** Write a `Dockerfile` to package the entire tool, including all its Python dependencies.
- **4B (Distribution):** Refine the application to be run as a simple `docker run` command, making it easily portable and distributable.
