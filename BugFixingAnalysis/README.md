# Framework for evaluating real-world bug-fixing capabilities of LLMs

A benchmarking framework designed to evaluate the capability of Large Language Models (specifically Google Gemini) to fix real-world software defects in Python repositories.

This project was developed as part of my BSc thesis at **Budapest University of Technology and Economics (BME VIK)**.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Platform](https://img.shields.io/badge/Platform-WSL2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview

While LLMs excel at generating new code ("greenfield" development), repairing existing bugs in large, complex codebases ("brownfield" maintenance) remains an open challenge. This framework provides an automated pipeline to:

1.  **Mine** real bug-fix pairs from GitHub history.
2.  **Construct** context-aware prompts using static analysis and Retrieval Augmented Generation (RAG).
3.  **Generate** and apply patches using LLMs (Google Gemini 3 Pro Preview).
4.  **Validate** fixes by reproducing historical environments and running the original test suites.

## Requirements

This tool is designed to run in a **Linux** environment (specifically in WSL2).

*   **OS:** Windows 10/11 with WSL2 (Ubuntu 22.04/24.04 recommended).
*   **Python:** Version 3.12+
*   **System Dependencies:** `git`

## Installation

1.  **Clone the repository (inside WSL):**
    ```bash
    git clone https://github.com/bmeaut/GenAiAutomationExperiments.git
    cd BugFixingAnalysis
    ```

3.  **Set up the virtual environment:**
    ```bash
    # Create virtual environment
    python -m venv .venv
    source .venv/bin/activate
    
    # Upgrade pip
    pip install --upgrade pip
    
    # This project uses `pip-tools` for dependency management.
    pip install pip-tools
    pip-compile requirements.in
    pip install -r requirements.txt
    ```

## Configuration

1.  **API Keys:**
    Create a `.env` file in the `llm_bug_analysis` directory. You will need a GitHub token for corpus building and a Google API key for the LLM.
    Fill in your keys:
    ```ini
    GITHUB_TOKEN=your_github_pat_here
    GOOGLE_API_KEY=your_gemini_key_here
    ```

2.  **Target Repositories:**
    Edit `config.json` or use the GUI to add or remove the GitHub repositories you wish to analyze.
    ```json
    {
      "repositories": [
        "https://github.com/pallets/flask",
        "https://github.com/psf/requests"
      ]
    }
    ```

## Usage

To launch the Graphical User Interface:

```bash
python -m llm_bug_analysis.main