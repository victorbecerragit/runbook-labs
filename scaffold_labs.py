from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

NotebookSpec = tuple[str, str, str]
LabConfig = dict[str, str | list[NotebookSpec]]

LABS: dict[str, LabConfig] = {
    "rag-core": {
        "description": "Learn the basics of ingestion, chunking, and retrieval.",
        "requirements": "langchain==0.1.0\nchromadb==0.4.22\n",
        "notebooks": [
            ("00-intro.ipynb", "RAG Core: Introduction", "Understand the RAG architecture."),
            ("01-ingestion.ipynb", "RAG Core: Ingestion", "Read files, chunk text, and populate a vector store."),
            ("02-retrieval.ipynb", "RAG Core: Retrieval", "Query the vector store and pass context to an LLM."),
        ],
    },
    "bedrock-foundation-models": {
        "description": "Invoke Amazon Bedrock foundation models using boto3.",
        "requirements": "boto3>=1.34.14\n",
        "notebooks": [
            ("00-intro.ipynb", "Amazon Bedrock Foundation Models: Introduction", "Introduction to Amazon Bedrock."),
            ("01-invoke-model.ipynb", "Amazon Bedrock Foundation Models: Invoke", "Invoke a foundation model and process the response."),
        ],
    },
    "rag-evaluation": {
        "description": "Implement metrics to assess RAG quality.",
        "requirements": "ragas==0.0.22\n",
        "notebooks": [
            ("00-intro.ipynb", "RAG Evaluation: Introduction", "Understand why evaluation is necessary."),
            ("01-metrics.ipynb", "RAG Evaluation: Metrics", "Compute context precision and faithfulness."),
        ],
    },
    "rag-observability": {
        "description": "Trace execution and monitor RAG pipelines.",
        "requirements": "langsmith==0.0.83\n",
        "notebooks": [
            ("00-intro.ipynb", "Observability: Introduction", "Learn the importance of tracing."),
            ("01-traces.ipynb", "Observability: Traces", "Review generated trace ids and latencies."),
        ],
    },
    "bedrock-kb": {
        "description": "Set up fully managed RAG with AWS Bedrock.",
        "requirements": "boto3==1.34.14\n",
        "notebooks": [
            ("00-intro.ipynb", "Bedrock KB: Introduction", "Understand the managed Bedrock KB offering."),
            ("01-kb-setup.ipynb", "Bedrock KB: Setup and Query", "Synchronize data and run RetrieveAndGenerate."),
        ],
    },
    "bedrock-agents": {
        "description": "Build intelligent agents with tools using AWS Bedrock.",
        "requirements": "boto3==1.34.14\n",
        "notebooks": [
            ("00-intro.ipynb", "Bedrock Agents: Intro", "Understand autonomous agents."),
            ("01-agent-tools.ipynb", "Bedrock Agents: Tools", "Define action groups and test agent interactions."),
        ],
    },
    "bedrock-guardrails": {
        "description": "Create and test Amazon Bedrock Guardrails for prompt safety and PII protection.",
        "requirements": "boto3>=1.34.14\nipython>=8.0.0\n",
        "notebooks": [
            (
                "00-guardrails-exercise.ipynb",
                "Amazon Bedrock Guardrails Exercise",
                "Create and validate Bedrock Guardrails against unsafe prompts and sensitive data.",
            ),
        ],
    },
    "foundations": {
        "description": "Repository onboarding notebooks and a reusable template for new labs.",
        "requirements": "pandas>=2.0.0\n",
        "notebooks": [
            ("00-environment-check.ipynb", "Runbook Labs Intro", "Verify that the notebook environment is working."),
            ("01-new-lab-template.ipynb", "Lab Template", "Use this notebook as a base for new labs."),
        ],
    },
    "langchain-intro": {
        "description": "Introduction to LangChain concepts, chains, prompts, and application patterns.",
        "requirements": "langchain>=0.2.0\n",
        "notebooks": [
            ("00-langchain-overview.ipynb", "LangChain", "Learn the fundamentals of the LangChain framework."),
        ],
    },
    "prompt-engineering": {
        "description": "Hands-on prompt engineering patterns, in-context learning, and prompt templates.",
        "requirements": "langchain>=0.2.0\n",
        "notebooks": [
            ("00-prompt-templates.ipynb", "In-Context Engineering and Prompt Templates", "Practice prompt design and templating strategies."),
        ],
    },
    "rag-huggingface": {
        "description": "RAG workflows using Hugging Face models and retrieval-based QA patterns.",
        "requirements": "transformers>=4.0.0\nsentence-transformers>=2.0.0\n",
        "notebooks": [
            ("00-rag-huggingface.ipynb", "Enhance LLMs using RAG and Hugging Face", "Build a retrieval-augmented QA workflow with Hugging Face tools."),
        ],
    },
    "rag-pytorch": {
        "description": "Build retrieval-augmented generation pipelines with PyTorch and embeddings.",
        "requirements": "torch>=2.0.0\ntransformers>=4.0.0\n",
        "notebooks": [
            ("00-rag-pytorch.ipynb", "RAG with PyTorch", "Implement a RAG flow using PyTorch components and embeddings."),
        ],
    },
}

ROOT_DIRS = [
    Path("docs"),
    Path("shared/python/utils"),
    Path("shared/python/rag"),
    Path("shared/python/bedrock"),
    Path("shared/prompts"),
    Path("shared/sample-data"),
    Path("shared/schemas"),
    Path(".devcontainer/base"),
    Path(".devcontainer/rag"),
    Path(".devcontainer/bedrock"),
    Path(".devcontainer/langchain"),
    Path(".devcontainer/pytorch-rag"),
]

SEED_FILES: dict[Path, str] = {
    Path(".gitignore"): """__pycache__/\n*.pyc\n.ipynb_checkpoints/\n.env\n.venv/\nvenv/\noutputs/*\n!outputs/.gitkeep\ndata/*\n!data/.gitkeep\n*.log\n""",
    Path("shared/python/requirements.txt"): "jupyterlab==4.0.10\npython-dotenv==1.0.0\n",
    Path("shared/python/utils/__init__.py"): "",
    Path("shared/python/utils/logging.py"): """import logging\n\n\ndef get_logger(name: str) -> logging.Logger:\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s - %(name)s - %(levelname)s - %(message)s\",\n    )\n    return logging.getLogger(name)\n""",
    Path("shared/python/rag/__init__.py"): "",
    Path("shared/python/rag/helpers.py"): """def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:\n    \"\"\"Split text into overlapping chunks.\"\"\"\n    step = max(chunk_size - overlap, 1)\n    return [text[i : i + chunk_size] for i in range(0, len(text), step)]\n""",
    Path("shared/python/bedrock/__init__.py"): "",
    Path("shared/python/bedrock/client.py"): """import boto3\n\n\ndef get_bedrock_runtime():\n    \"\"\"Return a boto3 Bedrock runtime client.\"\"\"\n    return boto3.client(\"bedrock-runtime\")\n""",
    Path("shared/prompts/system_prompts.txt"): "You are a helpful, accurate, and concise AI assistant.\n",
    Path("shared/schemas/document.json"): json.dumps(
        {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "content": {"type": "string"},
            },
        },
        indent=2,
    )
    + "\n",
    Path("shared/sample-data/company_info.json"): json.dumps(
        [{"dept": "Engineering", "info": "Builds the product."}],
        indent=2,
    )
    + "\n",
    Path(".devcontainer/base/Dockerfile"): "FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye\n",
    Path(".devcontainer/rag/Dockerfile"): "FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye\n",
    Path(".devcontainer/bedrock/Dockerfile"): "FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye\n",
    Path(".devcontainer/langchain/Dockerfile"): "FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye\n",
    Path(".devcontainer/pytorch-rag/Dockerfile"): "FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye\n",
    Path(".devcontainer/base/devcontainer.json"): json.dumps(
        {
            "name": "Base Lab Environment",
            "build": {"dockerfile": "Dockerfile"},
            "customizations": {
                "vscode": {
                    "extensions": [
                        "ms-python.python",
                        "ms-python.vscode-pylance",
                        "ms-toolsai.jupyter",
                    ],
                    "settings": {"python.defaultInterpreterPath": "/usr/local/bin/python"},
                },
                "codespaces": {"openFiles": ["README.md"]},
            },
            "postCreateCommand": "make setup",
        },
        indent=4,
    ),
    Path(".devcontainer/rag/devcontainer.json"): json.dumps(
        {
            "name": "RAG Lab Environment",
            "build": {"dockerfile": "Dockerfile"},
            "customizations": {
                "vscode": {
                    "extensions": [
                        "ms-python.python",
                        "ms-python.vscode-pylance",
                        "ms-toolsai.jupyter",
                    ]
                },
                "codespaces": {"openFiles": ["labs/rag-core/README.md"]},
            },
            "postCreateCommand": "make setup && pip install -r labs/rag-core/requirements.txt",
        },
        indent=4,
    ),
    Path(".devcontainer/bedrock/devcontainer.json"): json.dumps(
        {
            "name": "AWS Bedrock Lab Environment",
            "features": {"ghcr.io/devcontainers/features/aws-cli:1": {}},
            "build": {"dockerfile": "Dockerfile"},
            "customizations": {
                "vscode": {
                    "extensions": [
                        "ms-python.python",
                        "ms-python.vscode-pylance",
                        "ms-toolsai.jupyter",
                        "amazonwebservices.aws-toolkit-vscode",
                    ]
                },
                "codespaces": {"openFiles": ["labs/bedrock-kb/README.md"]},
            },
            "postCreateCommand": "make setup && pip install -r labs/bedrock-kb/requirements.txt",
        },
        indent=4,
    ),
    Path(".devcontainer/langchain/devcontainer.json"): json.dumps(
        {
            "name": "LangChain Lab Environment",
            "build": {"dockerfile": "Dockerfile"},
            "customizations": {
                "vscode": {
                    "extensions": [
                        "ms-python.python",
                        "ms-python.vscode-pylance",
                        "ms-toolsai.jupyter",
                    ]
                },
                "codespaces": {"openFiles": ["labs/langchain-intro/README.md"]},
            },
            "postCreateCommand": "make setup && pip install -r labs/langchain-intro/requirements.txt && pip install -r labs/prompt-engineering/requirements.txt",
        },
        indent=4,
    ),
    Path(".devcontainer/pytorch-rag/devcontainer.json"): json.dumps(
        {
            "name": "PyTorch and RAG Lab Environment",
            "build": {"dockerfile": "Dockerfile"},
            "customizations": {
                "vscode": {
                    "extensions": [
                        "ms-python.python",
                        "ms-python.vscode-pylance",
                        "ms-toolsai.jupyter",
                    ]
                },
                "codespaces": {"openFiles": ["labs/rag-pytorch/README.md"]},
            },
            "postCreateCommand": "make setup && pip install -r labs/rag-pytorch/requirements.txt && pip install -r labs/rag-huggingface/requirements.txt && pip install -r labs/rag-core/requirements.txt",
        },
        indent=4,
    ),
}


def generate_notebook(title: str, objective: str) -> str:
    nb = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n\n",
                    f"Objective: {objective}\n\n",
                    "## Setup\n",
                    "Run the next cell to discover the repository root and shared modules.\n",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "from pathlib import Path\n",
                    "import sys\n\n",
                    "repo_root = Path.cwd().resolve().parents[2]\n",
                    "shared_python = repo_root / 'shared' / 'python'\n",
                    "if str(shared_python) not in sys.path:\n",
                    "    sys.path.append(str(shared_python))\n\n",
                    "print(f'Repository root: {repo_root}')\n",
                    "print(f'Shared Python path: {shared_python}')\n",
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Execution\n\nAdd your lab logic here.\n"],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# TODO: Implement lab step\n"],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Next Steps\n\nReview outputs and continue with the next notebook.\n"],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.11",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    return json.dumps(nb, indent=2)


def ensure_dir(path: Path, dry_run: bool) -> bool:
    if path.exists():
        return False
    if not dry_run:
        path.mkdir(parents=True, exist_ok=True)
    return True


def write_text(path: Path, content: str, overwrite: bool, dry_run: bool) -> str:
    existed = path.exists()
    if existed and not overwrite:
        return "skipped"

    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return "updated" if existed else "created"


def scaffold_repo(overwrite: bool = False, dry_run: bool = False) -> None:
    created_dirs = 0
    written_files = 0
    skipped_files = 0

    for relative_dir in ROOT_DIRS:
        created_dirs += int(ensure_dir(REPO_ROOT / relative_dir, dry_run=dry_run))

    for lab_name, config in LABS.items():
        for subdir in ("notebooks", "data", "configs", "outputs"):
            created_dirs += int(ensure_dir(REPO_ROOT / "labs" / lab_name / subdir, dry_run=dry_run))

        lab_readme = REPO_ROOT / "labs" / lab_name / "README.md"
        result = write_text(
            lab_readme,
            f"# {lab_name}\n\n{config['description']}\n",
            overwrite=overwrite,
            dry_run=dry_run,
        )
        written_files += int(result != "skipped")
        skipped_files += int(result == "skipped")

        requirements = REPO_ROOT / "labs" / lab_name / "requirements.txt"
        result = write_text(
            requirements,
            str(config["requirements"]),
            overwrite=overwrite,
            dry_run=dry_run,
        )
        written_files += int(result != "skipped")
        skipped_files += int(result == "skipped")

        for subdir in ("data", "configs", "outputs"):
            gitkeep = REPO_ROOT / "labs" / lab_name / subdir / ".gitkeep"
            result = write_text(gitkeep, "", overwrite=overwrite, dry_run=dry_run)
            written_files += int(result != "skipped")
            skipped_files += int(result == "skipped")

        notebooks = config.get("notebooks", [])
        if isinstance(notebooks, list):
            for notebook_name, title, objective in notebooks:
                notebook_path = REPO_ROOT / "labs" / lab_name / "notebooks" / str(notebook_name)
                result = write_text(
                    notebook_path,
                    generate_notebook(str(title), str(objective)),
                    overwrite=overwrite,
                    dry_run=dry_run,
                )
                written_files += int(result != "skipped")
                skipped_files += int(result == "skipped")

    for relative_path, content in SEED_FILES.items():
        result = write_text(REPO_ROOT / relative_path, content, overwrite=overwrite, dry_run=dry_run)
        written_files += int(result != "skipped")
        skipped_files += int(result == "skipped")

    print(f"Repository root: {REPO_ROOT}")
    print(f"Directories created: {created_dirs}")
    print(f"Files written: {written_files}")
    print(f"Files skipped: {skipped_files}")
    if dry_run:
        print("Dry run complete. No files were modified.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold or repair the notebook lab repository structure.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing scaffold files and notebooks.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be created without writing files.",
    )
    args = parser.parse_args()
    scaffold_repo(overwrite=args.force, dry_run=args.dry_run)


if __name__ == "__main__":
    main()

