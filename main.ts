input.onGesture(Gesture.FreeFall, function () {
    basic.showIcon(IconNames.Confused)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 5000, 1, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    Kitronik_Move_Motor.stop()
    Move = true
})
input.onSound(DetectedSound.Loud, function () {
    basic.showIcon(IconNames.Happy)
    Move = !(Move)
    if (Move) {
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 44)
    } else {
        Kitronik_Move_Motor.stop()
    }
})
let Move = false
Move = false
input.setSoundThreshold(SoundThreshold.Loud, 29)
