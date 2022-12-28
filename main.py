def on_gesture_free_fall():
    basic.show_icon(IconNames.CONFUSED)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
            5000,
            1,
            255,
            255,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    Kitronik_Move_Motor.stop()
    Move = False
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_sound_loud():
    global Move
    basic.show_icon(IconNames.HAPPY)
    Move = not (Move)
    if Move:
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 44)
    else:
        Kitronik_Move_Motor.stop()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

Move = False
input.set_sound_threshold(SoundThreshold.LOUD, 29)