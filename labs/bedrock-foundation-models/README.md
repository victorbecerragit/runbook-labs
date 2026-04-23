# Bedrock Foundation Models Lab

This lab demonstrates how to invoke Amazon Bedrock foundation models using the legacy `boto3` runtime and shared Python utilities.

## Overview

In this lab, you will learn how to:
- Use the shared Bedrock client from `shared/python/bedrock/client.py`.
- Invoke the `amazon.titan-text-express-v1` model for text generation.
- Handle model responses and extract generated text.

## Structure

- `notebooks/01-invoke-model.ipynb`: Primary exercise for model invocation.
- `configs/`: (Reserved) Configuration files for model parameters.
- `data/`: (Reserved) Sample prompts and input data.
- `outputs/`: (Reserved) Generated model responses.

## Getting Started

1. Set up your AWS credentials.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `notebooks/01-invoke-model.ipynb` and follow the instructions.

