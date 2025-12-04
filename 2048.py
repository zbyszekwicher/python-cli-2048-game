from time import sleep
from random import randrange as r
import keyboard

sq_values = [
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0  ]
logo = "╔═══╦═══╦╗─╔╦═══╗\n║╔═╗║╔═╗║║─║║╔═╗║\n╚╝╔╝║║║║║╚═╝║╚═╝║\n╔═╝╔╣║║║╠══╗║╔═╗║\n║║╚═╣╚═╝║──║║╚═╝║\n╚═══╩═══╝──╚╩═══╝"
new_item = [2,2,2,2,4]
score = 0
playing = True

def PrintBoard(sq_values):
    # Finding the biggest value
    l_b = []
    for i in sq_values:
        l_b.append(i)
    l_b.sort()
    b = str(l_b[-1])

    # Make list of strings to print
    p = []
    for i in sq_values:
        if i == 0:
            p.append(' ')
        else:
            p.append(str(i))

        while len(p[-1]) < len(b):
            p[-1] += ' '

    print('| '+p[0]+' | '+p[1]+' | '+p[2]+' | '+p[3]+' |')
    print('| '+p[4]+' | '+p[5]+' | '+p[6]+' | '+p[7]+' |')
    print('| '+p[8]+' | '+p[9]+' | '+p[10]+' | '+p[11]+' |')
    print('| '+p[12]+' | '+p[13]+' | '+p[14]+' | '+p[15]+' |')


def NewOutput():
    # Print new space
    print('\n'*20)
    print(logo)

    # Print score
    print('SCORE:',score,'\n')

    # Print board
    PrintBoard(sq_values)
    print('\n'*2)
    print('controls: W-A-S-D')
    print('\n'*2)

def Move(a,b,c,d,  e,f,g,h,  i,j,k,l,  m,n,o,p):
    global score
    #1sq
    if sq_values[a] == 0:
        sq_values[a] = sq_values[b]
        sq_values[b] = 0
    elif sq_values[a] == sq_values[b]:
        sq_values[a] *= 2
        score += sq_values[a]
        sq_values[b] = 0
    #2sq
    if sq_values[b] == 0 and sq_values[a] == 0:
        sq_values[a] = sq_values[c]
        sq_values[c] = 0
    elif sq_values[b] == 0 and sq_values[a] == sq_values[c]:
        sq_values[a] *= 2
        score += sq_values[a]
        sq_values[c] = 0

    elif sq_values[b] == 0:
        sq_values[b] = sq_values[c]
        sq_values[c] = 0
    elif sq_values[b] == sq_values[c]:
        sq_values[b] *= 2
        score += sq_values[b]
        sq_values[c] = 0
    #3sq
    if sq_values[c] == 0 and sq_values[b] == 0 and sq_values[a] == 0:
        sq_values[a] = sq_values[d]
        sq_values[d] = 0
    elif sq_values[c] == 0 and sq_values[b] == 0 and sq_values[a] == sq_values[d]:
        sq_values[a] *= 2
        score += sq_values[a]
        sq_values[d] = 0

    elif sq_values[c] == 0 and sq_values[b] == 0:
        sq_values[b] = sq_values[d]
        sq_values[d] = 0
    elif sq_values[c] == 0 and sq_values[b] == sq_values[d]:
        sq_values[b] *= 2
        score += sq_values[b]
        sq_values[d] = 0

    elif sq_values[c] == 0:
        sq_values[c] = sq_values[d]
        sq_values[d] = 0
    elif sq_values[c] == sq_values[d]:
        sq_values[c] *= 2
        score += sq_values[c]
        sq_values[d] = 0
    #5sq
    if sq_values[e] == 0:
        sq_values[e] = sq_values[f]
        sq_values[f] = 0
    elif sq_values[e] == sq_values[f]:
        sq_values[e] *= 2
        score += sq_values[e]
        sq_values[f] = 0
    #6sq
    if sq_values[f] == 0 and sq_values[e] == 0:
        sq_values[e] = sq_values[g]
        sq_values[g] = 0
    elif sq_values[f] == 0 and sq_values[e] == sq_values[g]:
        sq_values[e] *= 2
        score += sq_values[e]
        sq_values[g] = 0

    elif sq_values[f] == 0:
        sq_values[f] = sq_values[g]
        sq_values[g] = 0
    elif sq_values[f] == sq_values[g]:
        sq_values[f] *= 2
        score += sq_values[f]
        sq_values[g] = 0
    #7sq
    if sq_values[g] == 0 and sq_values[f] == 0 and sq_values[e] == 0:
        sq_values[e] = sq_values[h]
        sq_values[h] = 0
    elif sq_values[g] == 0 and sq_values[f] == 0 and sq_values[e] == sq_values[h]:
        sq_values[e] *= 2
        score += sq_values[e]
        sq_values[h] = 0

    elif sq_values[g] == 0 and sq_values[f] == 0:
        sq_values[f] = sq_values[h]
        sq_values[h] = 0
    elif sq_values[g] == 0 and sq_values[f] == sq_values[h]:
        sq_values[f] *= 2
        score += sq_values[f]
        sq_values[h] = 0

    elif sq_values[g] == 0:
        sq_values[g] = sq_values[h]
        sq_values[h] = 0
    elif sq_values[g] == sq_values[h]:
        sq_values[g] *= 2
        score += sq_values[g]
        sq_values[h] = 0
    #9sq
    if sq_values[i] == 0:
        sq_values[i] = sq_values[j]
        sq_values[j] = 0
    elif sq_values[i] == sq_values[j]:
        sq_values[i] *= 2
        score += sq_values[i]
        sq_values[j] = 0
    #10sq
    if sq_values[j] == 0 and sq_values[i] == 0:
        sq_values[i] = sq_values[k]
        sq_values[k] = 0
    elif sq_values[j] == 0 and sq_values[i] == sq_values[k]:
        sq_values[i] *= 2
        score += sq_values[i]
        sq_values[k] = 0

    elif sq_values[j] == 0:
        sq_values[j] = sq_values[k]
        sq_values[k] = 0
    elif sq_values[j] == sq_values[k]:
        sq_values[j] *= 2
        score += sq_values[j]
        sq_values[k] = 0
    #11sq
    if sq_values[k] == 0 and sq_values[j] == 0 and sq_values[i] == 0:
        sq_values[i] = sq_values[l]
        sq_values[l] = 0
    elif sq_values[k] == 0 and sq_values[j] == 0 and sq_values[i] == sq_values[l]:
        sq_values[i] *= 2
        score += sq_values[i]
        sq_values[l] = 0

    elif sq_values[k] == 0 and sq_values[j] == 0:
        sq_values[j] = sq_values[l]
        sq_values[l] = 0
    elif sq_values[k] == 0 and sq_values[j] == sq_values[l]:
        sq_values[j] *= 2
        score += sq_values[j]
        sq_values[l] = 0

    elif sq_values[k] == 0:
        sq_values[k] = sq_values[l]
        sq_values[l] = 0
    elif sq_values[k] == sq_values[l]:
        sq_values[k] *= 2
        score += sq_values[k]
        sq_values[l] = 0
    #13sq
    if sq_values[m] == 0:
        sq_values[m] = sq_values[n]
        sq_values[n] = 0
    elif sq_values[m] == sq_values[n]:
        sq_values[m] *= 2
        score += sq_values[m]
        sq_values[n] = 0
    #14sq
    if sq_values[n] == 0 and sq_values[m] == 0:
        sq_values[m] = sq_values[o]
        sq_values[o] = 0
    elif sq_values[n] == 0 and sq_values[m] == sq_values[o]:
        sq_values[m] *= 2
        score += sq_values[m]
        sq_values[o] = 0

    elif sq_values[n] == 0:
        sq_values[n] = sq_values[o]
        sq_values[o] = 0
    elif sq_values[n] == sq_values[o]:
        sq_values[n] *= 2
        score += sq_values[n]
        sq_values[o] = 0
    #15sq
    if sq_values[o] == 0 and sq_values[n] == 0 and sq_values[m] == 0:
        sq_values[m] = sq_values[p]
        sq_values[p] = 0
    elif sq_values[o] == 0 and sq_values[n] == 0 and sq_values[m] == sq_values[p]:
        sq_values[m] *= 2
        score += sq_values[m]
        sq_values[p] = 0

    elif sq_values[o] == 0 and sq_values[n] == 0:
        sq_values[n] = sq_values[p]
        sq_values[p] = 0
    elif sq_values[o] == 0 and sq_values[n] == sq_values[p]:
        sq_values[n] *= 2
        score += sq_values[n]
        sq_values[p] = 0

    elif sq_values[o] == 0:
        sq_values[o] = sq_values[p]
        sq_values[p] = 0
    elif sq_values[o] == sq_values[p]:
        sq_values[o] *= 2
        score += sq_values[o]
        sq_values[p] = 0

while playing:
    # Add new random item to sq_values
    n = new_item[r(len(new_item))]
    x = 0
    while x < 16:
        x += 1
        s = r(len(sq_values))
        if sq_values[s] == 0:
            sq_values[s] = n
            n = 0
            break
    if n != 0:
        for i in sq_values:
            if i == 0:
                sq_values[sq_values.index(i)] = n
                n = 0
                break

    NewOutput()

    inp = 0
    while inp == 0:
        if keyboard.is_pressed('a'):
            inp = 'left'
            while keyboard.is_pressed('a'):
                sleep(0.1)
        elif keyboard.is_pressed('d'):
            inp = 'right'
            while keyboard.is_pressed('d'):
                sleep(0.1)
        elif keyboard.is_pressed('w'):
            inp = 'up'
            while keyboard.is_pressed('w'):
                sleep(0.1)
        elif keyboard.is_pressed('s'):
            inp = 'down'
            while keyboard.is_pressed('s'):
                sleep(0.1)
        sleep(0.02)

    if inp == 'left':
        Move(0,1,2,3, 4,5,6,7, 8,9,10,11, 12,13,14,15)

    elif inp == 'right':
        Move(3,2,1,0, 7,6,5,4, 11,10,9,8, 15,14,13,12)

    elif inp == 'up':
        Move(0,4,8,12, 1,5,9,13, 2,6,10,14, 3,7,11,15)

    elif inp == 'down':
        Move(12,8,4,0, 13,9,5,1, 14,10,6,2, 15,11,7,3)
