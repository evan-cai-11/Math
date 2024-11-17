# Task 9: Transform nested lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Solution
sums = list(map(lambda x: sum(x), nested))
print(sums)  # [6, 15, 24]

# Task 10: Process strings with multiple conditions
words = ['python', 'java', 'javascript', 'csharp']
# Solution
processed = list(map(
    lambda x: f"{x.upper()}: {len(x)}" if len(x) > 5 
    else x.upper(),
    words
))
print(processed)