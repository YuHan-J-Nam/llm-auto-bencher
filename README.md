# LLM Auto-Bencher

An automated tool to profile server hardware and benchmark local LLMs.

## Overview

This project automatically detects hardware (CPU, GPU, RAM) and runs performance tests on local LLMs using Docker and Hugging Face's Text Generation Inference (TGI).

The project is developed with a dual-track approach: a robust Python application for the core logic, and a parallel set of pure shell scripts in the `shell_equivalents/` directory for educational comparison.

## Requirements

- Linux (Ubuntu 22.04+ recommended)
- Docker and Docker Compose
- NVIDIA Container Toolkit (for NVIDIA GPUs)
- Python 3.10+
- Git

## Usage

(Coming soon)

## Project Structure

- `run_benchmark.sh`: The main entry point for the application.
- `main.py`: The core Python engine for detection, benchmarking, and logging.
- `docker-compose.yml`: Defines the LLM services to be run.
- `requirements.txt`: Python dependencies.
- `results.csv`: The output file where benchmark results are stored.
- `shell_equivalents/`: Contains pure shell scripts for learning and comparison.
