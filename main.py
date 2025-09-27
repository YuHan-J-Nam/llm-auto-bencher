# Import Libraries
import psutil
import subprocess
import shlex # library to help safely split command strings

def get_hardware_specs():
	"""
	Detects CPU, RAM, and NVIDIA GPU hardware specifications.
	Returns a dictionary containing all the specs.
	"""

	# 1. Obtain server CPU and RAM info
	specs = {
		"cpu_cores": psutil.cpu_count(),
		"ram_total_gb": round(psutil.virtual_memory().total / (1024**3), 2)
	}

	# 2. Try to obtain NVIDIA GPU info

	# Initialize null values in case there is no NVIDIA GPU 
	specs['gpu_model'] = "N/A"
	specs['gpu_driver_version'] = "N/A"
	specs['gpu_vram_gb'] = 0

	try:
		command = [
			"nvidia-smi",
			"--query-gpu=gpu_name,driver_version,memory.total",
			"--format=csv,noheader,nounits"
		]
		smi_output = subprocess.check_output(command, text=True)

		# Parse nvidia-smi results
		gpu_info = smi_output.strip().split(',')
		specs['gpu_model']=gpu_info[0].strip()
		specs['gpu_driver_version']=gpu_info[1].strip()
		specs['gpu_vram_gb'] = round(int(gpu_info[2].strip())/1024, 2)

	except subprocess.CalledProcessError as e:
		print(f"Error running nvidia-smi: {e}")
	except FileNotFoundError:
		print("nvidia-smi not found. Please make sure NVIDIA drivers are installed.")

	return specs

# Main execution block
if __name__ == "__main__":
	print("Detecting hardware specifications")
	hardware_specs = get_hardware_specs()

	print("\n--- System Information ---")
	print(f"CPU Cores: {hardware_specs['cpu_cores']}")
	print(f"Total RAM: {hardware_specs['ram_total_gb']} GB")
	print(f"GPU Model: {hardware_specs['gpu_model']}")
	print(f"GPU VRAM: {hardware_specs['gpu_vram_gb']} GB")
	print(f"NVIDIA Driver Version: {hardware_specs['gpu_driver_version']}")
	print("--------------------------")
