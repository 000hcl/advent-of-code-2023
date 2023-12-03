# input reading

file_name = 'input2.txt'

with open(file_name) as file:
    content = file.read()
    games = content.split('\n')


## PART 1
"""
ok_sum = 0

for game in games:
    game_nr = int(game.split(':')[0].split(' ')[1])
    sets = game.split(':')[1].split(';')
    max_red = 0
    max_blue = 0
    max_green = 0
    for set in sets:
        balls = set.split(',')
        for ball in balls:
            ball = ball.strip()
            amount, colour = ball.split(' ')
            if colour == 'red':
                max_red = max(max_red, int(amount))
            elif colour == 'blue':
                max_blue = max(max_blue, int(amount))
            elif colour == 'green':
                max_green = max(max_green, int(amount))
    if max_blue<=14 and max_green<=13 and max_red<=12:
        ok_sum += game_nr

print(ok_sum)
"""
## PART 2

power_sum = 0

for game in games:
    game_nr = int(game.split(':')[0].split(' ')[1])
    sets = game.split(':')[1].split(';')
    max_red = 0
    max_blue = 0
    max_green = 0
    for set in sets:
        balls = set.split(',')
        for ball in balls:
            ball = ball.strip()
            amount, colour = ball.split(' ')
            if colour == 'red':
                max_red = max(max_red, int(amount))
            elif colour == 'blue':
                max_blue = max(max_blue, int(amount))
            elif colour == 'green':
                max_green = max(max_green, int(amount))
    
    power_sum += max_blue*max_green*max_red

print(power_sum)