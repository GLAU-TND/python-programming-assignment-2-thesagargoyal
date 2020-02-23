list = list(map(str,input().split()))
list2 = [list[0]]
for i in list :
	for j in list2 :
		if i[-1]==j[0]:
			if j not in k :
				k.append(j)
				break
print(list2)