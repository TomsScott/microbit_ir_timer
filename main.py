Time2 = 0
Lap = 0
Time = 0
radio.set_group(10)
basic.show_leds("""
    . . . . #
        . . . # .
        # . # . .
        . # . . .
        . . . . .
""")
basic.pause(100)
basic.clear_screen()
servos.P0.set_angle(0)

def on_every_interval():
    global Time
    Time += 1
loops.every_interval(1000, on_every_interval)

def on_forever():
    global Lap, Time2, Time
    if Lap <= 10:
        if BitMaker.read_Din_value(GrovePort.P0) == 0:
            Lap += 1
            serial.write_line("Lap"+str(Lap)+ "finished in")
            serial.write_number(Time)
            Time2 = Time + Time2
            serial.write_line("Lap" + str(Lap) + "finished at")
            serial.write_number(Time2)
            Time = 0
            basic.show_number(Lap)
            servos.P0.set_angle(65)
            basic.pause(300)
            servos.P0.set_angle(0)
basic.forever(on_forever)
