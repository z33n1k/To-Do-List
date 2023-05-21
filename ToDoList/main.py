import todo as m
import os
cwd = os.getcwd()
while True:
    print("---//---")
    global j
    j = int(input("1 to check to do's\n2 to add to do's\n3 to remove to do's\n4 to check finished to do's\n5 to quit\ninput: "))
    try:
        if j == 1:
            m.check_todo()
        elif j == 2:
            m.write_todo()
        elif j == 3:
            m.get_more_info1()
        elif j == 4:
            m.check_finished()
        elif j == 5:
            break
    except:
        continue