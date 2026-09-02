votes = ["A", "B", "A", "C", "B", "A", "B"]
frequency = {}
for vote in votes:
    if vote in frequency:
        frequency[vote] += 1
    else:
        frequency[vote] = 1
max_frequency = 0
most_common_vote = ""
for vote, count in frequency.items():
    if count > max_frequency:
        max_frequency = count
        most_common_vote = vote
print(f"The most common vote is: {most_common_vote} with a frequency of {max_frequency}.")