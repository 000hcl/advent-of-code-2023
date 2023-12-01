#input reading

file_name = '1input1.txt'

with open(file_name) as file:
    content = file.read()
    words = content.split('\n')


## PART 1

#sum = 0
#for word in words:
#    ints = '0123456789'
#    ints_order = []
#    for char in word:
#        if char in ints:
#            ints_order.append(char)
    
#    word_digit = int(ints_order[0]+ints_order[-1])
#    sum += word_digit

#print(sum)

## PART 2

sum = 0
for word in words:
    ints = '123456789'
    numbers = {'one':'1',
                'two':'2',
                'three':'3',
                'four':'4',
                'five':'5',
                'six':'6',
                'seven':'7',
                'eight':'8',
                'nine':'9'}

    ints_order = []

    i = 0
    while i < len(word):
        char = word[i]
        if char in ints:
            ints_order.append(char)
            i+=1
            continue
        
        if len(word)-i >= 3:
            if word[i:i+3] in numbers:
                ints_order.append(numbers[word[i:i+3]])
                i+=2
                continue
        
        if len(word)-i >= 4:
            if word[i:i+4] in numbers:
                ints_order.append(numbers[word[i:i+4]])
                i+=3
                continue
        
        if len(word)-i >= 5:
            if word[i:i+5] in numbers:
                ints_order.append(numbers[word[i:i+5]])
                i += 4
                continue

        i+=1
            

    
    word_digit = int(ints_order[0]+ints_order[-1])
    sum += word_digit

print(sum)