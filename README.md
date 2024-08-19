## Docgenie: Documentation Generation Tool

Docgenie is a powerful command-line tool that leverages advanced AI models to automatically generate comprehensive documentation for your projects. It supports various documentation types, including general documentation, README files, API documentation, and code model explanations.

### Installation

Docgenie requires Python 3.8.1 or higher. To install it, run the following command:

```bash
pip install docgenie
```

### Setup

1. **Initialize Configuration:**
   Run `docgenie init` to create a `docgenie.config.json` file in your project root directory. This file contains the configuration settings for Docgenie.

2. **Configure the AI Agent:**

   - **Custom API:** Select `custom-api` as the AI agent if you want to use your own API endpoint for documentation generation. You will need to provide the API URL, headers, and query parameters.
   - **Gemini:** Select `gemini-1.5-flash` as the AI agent to leverage Google's Gemini model. You will need to set the `DOCGENIE_MODEL_API_KEY` environment variable to your Gemini API key.

3. **Define Documentation Rules:**
   - **Type:** Select the type of documentation you want to generate for each rule (e.g., `general`, `readme`, `api`, `model`).
   - **Directory:** Specify the directory where the code files reside.
   - **Include Patterns:** Define patterns for files to be included in the documentation generation process (wildcards `*` and `?` are supported).
   - **Exclude Patterns:** Define patterns for files to be excluded from the documentation generation process (wildcards `*` and `?` are supported).
   - **Output Directory:** Specify the directory where the generated documentation files will be saved.
   - **Search Depth:** Set the depth of the directory search for code files.
   - **Output Format:** Choose the output format for the documentation (e.g., `markdown`, `html`, `text`).
   - **Prompt:** Add any additional instructions or context for the AI agent.

**Example `docgenie.config.json`:**

```json
{
  "root_dir": ".",
  "agent": {
    "name": "gemini-1.5-flash",
    "config": {}
  },
  "rules": [
    {
      "type": "readme",
      "dir": "src",
      "include": ["*.py"],
      "exclude": [],
      "output": "docs",
      "depth": 3,
      "format": "markdown",
      "prompt": ""
    }
  ]
}
```

### Usage

To generate documentation, run the following command:

```bash
docgenie build
```

Docgenie will process your code files based on the defined rules and generate documentation in the specified output directory.

### Code Structure

The code is structured as follows:

- **docgenie/cli/**init**.py:** Defines the command-line interface (CLI) for Docgenie, including the `build` and `init` commands.
- **docgenie/models/**init**.py:** Defines the supported AI models.
- **docgenie/models/gemini.py:** Implements the Gemini model for documentation generation.
- **docgenie/models/custom_api.py:** Implements the Custom API model for documentation generation.
- **docgenie/main.py:** Contains the core logic for loading configuration, generating prompts, and generating documentation.
- **docgenie/prompts.py:** Defines the prompts used to interact with the AI models.
- **docgenie/utils/file.py:** Provides utility functions for reading and writing files.
- **docgenie/utils/patterns.py:** Provides functionality for matching files based on patterns.
- **docgenie/utils/languages.py:** Provides functions to extract import paths from code based on the language.
- **docgenie/model.py:** Handles the loading and interaction with AI models.
- **docgenie/utils/terminal.py:** Provides functions for displaying colored text in the terminal.

### Configuration Parameters

**`docgenie.config.json`**:

- **`root_dir`**: Specifies the root directory of the project. Defaults to the current directory.
- **`agent`**:
  - **`name`**: The name of the AI agent to use. Supported values: `gemini-1.5-flash`, `custom-api`.
  - **`config`**:
    - **For `custom-api`**:
      - **`url`**: The URL of the custom API endpoint.
      - **`headers`**: A dictionary of headers to be sent with the API request.
      - **`query`**: A dictionary of query parameters to be sent with the API request.
    - **For `gemini-1.5-flash`**: No specific configuration parameters are required.
- **`rules`**: An array of objects representing the documentation rules. Each rule object has the following properties:
  - **`type`**: The type of documentation to generate. Supported values: `general`, `readme`, `api`, `model`.
  - **`dir`**: The directory where the code files reside.
  - **`include`**: An array of patterns for files to be included in the documentation generation process.
  - **`exclude`**: An array of patterns for files to be excluded from the documentation generation process.
  - **`output`**: The directory where the generated documentation files will be saved.
  - **`depth`**: The depth of the directory search for code files.
  - **`format`**: The output format for the documentation. Supported values: `markdown`, `html`, `text`.
  - **`prompt`**: Additional instructions or context for the AI agent.

### Environment Variables

- **`DOCGENIE_MODEL_API_KEY`**: The API key for the Gemini model.

### Contributing

Contributions are welcome! Please follow the standard contribution guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and write unit tests.
4. Submit a pull request.

### License

Docgenie is licensed under the MIT License.

The documentation is generated using AI by docgenie. If you found any issues, please report them to the team.
