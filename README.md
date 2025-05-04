# multilingual-nlp-homeworks
This readme is focused on the LM-based approach.
The instructions for the Non-LM-based approach can be found in the corresponding subfolder.

## Training Logs
The training logs can be found on [WandB](https://wandb.ai/kubach/mnlp-h1-lm?nw=66ubndiosr).

## Install

### Prerequirements
Developed using Python 3.13, but compatible for >=3.10.
Jupyter is required to be already installed on your machine.

### Using uv
Recommended, because more modern and for better reproducible projects: 
https://docs.astral.sh/uv/getting-started/installation/

Install all dependencies from pyproject.toml and uv.lock:
```bash
# install
uv sync
# run a jupyter server locally
uv run --with jupyter jupyter lab
# done - ready to run the scripts of this project
# optional: add Huggingface HF_TOKEN as env var
export HF_TOKEN=your_token
```
Your IDE can be connected with the started jupyter server.

### Using pip and venv
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Development
Project setup via uv is used and recommended here but for compatibility to tools like pip a requirements.txt file
can be created via `uv export -o requirements.txt`.

Note: For running commands inside a cell, a custom kernel is required.

### Most important UV commands

```bash
# add dependency
uv add torch
# remove dependency
uv remove torch
```
