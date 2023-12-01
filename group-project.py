import csv

with open('/Users/Zapao/Desktop/USA_cars_datasets.csv', 'r', encoding = 'UTF -8') as file:
    file.readline()
    data = []
    for i in file:
        data.append(i.strip().split(','))
    #print(data)
    #what is the longest mileage that particular brand has
    def longest_mileage(brand):
        data_brand = []
        for i in data:
            if i[2] == brand:
                data_brand.append(i)
        mileage = []
        for i in data_brand:
            mileage.append(i[6])
        n = len(mileage)
        max = 0
        for i in range(1,n):
            if mileage[i] > mileage[max]:
                max = i
        return f"The longest mileage of {brand} is {mileage[max]}"
    #4.count the number of particular colours
    def count_by_colors(color):
        color_list = []
        for i in data:
            color_list.append(i[7])
        n = len(color_list)
        count = 0
        for i in range(0,n):
            if color_list[i] == color:
                count+=1
        return f'There are {count} {color} cars'
        
    print(longest_mileage('ford'))
    print(count_by_colors('black'))
