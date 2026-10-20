import csv

with open("appointments.csv",newline="") as f:
    rows = list(csv.DictReader(f))

print("Totoal Number of Appointments:", len(rows))

def sort_counts(counts):
    pairs = list(counts.items())
    n = len(pairs)
    for i in range(n):
        for j in range(n-i-1):
            if pairs[j][1] < pairs[j+1][1]:
                pairs[j],pairs[j+1] = pairs[j+1],pairs[j]
        

    lines = []
    for key,count in pairs:
        lines.append(f"{key}: {count}")
    return lines

def count_by(rows: list[dict],field: str) -> dict[str, int]:
    counts = {}
    for row in rows:
        key = row[field]
        counts[key] = counts.get(key,0) + 1
    return counts
    

provider_counts = {}
provider_counts = count_by(rows,"provider")
print("Provider Counts:", provider_counts)

sorted_provider_counts = sort_counts(provider_counts)
print (sorted_provider_counts)

status_counts = {}
status_counts = count_by(rows,"status")
print("Status Counts:", status_counts)

sorted_status_counts = sort_counts(status_counts)
print (sorted_status_counts)

total_duration = 0
for row in rows:
    if row["status"] == "completed":
        total_duration += int(row["minutes"])

print(f"Total Duration of Completed Appointments: {total_duration}")
