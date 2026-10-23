marks = []
i = 0

mark = int(input('enter mark (or -1 to stop)'))

while mark != -1:
    marks.append(mark)
    mark = int(input('entermark (or -1 to stop)'))
    
    print(f'our list has {len(marks)} elements')
    
    for x in range(len(marks)):
        print(marks [x])
sum = 0
for x in range(len(marks)):
    mark = marks[x]
    total = total + marks
    avg = total/len + marks
    print(f'the average of all marks = {avg}')
    