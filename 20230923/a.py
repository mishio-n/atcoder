x = list(input())
ans = "Yes"

for i,n in enumerate(x):
    if i == 0:
        continue
    
    if x[i-1] <= n:
        ans = "No"
        break

print(ans)

