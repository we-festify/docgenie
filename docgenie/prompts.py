__prompts_by_docs_type = {
    "general": """
Generate concise documentation for the code given, including an introduction to the project, setup instructions, usage examples, and a summary of the code structure whatever is applicable.
Ensure the documentation is clear and easy to follow for new developers and users.
""",
    "readme": """
Create a README file for the project based on the code provided.
Include an introduction to the project, setup instructions, usage examples, and a summary of the code structure.
Ensure the README is clear and easy to follow for new developers and users.
You can use various markdown features to make the README more immersive and informative.
""",
    "model": """
Use tables, bullet points, and diagrams(mermaid) wherever necessary to explain the code.
Please don't write the code itself in the documentation, and don't expose an explanation of the libraries used.
""",
    "api": """
Use tables, bullet points, and diagrams(mermaid) if required to explain the API.
You can refer to the example provided for the Sponsor API documentation.:
```md
# Sponsor API Documentation

This document outlines the Sponsor API, providing details about the endpoints, request/response payloads, and authorization requirements.

## Table of Contents

- [Introduction](#introduction)
- [Authorization](#authorization)
  - [Permissions](#permissions)
- [Endpoints](#endpoints)
  - [POST /sponsor](#post-sponsor)
  - [GET /sponsor/:id](#get-sponsor-id)
  - [GET /sponsor](#get-sponsor)
  - [PATCH /sponsor/:id](#patch-sponsor-id)
  - [DELETE /sponsor/:id](#delete-sponsor-id)

## Introduction

The Sponsor API is responsible for managing sponsor data, including creation, retrieval, update, and deletion. This API is designed for internal use and requires proper authentication and authorization.

## Authorization

The Sponsor API requires authentication using an access token obtained through the authentication service. Additionally, specific permissions are required to access individual endpoints.

### Permissions:

- **sponsor:create:** Permission to create new sponsors.
- **sponsor:read:** Permission to read sponsor data.
- **sponsor:update:** Permission to update existing sponsors.
- **sponsor:delete:** Permission to delete existing sponsors.

## Endpoints

### POST /sponsor

**Description:** Creates a new sponsor.

**Request Body:**

| Field      | Type   | Description                                                          |
| ---------- | ------ | -------------------------------------------------------------------- |
| name       | string | The name of the sponsor.                                             |
| websiteUrl | string | The URL of the sponsor's website.                                    |
| logoUrl    | string | The URL of the sponsor's logo.                                       |
| type       | string | The type of sponsor (e.g., "Gold", "Silver").                        |
| priority   | number | The priority of the sponsor (higher priority sponsors appear first). |

**Response:**

- **201 Created:**
  - **Body:**
    ```json
    {
      "sponsor": {
        "_id": "string",
        "name": "string",
        "websiteUrl": "string",
        "logoUrl": "string",
        "type": "string",
        "priority": "number",
        "createdAt": "date",
        "updatedAt": "date"
      }
    }
    ```
- **400 Bad Request:** Invalid request body.
- **401 Unauthorized:** Unauthorized access.
- **403 Forbidden:** Insufficient permissions.

**Permissions:** `sponsor:create`
```
""",
}

__prompts_by_output_format = {
    "markdown": """
The documentation should be written in Markdown format.
Use headings, lists, tables, code blocks, and other Markdown features to structure the content if needed.
""",
    "html": """
The documentation should be written in HTML format.
Use appropriate HTML tags to structure the content, including headings, lists, tables, and code blocks.
""",
    "text": """
The documentation should be written in plain text format.
Use paragraphs, bullet points, and code blocks to structure the content if needed.
""",
}

def generatePrompt(code: str, docs_type: str, output_format: str, additional_prompt: str = "") -> str:
    docsPrompt = __prompts_by_docs_type.get(docs_type, "")
    outputPrompt = __prompts_by_output_format.get(output_format, "")

    prompt = f"""
You are a professional technical writer tasked with documenting a code.
The code is provided as input, and you must generate a detailed documentation based on the code structure and functionality.
Don't include your personal recommendations or opinions in the documentation, or any information related to future updates, versions, etc unless specified.
{docsPrompt}
{outputPrompt}
Please write the documentation based on the code provided.
Code:
{code}
{additional_prompt}
"""
    return prompt