if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
# Step 1: Get all unique scores
scores = sorted(set([s[1] for s in students]))
    
# Step 2: Find second lowest score
second_lowest = scores[1]
    
# Step 3: Get all names with that score
result = [s[0] for s in students if s[1] == second_lowest]
    
# Step 4: Sort alphabetically
result.sort()
    
# Step 5: Print each name
for name in result:
    print(name)
