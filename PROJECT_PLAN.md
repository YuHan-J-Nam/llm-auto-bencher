# Project Plan: LLM Auto-Bencher

### Vision Statement
To create a portable, intelligent tool that profiles a server's hardware and empowers users by dynamically discovering and recommending compatible LLMs from public registries, then provides the tools to benchmark their real-world performance.

### Goals & Objectives
- **Automated Hardware Profiling:** Reliably detect server hardware (CPU, GPU, RAM, Disk).
- **Dynamic Model Discovery:** Fetch an up-to-date list of available models by querying public APIs (e.g., Ollama's).
- **Intelligent Recommendation Engine:** Analyze hardware specs and model data to generate a clear, tabular recommendation of which models are suitable for the user's system.
- **Standardized Benchmarking:** Provide scripts to measure key performance metrics (latency, tokens/second) against a running LLM service.
- **Dual-Path Learning:** Maintain a parallel set of shell scripts to contrast with the Python implementation and deepen system-level understanding.

### Technical Stack & Architecture
- **Language:** Python 3.10+, Bash Shell Script
- **Key Libraries:** `psutil` (hardware), `requests` (API communication), `tabulate` (output formatting)
- **Primary Data Source:** Ollama's public web API for the model library.
- **Target LLM Service:** Ollama API endpoint for benchmarking.
- **Version Control:** Git, GitHub
