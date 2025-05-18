import os
import json
import argparse
from pathlib import Path
import pandas as pd

#def flatten_json(y, parent_key='', sep='_', max_level=None, current_level=0):
#    items = {}
#    for k, v in y.items():
#        new_key = f"{parent_key}{sep}{k}" if parent_key else k
#        if isinstance(v, dict) and (max_level is None or current_level < max_level):
#            items.update(flatten_json(v, new_key, sep=sep, max_level=max_level, current_level=current_level+1))
#        else:
#            items[new_key] = v
#    return items


def flatten_json(y, parent_key='', sep='_', max_level=None, current_level=1):
    items = {}
    for k, v in y.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict) and (max_level is None or current_level < max_level):
            items.update(flatten_json(v, new_key, sep=sep, max_level=max_level, current_level=current_level + 1))
        else:
            # If we reached max_level, keep the remaining structure as JSON string
            if isinstance(v, dict) or isinstance(v, list):
                items[new_key] = json.dumps(v)
            else:
                items[new_key] = v
    return items


def process_json_file(file_path, explode_level):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON file: {file_path}")
            return

    # Ensure data is a list of records
    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list):
        print(f"Unsupported JSON format in file: {file_path}")
        return

    flattened_data = [flatten_json(record, max_level=explode_level) for record in data]
    df = pd.DataFrame(flattened_data)

    output_file = file_path.with_suffix('.xlsx')
    df.to_excel(output_file, index=False)
    print(f"Converted: {file_path} → {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert JSON files to XLSX with flattening options.")
    parser.add_argument(
        '--explode-level', 
        type=int, 
        default=None, 
        help="Specify the explode level (0 for no flattening, higher values for deeper flattening)."
    )
    args = parser.parse_args()

    current_dir = Path.cwd()
    json_files = list(current_dir.glob('*.json'))

    if not json_files:
        print("No JSON files found in the current directory.")
        return

    for json_file in json_files:
        process_json_file(json_file, args.explode_level)

if __name__ == "__main__":
    main()
