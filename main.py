 jgkjniuhnyvb i n
 def on_forever():
    basic.show_icon(IconNames.sad)
    servos.P0.stop()
    servos.P0.set_range(0, 180)
basic.forever(on_forever)
