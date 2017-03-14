diagnostics.watch(wiimote[0].acceleration.x)
diagnostics.watch(wiimote[0].acceleration.y)
diagnostics.watch(wiimote[0].acceleration.z)

def wiimoteAccelerationUpdate():
 	vJoy[0].x = wiimote[0].acceleration.y / 9.81 * vJoy[0].axisMax * -1
 	vJoy[0].y = wiimote[0].acceleration.x / 9.81 * vJoy[0].axisMax * -1
 	
def wiimoteButtonUpdate():
	b1 = wiimote[0].buttons.button_down(WiimoteButtons.One)
	b2 = wiimote[0].buttons.button_down(WiimoteButtons.Two)
	vJoy[0].setButton(0, b1 and not b2)
	vJoy[0].setButton(1, b2 and not b1)
	vJoy[0].setButton(6, b1 and b2)	# Handbrake
	vJoy[0].setButton(2, wiimote[0].buttons.button_down(WiimoteButtons.A))
	vJoy[0].setButton(3, wiimote[0].buttons.button_down(WiimoteButtons.B))
	vJoy[0].setButton(4, wiimote[0].buttons.button_down(WiimoteButtons.Plus))
	vJoy[0].setButton(5, wiimote[0].buttons.button_down(WiimoteButtons.Minus))
	vJoy[0].setButton(7, wiimote[0].buttons.button_down(WiimoteButtons.Home))
	
	# D-Pad
	cPovMax = vJoy[0].continuousPovMax
	if wiimote[0].buttons.button_down(WiimoteButtons.DPadLeft):		#Down
		vJoy[0].setAnalogPov(0, cPovMax / 2)
	elif wiimote[0].buttons.button_down(WiimoteButtons.DPadRight):	#Up
		vJoy[0].setAnalogPov(0, 0)
	elif wiimote[0].buttons.button_down(WiimoteButtons.DPadUp):		#Left
		vJoy[0].setAnalogPov(0, cPovMax * 3 / 4)
	elif wiimote[0].buttons.button_down(WiimoteButtons.DPadDown):	#Right
		vJoy[0].setAnalogPov(0, cPovMax / 4)
	else:
		vJoy[0].setAnalogPov(0, -1)

vJoy[0].setButton(8, keyboard.getKeyDown(Key.LeftArrow))
vJoy[0].setButton(9, keyboard.getKeyDown(Key.RightArrow))
	

if starting:
	wiimote[0].acceleration.update += wiimoteAccelerationUpdate
	wiimote[0].buttons.update += wiimoteButtonUpdate
	