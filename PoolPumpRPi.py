#This program is written to remotely control a pool pump using a RaspberryPi's GPIO Pins.

import time
import datetime

import RPi.GPIO as GPIO
#This configures the GPIO pin numbering scheme
GPIO.setmode(GPIO.BOARD)
#This configures GPIO Pin 17 (Physically pin 11) as an output pin
GPIO.setup(11, GPIO.OUT)
#This sets GPIO Pin 17 to a "LOW" or "OFF" state.
GPIO.output(11, GPIO.LOW)

pumpstate = 'off'

while pumpstate in ['on', 'off']:
#This is because I don't know how to list shit properly yet:
    print ''
    print 'Please choose an option:'
    print ''
    print '1: Enter a new pump state'
    print '2: View current pump state'
    print '3: Set the pump on a timer'
    print '4: Modify a schedule'
    print '5: Exit the system'
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
                GPIO.output(11, GPIO.HIGH)

        elif pumpfalseboolean == True:
                pumpstate = 'off'
                GPIO.output(11, GPIO.LOW)

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
            GPIO.output(11, GPIO.HIGH)
            print 'The pump has been turned on for the specified amount of time, and will be turned off automatically'
            time.sleep (pumptimer * 60 * 60)
            pumpstate = 'off'
            GPIO.output(11, GPIO.LOW)
            print ''
            print 'Timer has expired, and the pump has been turned off'
            print ''

        except ValueError:
            print 'Please enter a valid integer'


#SELECTION 4


    elif firstmenuselection == '4':
        try:
            while pumpstate == 'off':

                print ''
                print 'Please enter the period of time the pump will run for'
                print ''

                try:
                    pumptimeoninput = int(raw_input()) * 60 * 60

                except ValueError:
                    print ''
                    print 'Please enter the number of hours the pump will be active for'
                    print ''
                    time.sleep (1)

                print ''
                print 'Please enter the period of time the pump will sleep for between running cycles'
                print ''

                try:
                    pumptimesleepinput = int(raw_input()) * 60 * 60

                except ValueError:
                    print ''
                    print 'Please enter the time in which the pump will sleep for as a valid integer'
                    print ''

                while pumpstate == 'on' or 'off':

                    print "Pump has been turned on at", datetime.datetime.now()
                    pumpstate = 'on'
                    GPIO.output(11, GPIO.HIGH)
                    time.sleep (pumptimeoninput)
                    print "Pump has been turned off at", datetime.datetime.now()
                    pumpstate = 'off'
                    GPIO.output(11, GPIO.LOW)
                    time.sleep(pumptimesleepinput)
                    
        except KeyboardInterrupt:
            pass

# SELECTION 5


    elif firstmenuselection == '5':
        quit()


    else: print 'Please make a valid selection'
    print ''
