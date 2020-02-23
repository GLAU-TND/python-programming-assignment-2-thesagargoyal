n=int(input())
s=str(bin(n).replace('0b',''))
s=s.split('0')
max=0
for item in s:
	if s.len(item)>max:
		max = s.len(item)
print(max)