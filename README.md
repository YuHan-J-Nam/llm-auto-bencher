# LLM Auto-Bencher

An automated tool to profile server hardware, dynamically discover compatible models, and benchmark their performance.

## Overview

This project automatically detects a server's hardware specifications (CPU, RAM, GPU, Disk). It then queries the public Ollama model registry to fetch a list of available models. Based on the detected hardware, it generates a tailored recommendation table, showing which models the system can likely run. Finally, it provides tools to benchmark the performance of a running LLM service (like Ollama) by measuring metrics such as tokens per second.

The project is developed with a dual-track approach: a robust Python application for the core logic, and a parallel set of pure shell scripts in the `shell_equivalents/` directory for educational comparison.

## Requirements

- Linux (Ubuntu 22.04+ recommended) with NVIDIA Drivers (for GPU detection)
- Python 3.10+
- An internet connection (to query the Ollama model API)
- An `llm-auto-bencher/requirements.txt` file that includes `psutil`, `requests`, `tabulate`.
- Git

## Usage

1.  **Get Hardware-Based Recommendations:**
    ```bash
    # (Coming Soon) The script will automatically fetch models and generate a table.
    python3 main.py
    ```

2.  **Benchmark a running Ollama service:**
    ```bash
    # (Coming Soon)
    python3 benchmark_ollama.py "Your prompt here"
    ```

## Project Structure

- `main.py`: The core Python engine for detection and recommendation.
- `benchmark_ollama.py`: Script to benchmark a running Ollama instance.
- `requirements.txt`: Python dependencies.
- `ARCHITECTURE.md`: Documentation of the server setup used for development.
- `shell_equivalents/`: Contains pure shell scripts for learning and comparison
