# Import Libraries
import psutil
import subprocess

def get_cpu_and_ram_info():
	return {"CPU_count": psutil.cpu_count(),
		"MEM_size": psutil.virtual_memory().total / (1024**3)}

hardware_specs = get_cpu_and_ram_info()

print(f"Number of CPUs: {hardware_specs['CPU_count']}")
print(f"Size of Memory: {hardware_specs['MEM_size']:.2f}GB")

def call_nvidia_smi():
	try:
		result = subprocess.run("nvidia-smi --query-gpu=gpu_name,driver_version,memory.total --format=csv,noheader,nounits",
			capture_output=True,
			text=True,
			check=True)
		return result.stdout.strip().split(',')
	except subprocess.CalledProcessError as e:
		print(f"Error running nvidia-smi: {e}")
		return None, None, None
	except FileNotFoundError:
		print("nvidia-smi not found. Please make sure nvidia drivers are installed.")
		return None, None, None
	except (IndexError, ValueError) as e:
		print(f"Error parsing nvidia-smi output: {e}")
		return None, None, None

GPU_model, driver_ver, VRAM_size = call_nvidia_smi()
hardware_specs['GPU_model'] = GPU_model
hardware_specs['driver_ver'] = driver_ver
hardware_specs['VRAM_size'] = VRAM_size

print(hardware_specs)
