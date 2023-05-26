let Time2 = 0
let Lap = 0
let Time = 0
radio.setGroup(10)
basic.showLeds(`
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    . . . . .
    `)
basic.pause(100)
basic.clearScreen()
servos.P0.setAngle(0)
loops.everyInterval(1000, function () {
    Time += 1
})
basic.forever(function () {
    if (Lap <= 10) {
        if (BitMaker.read_Din_value(GrovePort.P0) == 0) {
            Lap += 1
            serial.writeLine("Lap" + ("" + Lap) + "finished in")
            serial.writeNumber(Time)
            Time2 = Time + Time2
            serial.writeLine("Lap" + ("" + Lap) + "finished at")
            serial.writeNumber(Time2)
            Time = 0
            basic.showNumber(Lap)
            servos.P0.setAngle(65)
            basic.pause(300)
            servos.P0.setAngle(0)
        }
    }
})
