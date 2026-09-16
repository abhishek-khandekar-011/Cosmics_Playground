salaries = [1729 , 6138 , 5129, 1234 , 2560]

sel_sort = salaries[:]

for i in range(len(sel_sort)):

    min_index = i
	
    for j in range(i + 1, len(sel_sort)):
	
        if sel_sort[j] < sel_sort[min_index]:
		
             min_index = j
			 
    sel_sort[i] , sel_sort[min_index] = sel_sort[min_index] , sel_sort[i]
	
print(sel_sort)



bub_sort = salaries[:]

for i in range(len(bub_sort)):

    for j in range(0, len(bub_sort)-i-1):
	
        if bub_sort[j] > bub_sort[j+1]:
		
            bub_sort[j], bub_sort[j+1] = bub_sort[j+1], bub_sort[j]
			
print(bub_sort)