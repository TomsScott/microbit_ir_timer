"""

Sets the necessary variables in place

"""
Time2 = 0
Time = 0
Lap = 0
basic.show_leds("""
    . . . . #
        . . . # .
        # . # . .
        . # . . .
        . . . . .
""")
basic.pause(100)
basic.clear_screen()
servos.P2.set_angle(0)
"""

Startup logo to demonstrate a successfull startup.

"""

def on_forever():
    global Lap, Time2, Time
    if Lap <= 10:
        if BitMaker.read_Din_value(GrovePort.P0) == 0:
            Lap += 1
            serial.write_line("Lap " + ("" + str(Lap)) + " finished in ")
            # Write the lap number and the duration it took to finish said lap.
            serial.write_number(Time)
            serial.write_line("secondes")
            Time2 = Time + Time2
            serial.write_line("Lap " + ("" + str(Lap)) + " finished at ")
            # Write the lap number and the total duration that has passed.
            serial.write_number(Time2)
            serial.write_line("secondes")
            Time = 0
            basic.show_number(Lap)
            servos.P2.set_angle(5)
            # Agitation de drapeau
            basic.pause(300)
            servos.P2.set_angle(0)
basic.forever(on_forever)
