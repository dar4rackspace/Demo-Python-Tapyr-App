#!/bin/bash
# This script is for running quality checks in GitHub Actions.
# It runs tests, and type checks with pyright.

set -e # Exit immediately if a command exits with a non-zero status.

echo "Running pytest for unit tests..."
uv run pytest

echo "Running pyright for type checking..."
uv run pyright tapyr_llm_demo
