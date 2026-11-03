import argparse
import csv
import json
import logging


def clean_rows(row:dict) -> dict:
    allowed_statuses = {"completed", "no-show", "cancelled"}
    minute = int(row["minutes"])
    if not row["provider"]:
        raise ValueError("Missing provider")
    if row["status"] not in allowed_statuses:
        raise ValueError("Invalid status")
    if minute < 0:
        raise ValueError("Negative value for minutes") 
    row["minutes"] = minute
    return row


if __name__ == "__main__":
    
    logging.basicConfig(filename="cleaning.log", level=logging.INFO, format="%(asctime)s %(message)s")

    parser = argparse.ArgumentParser(description="Clean a messy appointments CSV")
    parser.add_argument("input")
    parser.add_argument("--out", default="clean.json")
    args = parser.parse_args()

    with open(args.input, newline= "") as f:
        rows = list(csv.DictReader(f))


    good_list = []
    bad_list = []
    for row in rows:
        try:
            cleaned_row = clean_rows(row)
            good_list.append(cleaned_row)
        except ValueError as e:
            bad_list.append(row)
            logging.error(f"Error cleaning row {row}: {e}")

    logging.info(f"Good rows: {len(good_list)}, bad rows: {len(bad_list)}")

    with open(args.out, "w") as f:
        json.dump(good_list, f, indent=2)