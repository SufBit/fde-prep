import argparse
import csv
import json
import logging


logging.basicConfig(filename="cleaning.log", level=logging.INFO, format="%(asctime)s %(message)s")

parser = argparse.ArgumentParser(description="Clean a messy appointments CSV")
parser.add_argument("input")
parser.add_argument("--out", default="clean.json")
args = parser.parse_args()

with open(args.input, newline= "") as f:
    rows = list(csv.DictReader(f))

good_list = []
bad_list = []
allowed_statuses = {"completed", "no-show", "cancelled"}
for row in rows:
    try:
        minutes = int(row["minutes"])
    except ValueError:
        logging.warning(f"Invalid value for minutes in row {row['id']}")
        bad_list.append(row)
        continue
    if not row["provider"]:
        logging.warning(f"Missing provider for row {row['id']}")
        bad_list.append(row)
        continue
    if row["status"] not in allowed_statuses:
        logging.warning(f"Invalid status for row {row['id']}")
        bad_list.append(row)
        continue
    if minutes < 0:
        logging.warning(f"Negative value for minutes in row {row['id']}")
        bad_list.append(row)
        continue
    row["minutes"] = minutes
    good_list.append(row)

logging.info(f"Good rows: {len(good_list)}, bad rows: {len(bad_list)}")

with open(args.out, "w") as f:
    json.dump(good_list, f, indent=2)