Time2 = 0
Lap = 0
Time = 0
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

def on_every_interval():
    global Time
    Time += 1
    # Compte le temps en secondes
loops.every_interval(1000, on_every_interval)

def on_forever():
    global Lap, Time2, Time
    if Lap <= 10:
        if BitMaker.read_Din_value(GrovePort.P0) == 0:
            Lap += 1
            serial.write_line("Lap " + ("" + str(Lap)) + " finished in ")
            # Montrer le numero du tour avec le temps du tour
            serial.write_number(Time)
            serial.write_line("")
            Time2 = Time + Time2
            serial.write_line("Lap " + ("" + str(Lap)) + " finished at ")
            # Montrer le numero du tour avec le temps totale
            serial.write_number(Time2)
            serial.write_line("")
            Time = 0
            basic.show_number(Lap)
            servos.P2.set_angle(5)
            # Agitation de drapeau
            basic.pause(300)
            servos.P2.set_angle(0)
basic.forever(on_forever)
