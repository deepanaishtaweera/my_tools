# PDF Combiner

A Python tool to combine multiple PDF files from a folder into a single PDF file.

## Quick Setup

```bash
# Install Python 3.12 with uv
uv install python 3.12

# Create virtual environment
uv venv --python 3.12 .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python tools/pdf_combiner.py ./documents combined.pdf

# With verbose output
python tools/pdf_combiner.py ./pdfs output -v

# Show help
python tools/pdf_combiner.py --help
```

## Features

- Combines all PDF files from a folder in alphabetical order
- Automatic .pdf extension handling
- Verbose output option
- Built-in help and version info
