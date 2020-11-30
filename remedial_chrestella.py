# Nomor 1
def find_short(count_words): 
    min_words = len(count_words[0])
    for i in count_words: 
        if(len(i) < min_words): 
            min_words = len(i)  
    print(f'The shortest word has {min_words} char(s)') 
  
kalimat1 = 'Many people get up early in the morning'
kalimat2 = 'Every office would getting newest monitor'
kalimat3 = 'Create new file after this morning'
count_words = (kalimat1.split())
find_short(count_words)

# Nomor 2
persistence = input('Please input numbers: ')
if "-" in persistence or persistence.isdigit() < 0:
    print ('Please input positive number only')
elif persistence.isdigit() == True and (len(persistence) == 1):
    print (f'0. "{persistence}" is already single digit')
elif persistence.isdigit() == True and (len(persistence) != 1):
    count = 1
    converted_angka = str(persistence)
    def split(converted_angka): 
        return [char for char in converted_angka]
    test_list = [int(i) for i in converted_angka]
    def multiplyList(test_list):
        result = 1
        for x in test_list:
            result = result * x 
        return result
    converted_list = str(multiplyList(test_list))

    if len(converted_list) > 1:
        for i in converted_list:
            def split2(converted_list): 
                return [char for char in converted_list]
            test_list2 = [int(i) for i in converted_list]
            def multiplyList2(test_list2):
                result = 1
                for x in test_list2:
                    result = result * x 
                return result     
            converted_list2 = str(multiplyList2(test_list2))
            count +=1
    print(f'It takes {count} times multiplication until we get a single digit')