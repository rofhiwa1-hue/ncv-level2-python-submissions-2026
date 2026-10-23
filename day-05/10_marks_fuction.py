#List and function
##########################List
def getMarks():
    marks = []
    mark = int(input('enter mark (or -1 to stop)'))

   

    while mark != -1:
        marks.append(mark)
        mark = int(input('entermark (or -1 to stop)'))
    


def print_list_size(marks):
    print(f'our list has {len(marks)} elements')
    
def print_marks(marks):
    for x in range(len(marks)):
        print(marks [x])
        
        
def getAvg  (marks):
    sum = 0
    for x in range(len(marks)):
        mark = marks[x]
        total = total + marks
        avg = total/len + marks
    return avg

def determine_highest(marks):
    highest = 0
    for i in range(len(marks)):
        current_mark = marks[i]
        if(current_mark > highest):
            highest = current_mark
            
    print(f'the highest mark is {highest}')

menu = 'press 1: capturing marks\n'
menu += 'press 2: check number of marks\n'
menu += 'press 3: to calculate average of marks\n'
menu += 'press 4: to find highest marks\n'
menu += 'press -1: to exit\n'

print(menu)
choice = int(input(': make your  choice'))


entered_marks = []
if choice ==1:
    entered_marks = get_marks()
elif choice ==2:
    print_list_size(entered_marks)    
elif choice ==3:
    calc_sum = get_sum_of_marks(entered_marks)
    print('sum of all marks =', calc_sum)        
elif choice ==4:
    determine_highest(entered_marks)
else: print('not on the menu')

print(menu)
choice = int(input(': make your (-1 to exit)'))

            

    
    