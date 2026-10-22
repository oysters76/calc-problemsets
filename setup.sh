#!/bin/bash
set -e

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Installing dependencies..."
.venv/bin/pip install -r requirements.txt

echo "Configuring git hooks..."
git config core.hooksPath hooks

echo "Done! Use .venv/bin/python to run scripts."
