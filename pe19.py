days = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
li = [(2,31),(3,28),(4,31),(5,30),(6,31),(7,30),(8,31),(9,31),(10,30),(11,31),(12,30),(1,31)]
cnt = 0
old_index_day = 0
for year in range(1900,2001):
    for num_month,num_day in li:
        # năm nhuận
        if (year % 100 == 0 and year % 400 == 0) or (year %100 != 0 and year %4==0):
            if year == 2000 and num_month == 1: # đây là 1/1/2001 nên không tính
                new_index_day = (old_index_day + num_day+1) % 7
                # đây là ngày 1 của tháng num_month
                day = days[new_index_day]
                old_index_day = new_index_day
            if num_month == 3:
                new_index_day = (old_index_day + num_day+1) % 7
                day = days[new_index_day]
                old_index_day = new_index_day
                if day == 'Sun':
                    cnt+=1
            else:
                new_index_day = (old_index_day + num_day) % 7
                day = days[new_index_day]
                old_index_day = new_index_day
                if day == 'Sun':
                    cnt+=1
        # năm không nhuận
        else:
            new_index_day = (old_index_day + num_day) % 7
            day = days[new_index_day]
            old_index_day = new_index_day
            # nếu year = 1900 và num_month == 1 tức là 1/1/1901
            if day == 'Sun' and ((year == 1900 and num_month == 1) or(year > 1900)):
                    cnt+=1
print(cnt)



        
