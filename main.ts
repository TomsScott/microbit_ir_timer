let Time2 = 0
let Lap = 0
basic.showLeds(`
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    . . . . .
    `)
basic.pause(100)
basic.clearScreen()
servos.P2.setAngle(0)
basic.forever(function () {
    if (Lap <= 10) {
        if (BitMaker.read_Din_value(GrovePort.P0) == 0) {
            Lap += 1
            serial.writeLine("")
            serial.writeLine("Lap " + ("" + Lap) + " finished at ")
            // Montrer le numero du tour avec le temps totale
            serial.writeNumber(control.millis() / 1000)
            serial.writeLine(" secondes")
            serial.writeLine("Lap " + ("" + Lap) + " finished in ")
            // Montrer le numero du tour avec le temps du tour
            serial.writeNumber((control.millis() - Time2) / 1000)
            serial.writeLine(" secondes")
            Time2 = control.millis()
            basic.showNumber(Lap)
            servos.P2.setAngle(5)
            // Agitation de drapeau
            basic.pause(300)
            servos.P2.setAngle(0)
        }
    }
})
