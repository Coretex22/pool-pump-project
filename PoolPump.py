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
    print '4: Modify a schedule'
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
            pumptimer = int(raw_input())

            pumpstate = 'on'
            print 'The pump has been turned on for the specified amount of time, and will be turned off automatically'
            time.sleep (pumptimer * 60 * 60)
            pumpstate = 'off'
            print ''
            print 'Timer has expired, and the pump has been turned off'
            print ''

        except ValueError:
            print 'Please enter a valid integer'


#SELECTION 4


    elif firstmenuselection == '4':
        print ''
        print 'Please enter the period of time the pump will run for'
        print ''

        while pumpstate = 'off'
        try:
            pumptimeoninput = int(raw_input())
            pumpstate = 'on'
            #GPIO ON
            time.sleep (pumptimeoninput * 60 * 60)
            pumpstate = 'off'
            #GPIO OFF
            

        except ValueError:
            print ''
            print 'Please enter the number of hours for active, and the hours for sleep'
            print ''
            time.sleep (3)

        print ''
        print 'Please enter the period of time the pump will sleep for between running cycles'
        print ''

        try:
            pumptimesleepinput = int(raw_input())

        except ValueError:
            print ''
            print 'Please enter the time in which the pump will sleep for as a valid integer'
            print ''




    else: print 'Please make a valid selection'
    print ''
