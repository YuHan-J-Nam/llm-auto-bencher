# Home Server System Architecture

This document outlines the system architecture, resource allocation, and available service endpoints for the Proxmox home server.

## 1. System Overview

This is a single-node virtualization server running on a laptop. Its purpose is to provide:
1.  A lightweight **Docker Host (LXC)** for running 24/7 containerized services.
2.  A powerful **LLM Server (VM)** with dedicated GPU passthrough for AI and machine learning tasks.

---

## 2. Physical Host Hardware

* **Model:** Laptop (AMD Ryzen 7 4800H)
* **CPU:** 8-Core / 16-Thread
* **RAM:** 16GB
* **GPU:** NVIDIA GeForce RTX 2060 Mobile (6GB VRAM)
    * **Note:** The GPU is fully dedicated to `llm-server` (VM 101) via VFIO passthrough and is unavailable to the Proxmox host or any other guest.

---

## 3. Network Structure & IP Allocation

The core network is `192.168.219.0/24`. The router's DHCP pool is restricted to `.100` - `.200`. All server components use static IPs *outside* this range.

| IP Address          | Hostname       | Purpose                  |
| :------------------ | :------------- | :----------------------- |
| `192.168.219.1`     | `(Router)`     | Network Gateway / DNS    |
| `192.168.219.10`    | `proxmox`      | Proxmox Host Hypervisor  |
| `192.168.219.20`    | `docker-host`  | LXC 100: Docker Services |
| `192.168.219.130`   | `llm-server`   | VM 101: LLM Server       |

---

## 4. Guest Systems & Services

### 4.1. Guest 100: `docker-host`

* **Type:** LXC Container
* **IP Address:** `192.168.219.20`
* **OS:** Debian 12
* **Allocated Resources:** 4 CPU Cores, 4GB RAM
* **Purpose:** Runs all lightweight, CPU-based services via Docker.
* **SSH Access:** `ssh yuhan@192.168.219.20`

#### Services on `docker-host`

| Service | Internal Port | External Port | Access URL (from LAN) |
| :--- | :--- | :--- | :--- |
| **Portainer** | `9000` | `9000` | `http://192.168.219.20:9000` |
| **n8n** | `5678` | `5678` | `http://192.168.219.20:5678` |

### 4.2. Guest 101: `llm-server`

* **Type:** Virtual Machine
* **IP Address:** `192.168.219.130`
* **OS:** Ubuntu Server 24.04
* **Allocated Resources:** 4 CPU Cores, 4GB (Min) - 8GB (Max) RAM, NVIDIA RTX 2060
* **Purpose:** Dedicated, GPU-accelerated server for LLM inference.
* **SSH Access:** `ssh yuhan@192.168.219.130`

#### Services on `llm-server`

| Service | Port | Access URL (from LAN) |
| :--- | :--- | :--- |
| **Ollama API** | `11434` | `http://192.168.219.130:11434` |

---

## 5. Service Endpoint Quick Reference

This is a summary of all available service endpoints for use in other projects.

| Service Name | Access Endpoint |
| :--- | :--- |
| **Proxmox Web UI** | `https"//192.168.219.10:8006` |
| **Portainer (Docker UI)** | `http://192.168.219.20:9000` |
| **n8n (Workflows)** | `http://192.168.219.20:5678` |
| **Ollama (LLM API)** | `http://192.168.219.130:11434` |
