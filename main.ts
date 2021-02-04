let køyrelengd = 0
let rotasjonar = 0
function Finn_køyrelengd (rotasjonar: number) {
    køyrelengd = 17.3 * rotasjonar + 0.1 * (rotasjonar * rotasjonar) * 3.14
}
input.onButtonPressed(Button.A, function () {
    rotasjonar += 1
    Finn_køyrelengd(rotasjonar)
    basic.showNumber(køyrelengd)
})
