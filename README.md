# BT2Automata Experiments - Windows x86_64

Local installation instructions for the HSCC25 Repetability Evaluation for submission #40 *BT2Automata: Expressing Behavior Trees as Automata for Formal Control Synthesis*

This branch is for x86 Windows based systems. Choose a branch that best fits your systems OS.

## Prequisites

### **OS**
Windows 11 (recommended)

### **Environment**
[Miniconda](https://docs.anaconda.com/miniconda/)

## Local Installation Instructions

Download this branch:
```bash
git clone https://github.com/rhinomatheu/hscc25-rp -b windows-x86
cd hscc25-rp
```

Create a conda environment:
```bash
conda create -n "bt2automata" python=3.10
```
Activate the environment and install the required packages:
```bash
conda activate bt2automata
pip install -r requirements.txt
```

## Usage

See the individual READMEs for both experiments in their respective folders, `/bt2ta` and `/hscc25-pandagym`. Both experiments make use of the same conda env `bt2automata`. Instructions for usage is provided in the repsective README.

## Note

UPPAAL requires a license to run, in this case an academic license is appropriate. The windows and linux versions may be preactivated with my license but the MacOS versions certainly are not. **The license key is included in the rebuttal and the instructions pdf.** I am not including it here for obvious reasons.