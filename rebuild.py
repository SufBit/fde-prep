import csv

def count_by(rows:list[dict], field:str) -> dict[str,int]:
        counts = {}
        for row in rows:
            key = row[field]
            counts[key] = counts.get(key,0) + 1
        return counts


if __name__ == "__main__":

    with open("appointments.csv",newline="") as f:
        rows = list(csv.DictReader(f))

    counts = count_by(rows,"status")
    print(sorted(counts.items(), key=lambda x:x[1], reverse=True))