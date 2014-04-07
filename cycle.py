txt = []

def add(text):
    txt.append(text)
    txt.append("<hr>")


def plrc(l,r,c):
    add("Left {0} Right {1} Cycles {2}".format(l,r,c))

def cycle_factor(left,right):
    cycles = 0
    while True:
        plrc(left, right, cycles)
        if ((right >= left) and left >= 25 and right >= 50):
            cycles += 1
            left -= 25
            right -= 50
        elif ((left >= right) and left >= 50 and right >= 25):
            cycles += 1
            right -= 25
            left -= 50
        else:
            add("All cycles done")
            break
    return txt
