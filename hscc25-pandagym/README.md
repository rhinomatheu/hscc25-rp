# BT2Automata Experiment: Panda Pick-and-Place Task

## Directory Structure

```
hscc25-pandagym
├── main.py
├── panda_specifications.py
├── README.md
├── tbt_monitor.py
├── tqc_pandp.zip
└── videos
    ├── rl-video-episode-0.mp4
    ├── rl-video-episode-0.mp4_slowmo.mp4
    ├── rl-video-episode-1.mp4
    ├── rl-video-episode-1.mp4_slowmo.mp4
    ├── ...
```

## Running Evaluations

### File Descriptions

1. `main.py`: Python script to run the evaluation of the trained RL model.

2. `panda_specifications.py`: Python script containing the inner logic STL for the leaf nodes.

3. `tbt_monitor.py`: Python script for the BT outer logic.

### Running

The general command usage is:

```
python main.py [-h] [--renderer RENDERER] [--n-rollouts N_ROLLOUTS]

Run trial episodes on trained TQC pick-and-place model.

options:
  -h, --help            show this help message and exit
  --renderer RENDERER   Options: 'Tiny' or 'OpenGL'. Use 'OpenGL' when using NVIDIA graphic cards. Default: 'Tiny'
  --n-rollouts N_ROLLOUTS
                        Number of episodes to run (an integer). Default: 10
```

Example: to run a specific evaluation of the trained TQC model on 20 test trials

```shell
$ python main.py --n-rollouts 20
```

For Intel-based graphic cards, there is a driver issue for colored rendering with OpenGL. Hence, the default renderer is set to 'Tiny'.
