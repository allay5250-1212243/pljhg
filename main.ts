basic.forever(function () {
	
    basic.showIcon(IconNames.sad)
    servos.P0.stop()
    servos.P0.setRange(0, 180)
})
