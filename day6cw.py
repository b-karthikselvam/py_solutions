total = 0
sum = 0
attendance = [18,20,19,15,21]
for x in attendance:
    if x >= 20:
        print(f'{x} full' )
        sum += 1
    else:
         print(f'{x} not full' )
        
    total += x
print(f'{sum} days the class was full ')
print(f'Total attendance for all 5 days is: {total}')

