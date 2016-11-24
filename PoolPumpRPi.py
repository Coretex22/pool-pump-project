#This program is written to remotely control a pool pump using a RaspberryPi's GPIO Pins.

#This is because I don't know how to list shit properly yet:
import time
import RPi.GPIO as GPIO
#This configures the GPIO pin numbering scheme
GPIO.setmode(GPIO.BOARD)
#This configures GPIO Pin 17 (Physically pin 11) as an output pin
GPIO.setup(11, GPIO.OUT)
#This sets GPIO Pin 17 to a "LOW" or "OFF" state.
GPIO.output(11, GPIO.LOW)

pumpstate = 'off'

while pumpstate == 'off' or 'on':

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
                GPIO.output(11, GPIO.HIGH)
                print ''
                print 'The pump is now on'
                print ''

        elif pumpfalseboolean == True:
                pumpstate = 'off'
                GPIO.output(11, GPIO.LOW)
                print ''
                print 'The pump is now off'
                print ''

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
            GPIO.output(11, GPIO.HIGH)
            print 'The pump has been turned on for the specified amount of time, and will be turned off automatically'
            time.sleep (pumptimer * 60 * 60)
            pumpstate = 'off'
            GPIO.output(11, GPIO.LOW)
            print ''
            print 'Timer has expired, and the pump has been turned off'
            print ''

        except NameError:
            print 'Please enter a valid integer'

    else: print 'Please make a valid selection'
    print ''
