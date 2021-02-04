def Finn_køyrelengd(rotasjonar: number):
    global køyrelengd
    køyrelengd = 17.3 * rotasjonar + 0.1 * (rotasjonar)* 3.14

def on_button_pressed_a():
    global rotasjonar
    rotasjonar += 1
    Finn_køyrelengd(rotasjonar)
    basic.show_number(køyrelengd)
input.on_button_pressed(Button.A, on_button_pressed_a)

rotasjonar = 0
køyrelengd = 0