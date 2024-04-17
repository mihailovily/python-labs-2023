def from_list_to_string(spisok):
    kasha = []
    for i in spisok:
        for j in range(len(i)):
            kasha.append(i[j])
    return ' '.join(kasha)
    
print(from_list_to_string(['best', 'in', 'the', 'world']))