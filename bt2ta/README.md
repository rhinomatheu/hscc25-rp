# BT2Automata Experiment: Mobile Robot Path Planning with UPPAAL

## Directory Structure

```
bt2ta
├── main.py
├── leaf_node_templates.xml
├── README.md
├── UPPAAL Instructions.pdf
└── bt2ta
    └── bt2ta.py
```

## Running Evaluations

### File Descriptions

1. `main.py`: Python script for composing the BT equivalent automaton from the leaf node automata.

2. `leaf_node_templates.xml`: An XML file containing the UPPAAL leaf node templates for the leaf node automata.

3. `bt2ta/bt2ta.py`: The main library containing the timed automata class and translation algorithms.

4. `UPPAAL Instructions.pdf`: A guide to activating UPPAAL and synthesizing the satisfying trace.

## Running

To execute the main script, open a terminal and activate the conda environment `bt2automata`.

From the base directory `/bt2ta`, run the command:

```bash
python main.py
```

Doing so will create the composed automaton from experiment 6.1 and generate a new file `BT_converted.xml`.

Follow the guide `UPPAAL Instructions.pdf` to open the generated file in UPPAAL and follow the steps to verify the BT and generate a control.