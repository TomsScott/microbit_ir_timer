#Startup et preparations du program
Time2 = 0
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

def on_forever():
    global Lap, Time2
    if Lap <= 10:
        if BitMaker.read_Din_value(GrovePort.P0) == 0:
            Lap += 1
            serial.write_line("")
            serial.write_line("Lap " + ("" + str(Lap)) + " finished at ")
            # Montrer le numero du tour avec le temps totale en secondes
            serial.write_number(control.millis() / 1000)
            serial.write_line(" secondes")
            serial.write_line("Lap " + ("" + str(Lap)) + " finished in ")
            # Montrer le numero du tour avec le temps du tour en secondes
            serial.write_number((control.millis() - Time2) / 1000)
            serial.write_line(" secondes")
            Time2 = control.millis()
            #Variable "checkpoint" pour trouver le temps du prochain tour
            basic.show_number(Lap)
            servos.P2.set_angle(5)
            # Agitation de drapeau
            basic.pause(300)
            servos.P2.set_angle(0)
basic.forever(on_forever)
