# Problem: Chief Historian is missing

# Notes:
# He was visiting locations significant to the North Pole
# Each location should be checked with a star *
# Historian must be in one of the first fifty places
# Get fifty stars on their list
# Collect stars by solving puzzles --> two puzzles each day

# First problem:
# their list of locations is empty
# start is the chief historian's office
# some notes are there
# location numbers -->location ids (split into two groups)
# Problem the list aren't very similar

# test
list1 = [3, 4, 2, 1, 3, 3]
list2 = [4, 3, 5, 3, 9, 3]

list1.sort()
list2.sort()

distance = 0

for i in range(len(list1)):
    gap = abs(list1[i] - list2[i])
    distance = distance + gap

print(f"Test: The value of the overall distance is: {distance}")

# Solution Part 1
with open("input.txt", "r") as f:
    content = f.read()
    listContent = list(map(int, content.split()))
    half1 = listContent[::2]
    half2 = listContent[1::2]

    half1.sort()
    half2.sort()

    distance2 = 0

    for i in range(len(half1)):
        gap = abs(half1[i] - half2[i])
        distance2 = distance2 + gap

    print(f"Solution: The value of the overall distance is: {distance2}")


# Second problem:
# Maybe some numbers are misinterpreted handwriting
# Figure out how often each number from the left list appears in the right list
# Calculate a similarity score by adding up each number after multiplying it by the number it appears on the right

# test
test1 = [3, 4, 2, 1, 3, 3]
test2 = [4, 3, 5, 3, 9, 3]

testSimilarityScore = 0

for i in test1:
    counter = i * test2.count(i)
    testSimilarityScore = testSimilarityScore + counter

print(f"Test: The similarity is core is: {testSimilarityScore}")


# Solution Part 2
with open("input.txt", "r") as f:
    content = f.read()
    listContent = list(map(int, content.split()))
    half1 = listContent[::2]
    half2 = listContent[1::2]

    SimilarityScore = 0

    for i in half1:
        counter = i * half2.count(i)
        SimilarityScore = SimilarityScore + counter

    print(f"Test: The similarity is core is: {SimilarityScore}")
