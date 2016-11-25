#This program is written to remotely control a pool pump using a RaspberryPi's GPIO Pins.

import time

pumpstate = 'off'

while pumpstate == 'off' or 'on':
#This is because I don't know how to list shit properly yet:
    print ''
    print 'Please choose an option:'
    print ''
    print '1: Enter a new pump state'
    print '2: View current pump state'
    print '3: Set the pump on a timer'
    print ''

    firstmenuselection = raw_input()


#SELECTION 1


    if firstmenuselection == '1':
        print ''
        print 'Please enter a new pump state (on or off): '
        print ''
        newpumpstate = raw_input()
        print ''

        pumptrueboolean = newpumpstate in 'on, On, ON'
        pumpfalseboolean = newpumpstate in 'off, Off, OFF'

        if pumptrueboolean == True:
                pumpstate = 'on'

        elif pumpfalseboolean == False:
                pumpstate = 'off'

        else: print 'Please make a valid selection'
        time.sleep (1)


#SELECTION 2


    elif firstmenuselection == '2':
        print ''
        print 'Pump is currently', pumpstate
        print ''


#SELECTION 3


    elif firstmenuselection == '3':
        print ''
        print 'Please enter the timer interval in hours'
        print ''

        try:
            pumptimer = int(input())

            pumpstate = 'on'
            print 'The pump has been turned on for the specified amount of time, and will be turned off automatically'
            time.sleep (pumptimer * 60 * 60)
            pumpstate = 'off'
            print ''
            print 'Timer has expired, and the pump has been turned off'
            print ''

        except NameError:
            print 'Please enter a valid integer'

    else: print 'Please make a valid selection'
    print ''
