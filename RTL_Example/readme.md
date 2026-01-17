## Running Verilog Code Using Icarus Verilog and GTKWave

This section explains how to compile and simulate Verilog code using **Icarus Verilog** and view waveforms using **GTKWave**.

### Step 1: Write the Verilog Design and Testbench

Create your Verilog design file and testbench.

Example:

* Design file: `DFF.v`
* Testbench file: `tb_DFF.v`

You can use the sample D Flip-Flop code provided in this repository:

* `DFF.v`
* `tb_DFF.v`

---

### Step 2: Open Terminal and Navigate to Project Directory

Open the terminal and move to the directory where your Verilog files are stored.

```bash
cd path/to/your/project_directory
```

Your directory structure may look like this:

```text
project_folder/
├── DFF.v
├── tb_DFF.v
```

---

### Step 3: Compile the Verilog Files Using Icarus Verilog

Use the following command to compile the design and testbench:

```bash
iverilog -o dff_sim DFF.v tb_DFF.v
```

This command generates a simulation executable named `dff_sim`.

---

### Step 4: Run the Simulation

Execute the compiled file using:

```bash
vvp dff_sim
```

Any `$display` or `$monitor` statements will be shown in the terminal.

---

### Step 5: View Waveform Using GTKWave

Ensure the testbench contains waveform dump statements:

```verilog
$dumpfile("wave.vcd");
$dumpvars(0, tb_DFF);
```

After running the simulation, open the waveform file:

```bash
gtkwave wave.vcd
```

---

### Summary of Commands

```bash
iverilog -o dff_sim DFF.v tb_DFF.v
vvp dff_sim
gtkwave wave.vcd
```


















