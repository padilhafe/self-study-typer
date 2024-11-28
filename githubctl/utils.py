import csv
from csv import DictWriter
from sys import stdout
from typing import List
from options import OutputOption

def print_beauty(list_of_dict: List[dict], output_format: OutputOption):
    if output_format == OutputOption.csv:
        field_names = list_of_dict[0].keys()
        writer = DictWriter(stdout, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(list_of_dict)