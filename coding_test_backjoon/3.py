from itertools import combinations_with_replacement
roma = [1,5,10,50]
# roma = { 'I': 1, 'V' : 5, 'X': 10 , 'L' : 50} 

n = int(input())
a = list(combinations_with_replacement(roma,n))
answer = [] 

for i in a:
    if sum(i) not in answer:
        answer.append(sum(i))
    
print(len(answer))