# BT2Automata Experiments - Linux (Debian) x86_64

Local installation instructions for the HSCC25 Repetability Evaluation for submission #40 *BT2Automata: Expressing Behavior Trees as Automata for Formal Control Synthesis*

This branch is for x86 Debian Linux based systems. Choose a branch that best fits your systems OS.

## Prequisites

### **OS**
Ubuntu Desktop 22.04.5 LTS (recommended)

### **Environment**
[Miniconda](https://docs.anaconda.com/miniconda/)

## Local Installation Instructions

Create a conda environment:
```bash
conda create -n "bt2automata" python=3.10
```
Activate the environment and install the required packages:
```bash
conda activate bt2automata
pip install -r requirements.txt
```