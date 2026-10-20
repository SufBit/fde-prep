import string

with open('sample.txt') as f:
    text = f.read()

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

def word_freqeuncies(text:str) -> dict[str,int]:
    words = text.lower().split()
    words = [word.strip(string.punctuation) for word in words]
    counts = {}
    for word in words:
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts

counts = word_freqeuncies(text)
sorted_counts = sort_counts(counts)
print(sorted_counts[:10])
print(f"Unique words: {len(counts)}")