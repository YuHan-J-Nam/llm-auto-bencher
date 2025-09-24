# Project Plan: LLM Auto-Bencher

### Vision Statement
To create a portable benchmarking tool that automatically profiles a server's hardware and measures LLM performance. The project will serve as a hands-on learning experience by developing a robust Python-based application alongside pure shell script equivalents for direct comparison.

### Goals & Objectives
- **Automated Profiling:** Eliminate manual hardware checks.
- **Reproducibility:** Use Docker for consistent LLM environments.
- **Data-Driven Insights:** Generate structured data on key performance metrics.
- **Dual-Path Learning:** For each core task, develop and document both a robust Python implementation and a traditional Linux shell script equivalent to understand the trade-offs in reliability, maintainability, and development speed.

### Project Scope

| In-Scope (What we will build first) | Out-of-Scope (What we can add later) |
| :--- | :--- |
| Hardware Detection: CPU (cores, model), RAM (total), GPU (model, VRAM), Disk. | Detailed network or PCIe bus speed analysis. |
| LLM Support: Test pre-configured models like Llama 3 and Mistral 7B. | Fine-tuning models. |
| Benchmarking: Measure inference latency and throughput (tokens/second). | Complex accuracy benchmarks (e.g., MMLU). |
| User Interface: A Command-Line Interface (CLI). | A graphical user interface (GUI) or web dashboard. |
| Data Storage: Save benchmark results to a local CSV or JSON file. | A dedicated database. |
| OS Support: Develop on Ubuntu, with a goal for broader Linux support. | Windows or macOS support. |
