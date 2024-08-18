# Docgenie: Generate Documentation from Code

Docgenie is a command-line tool that leverages the power of large language models (LLMs) to automatically generate comprehensive documentation for your code.

## Getting Started

1. **Installation:**

   ```bash
   pip install docgenie
   ```

2. **Initialize Configuration:**

   ```bash
   docgenie init
   ```

   The `init` command guides you through setting up a `docgenie.config.json` file. This file stores your project's configuration, including:

   - **Root directory:** The base directory of your project.
   - **Agent:** The LLM model to use for generating documentation.
   - **Rules:** A set of rules defining the types of documentation to generate, the specific directories to process, and other customization options.

3. **Generate Documentation:**

   ```bash
   docgenie build
   ```

   This command uses the information in `docgenie.config.json` to analyze your code and generate documentation in the specified output formats.

## Usage Examples

### Basic Usage

The following example demonstrates generating general documentation for a project within the `my-project` directory:

```bash
# Initialize configuration
docgenie init

# Modify docgenie.config.json to include:
# - Root directory: my-project
# - Agent: gemini-1.5-flash
# - Rules:
#   - type: general
#     dir: .
#     include: *.py, *.js, *.ts
#     exclude: *test.py, *test.js
#     output: docs
#     depth: 3
#     format: markdown

# Build documentation
docgenie build
```

### Advanced Usage

Docgenie offers various options for customizing your documentation generation:

- **Document Types:** Generate different types of documentation like README files, API specifications, model explanations, and general overview documentation.
- **File Inclusion and Exclusion:** Control which files are included or excluded from documentation generation using patterns.
- **Output Formats:** Choose output formats like Markdown, HTML, and plain text.
- **Custom Prompts:** Add additional prompts to guide the LLM for specific documentation needs.

## Code Structure

The Docgenie project has the following code structure:

- **`docgenie`:** The main package containing core functionality:
  - **`cli`:** Command-line interface for interacting with Docgenie.
  - **`main`:** Main execution logic for documentation generation.
  - **`model`:** Abstraction layer for different LLM models.
  - **`prompts`:** Prompt templates for generating various types of documentation.
  - **`utils`:** Helper functions for file handling, pattern matching, and language-specific import analysis.
- **`docgenie.config.json`:** Configuration file for project settings.

## Contributing

Contributions to Docgenie are welcome! Please feel free to open issues or submit pull requests.

## License

Docgenie is licensed under the MIT License.

The documentation is generated using AI by docgenie. If you found any issues, please report them to the team.
