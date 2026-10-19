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
    

counts = {}
for row in rows:
    key = row["provider"] 
    counts[key] = counts.get(key,0) + 1

sorted_counts = sort_counts(counts)
print (sorted_counts)

status_counts = {}
for row in rows:
    key = row["status"]
    status_counts[key] = status_counts.get(key,0) + 1

sorted_status_counts = sort_counts(status_counts)
print (sorted_status_counts)

total_duration = 0
for row in rows:
    if row["status"] == "completed":
        total_duration += int(row["minutes"])

print(f"Total Duration of Completed Appointments: {total_duration}")



     