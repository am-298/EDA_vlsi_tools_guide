# RTL to GDS Flow – Open Source Tools

This repository contains information about open-source tools used in the VLSI **RTL to GDS** flow, including their purpose, installation steps, and key features.

## VLSI Design Flow

1. **Architecture**
   Defines the functionality, performance goals, and features of the circuit.

2. **RTL Simulation**
   RTL code is written to represent the architectural behavior and is verified using HDL languages such as **Verilog** or **VHDL**.

3. **RTL Synthesis**
   Converts the behavioral RTL code into a **gate-level netlist** using standard cell libraries.

4. **Floorplanning**
   Determines the chip area, aspect ratio, and placement of macros and major blocks.

5. **Placement**
   Places standard cells within the core area while optimizing timing, power, and congestion.

6. **Clock Tree Synthesis (CTS)**
   Creates a balanced clock distribution network to minimize skew and latency.

7. **Routing**
   Connects all cells and blocks using metal interconnects while following design rules.

8. **Static Timing Analysis (STA)**
   Analyzes timing to ensure there are no **setup or hold violations** before tape-out.

9. **LVS / DRC**

   * **LVS (Layout vs Schematic):** Ensures layout matches the netlist
   * **DRC (Design Rule Check):** Verifies compliance with foundry design rules

---

## Installation and Guide

Most of the tools used in this flow work on a **Linux environment**.

* **Linux users**: You can directly install and use the tools.
* **macOS users**: Most tools work without issues.
* **Windows users**: It is recommended to use a Linux environment via:

  * **WSL (Windows Subsystem for Linux)** *(preferred)*
  * or **Dual boot / Virtual Machine**

### Setting up Linux on Windows (WSL)

**WSL Installation (Windows)**

1. Open **PowerShell** as Administrator
2. Run:

   ```bash
   wsl --install
   ```
3. Restart your system
4. Launch **Ubuntu** from the Start menu and complete setup

Or Follow the steps shown in this YouTube tutorial:
   👉 [Installation](https://www.youtube.com/watch?v=zZf4YH4WiZo)

---

## RTL Development and Simulation

### RTL Coding

* Any text editor can be used to write **Verilog/SystemVerilog** code.
* Files should be saved with:

  * `.v` for Verilog
  * `.sv` for SystemVerilog
* **VS Code** is recommended for better readability and extensions, but it is optional.

### RTL Simulation

* **Icarus Verilog** is used to compile and simulate RTL code.
* It helps verify functional correctness of the design.

### Waveform Viewing

* To view simulation waveforms, install a waveform viewer such as **GTKWave**.

---

### Installing Icarus Verilog

Run the following commands in the terminal:

```bash
sudo apt update
sudo apt install iverilog
```

### Installing GTKWave

To install the waveform viewer, run:

```bash
sudo apt install gtkwave
```

### Verifying Installation

To verify that Icarus Verilog is installed correctly, run:

```bash
iverilog -V
```

If the version information is displayed, the installation was successful.

---
