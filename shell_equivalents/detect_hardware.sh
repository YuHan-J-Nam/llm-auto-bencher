#!/bin/bash

echo "--- Shell Script Hardware Detection ---"

# --- CPU and RAM Detection ---
CPU_CORES=$(lscpu | grep "^CPU(s)" | awk '{print $2}')
echo "CPU Cores:  $CPU_CORES"

TOTAL_RAM_GB=$(free -m | grep "^Mem:" | awk '{printf "%.2f", $2 / 1024}')
echo "Total RAM: $TOTAL_RAM_GB GB"

# --- GPU Detection with Error Handling ---
if command -v nvidia-smi &> /dev/null
then
	# If it exists, retrieve GPU specs
	GPU_INFO=$(nvidia-smi --query-gpu=gpu_name,driver_version,memory.total --format=csv,noheader,nounits)

	GPU_MODEL=$(echo "$GPU_INFO" | awk -F ',' '{print $1}')
	echo "GPU Model: $GPU_MODEL"

	TOTAL_VRAM_GB=$(echo "$GPU_INFO" | awk -F ',' '{printf "%.2f",  $3 / 1024}')
	echo "GPU VRAM: $TOTAL_VRAM_GB GB"

	GPU_DRIVER_VER=$(echo "$GPU_INFO" | awk -F ',' '{print $2}')
	echo "NVIDIA Driver Version: $GPU_DRIVER_VER"
else
	# If the command does not exist, report it
	echo "No NVIDIA GPU detected"
fi

echo "---------------------------------------"
