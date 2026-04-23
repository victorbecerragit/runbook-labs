# LLM Runbook Labs

A comprehensive collection of Jupyter-based LLM labs designed to run seamlessly in GitHub Codespaces. This monorepo provides isolated environments and reusable patterns for mastering RAG and AWS Bedrock workflows.

## Lab Catalog

| Lab | Path | Description |
|---|---|---|
| RAG Core | [labs/rag-core/](labs/rag-core/) | Fundamentals of Retrieval-Augmented Generation (ingestion, retrieval, generation). |
| RAG Evaluation | [labs/rag-evaluation/](labs/rag-evaluation/) | Techniques and frameworks for evaluating RAG pipeline quality. |
| RAG Observability | [labs/rag-observability/](labs/rag-observability/) | Tracing, logging, and monitoring complex LLM applications. |
| Bedrock Knowledge Bases | [labs/bedrock-kb/](labs/bedrock-kb/) | Setup and usage of managed AWS Bedrock Knowledge Bases. |
| Bedrock Agents | [labs/bedrock-agents/](labs/bedrock-agents/) | Creating intelligent agents equipped with tools via AWS Bedrock. |
| Bedrock Foundation Models | [labs/bedrock-foundation-models/](labs/bedrock-foundation-models/) | Core Amazon Bedrock model invocation techniques. |
| Bedrock Guardrails | [labs/bedrock-guardrails/](labs/bedrock-guardrails/) | Create and test Bedrock Guardrails for blocked topics, PII, and prompt safety. |
| Foundations | [labs/foundations/](labs/foundations/) | Environment intro notebook and reusable lab template. |
| LangChain Intro | [labs/langchain-intro/](labs/langchain-intro/) | Introductory LangChain walkthrough and concepts. |
| Prompt Engineering | [labs/prompt-engineering/](labs/prompt-engineering/) | In-context prompting and prompt template techniques. |
| RAG with Hugging Face | [labs/rag-huggingface/](labs/rag-huggingface/) | Retrieval-augmented generation with Hugging Face tooling. |
| RAG with PyTorch | [labs/rag-pytorch/](labs/rag-pytorch/) | RAG implementation patterns using PyTorch. |

See [docs/catalog.md](docs/catalog.md) for detailed lab summaries.

## Working within GitHub Codespaces

This repository leverages the GitHub Codespaces multiple devcontainer feature. Here is a quick guide on how to interact with the environment:

**How to Open the Monorepo**
1. Navigate to the main repository page on GitHub.
2. Click the green `<> Code` button.
3. Switch to the **Codespaces** tab.
4. Click **...** (the three dots) and select **New with options...**

**Choosing the right devcontainer**
GitHub multiple Codespaces configurations are designed intentionally around modular development within monorepos:
- **`Base Lab Environment`**: The primary Python data science environment. Built for very basic notebooks.
- **`RAG Lab Environment`**: Geared toward `labs/rag-*/`. Opens the core RAG folder explicitly and will initialize its code modules, pulling in libraries common to your specific RAG labs such as `chromadb`, `langchain`, etc.
- **`LangChain Lab Environment`**: Tailored for `labs/langchain-intro/` and `labs/prompt-engineering/`, with the relevant prompt and LangChain dependencies installed automatically.
- **`PyTorch and RAG Lab Environment`**: Tailored for `labs/rag-pytorch/`, `labs/rag-huggingface/`, and other retrieval labs that benefit from PyTorch and transformer tooling.
- **`AWS Bedrock Lab Environment`**: Geared toward `labs/bedrock-*/`. By using the devcontainers extension map, this inherently installs `awscli` directly as a system-level feature via Microsoft's Devcontainer GHCR repository, enabling safe handling of your environment roles, AWS credentials, Bedrock clients, and the toolkit extension.

You'll be directed right away to a browser-based VS Code environment mapped reliably to your target lab space!

## Common Tasks

Use the `make` utility at the root of the repository:
- `make list-labs`: Show all labs.
- `make validate`: Check repo integrity.
- `make clean`: Clean up Python and Jupyter caches.
