from itertools import permutations
list = list(map(str,input().split()))
a=permutation(list)
list2=[]
for i in list(a):
	s=''
	for j in i:
		s=s+j
	list2.append(int(s))
print(max(list2))