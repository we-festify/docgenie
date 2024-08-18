import click
import json
from ..main import main
import inquirer
from ..models import supported_models

@click.group()
def cli():
    """Docgenie CLI tool."""
    pass

@cli.command()
def build():
    """Build documentation using docgenie.config.json."""
    click.echo("\u001b[36mBuilding documentation using docgenie...\u001b[0m\n")
    main()

@cli.command()
def init():
    """Initialize docgenie configuration."""
    print("\u001b[36mInitializing docgenie configuration...\u001b[0m\n")

    agent_names = list(supported_models.keys())
    docs_types = ["general", "api", "readme", "model"]
    output_formats = ["markdown", "html", "text"]
    
    questions = [
        inquirer.Text('root_dir', message="Enter the root directory of your project", default="."),
        inquirer.List('agent_name', message="Select the agent to use", choices=agent_names, default="gemini-1.5-flash"),
        inquirer.List('docs_type', message="Select the type of documentation", choices=docs_types, default="general"),
        inquirer.Text('dir', message="Enter the directory to generate documentation for", default="."),
        inquirer.Text('include', message="Enter the include patterns", default=""),
        inquirer.Text('exclude', message="Enter the exclude patterns", default=""),
        inquirer.Text('output', message="Enter the output directory", default="."),
        inquirer.Text('depth', message="Enter the search depth", default="3", validate=lambda _, x: x.isdigit()),
        inquirer.List('format', message="Select the output format", choices=output_formats, default="markdown"),
        inquirer.Text('prompt', message="Enter any additional prompt", default="")
    ]

    answers = inquirer.prompt(questions)
    
    if answers is not None:
        config = {
            "root_dir": answers["root_dir"],
            "agent": {
                "name": answers["agent_name"],
                "config": {}
            },
            "rules": [
                {
                    "type": answers["docs_type"],
                    "dir": answers["dir"],
                    "include": answers["include"].split(","),
                    "exclude": answers["exclude"].split(","),
                    "output": answers["output"],
                    "depth": int(answers["depth"]),
                    "format": answers["format"],
                    "prompt": answers["prompt"]
                }
            ]
        }
    else:
        config = None

    if config is not None:
        with open("docgenie.config.json", "w") as file:
            json.dump(config, file, indent=4)
        click.echo("\u001b[36m\ndocgenie.config.json created successfully.\u001b[0m")
        click.echo("You can now run 'docgenie build' to generate documentation.")
    else:
        click.echo("\u001b[31mError initializing docgenie configuration.\u001b[0m")
