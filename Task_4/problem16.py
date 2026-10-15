# Nested Lists

if __name__ == '__main__':
    records=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.append(score)
    records=sorted(records)
    scores=sorted(set(scores))
    lowest=scores[1]
    for i in records:
        if lowest in i:
            print(i[0])
        
    