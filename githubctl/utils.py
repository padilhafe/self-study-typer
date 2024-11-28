import csv
from csv import DictWriter
from sys import stdout
from typing import List
from options import OutputOption
from rich import print_json
from rich.table import Table
from rich.console import Console
import json

def print_beauty(list_of_dict: List[dict], output_format: OutputOption):
    if output_format == OutputOption.csv:
        field_names = list_of_dict[0].keys()
        writer = DictWriter(stdout, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(list_of_dict)

    elif output_format == OutputOption.table:
        table = Table()
        headers = list_of_dict[0].keys()
        table.add_column("")

        for header in headers:
            table.add_column(str(header))

        for repo in list_of_dict:
            table.add_row(*[str((list_of_dict.index(repo) + 1))] + [str(row) for row in repo.values()])

        console = Console()
        console.print(table)



    else:
        print_json(json.dumps(list_of_dict))
