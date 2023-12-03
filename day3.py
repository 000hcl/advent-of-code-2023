# input reading

file_name = 'input3.txt'

with open(file_name) as file:
    content = file.read()
    lines = content.split('\n')


## PART 1
"""
schema_sum = 0
nr_run = ''
in_schema = False
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] not in '0123456789':
            if in_schema is True:
                schema_sum += int(nr_run)
            nr_run = ''
            in_schema = False
        if lines[i][j] in '0123456789':
            nr_run+=lines[i][j]
            i_directions = set([0])
            j_directions = set([0])
            if i>0:
                i_directions.add(-1)
            if i<len(lines)-1:
                i_directions.add(1)
            if j>0:
                j_directions.add(-1)
            if j<len(lines[0])-1:
                j_directions.add(1)
            for ix in i_directions:
                for jx in j_directions:
                    if lines[i+ix][j+jx] not in '.0123456789':
                        in_schema = True

if in_schema is True:
    schema_sum += int(nr_run)

print(schema_sum)
"""
## PART 2
gear_coords = {}
adj_gear = []
nr_run = ''
in_schema = False
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] not in '0123456789':
            for a in adj_gear:
                if gear_coords.get(a):
                    gear_coords[a].append(int(nr_run))
                else:
                    gear_coords[a] = [int(nr_run)]
            nr_run = ''
            adj_gear = []
        elif lines[i][j] in '0123456789':
            nr_run+=lines[i][j]
            i_directions = set([0])
            j_directions = set([0])
            if i>0:
                i_directions.add(-1)
            if i<len(lines)-1:
                i_directions.add(1)
            if j>0:
                j_directions.add(-1)
            if j<len(lines[0])-1:
                j_directions.add(1)
            for ix in i_directions:
                for jx in j_directions:
                    if lines[i+ix][j+jx] == '*':
                        if (i+ix,j+jx) not in adj_gear:
                            adj_gear.append((i+ix,j+jx))


g_sum = 0

for key in gear_coords:
    nrs = gear_coords[key]
    if len(nrs)==2:
        g_sum += nrs[0]*nrs[1]

print(g_sum)