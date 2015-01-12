#!/usr/bin/env python3
__author__ = 'nikolojedison'
#To change this template use Tools | Templates.

from networktables import NetworkTable
import wpilib
dead_zone = .1

def precision_mode(controller_input, button_state):
    """copied from CubertPy, b/c it worked"""
    if controller_input <= dead_zone and controller_input >= -dead_zone:
        return 0
    elif controller_input > 0:
        controller_input = ((controller_input-dead_zone)/(1-dead_zone))**3
    else:
        controller_input = ((-controller_input-dead_zone)/(dead_zone-1))**3

    if button_state:
        return controller_input * 0.5
    else:
        return controller_input

class Lopez_Jr(wpilib.SampleRobot):
    def robotInit(self):
        """initialises robot as a mecanum with 2 joysticks"""
        self.drive = wpilib.RobotDrive(3, 1, 2, 0)
        self.drive.setExpiration(0.1)
        self.stick_left = wpilib.Joystick(0)
        self.stick_right = wpilib.Joystick(1)
        self.drive.setInvertedMotor(self.drive.MotorType.kFrontLeft, True)
        self.drive.setInvertedMotor(self.drive.MotorType.kRearLeft, True)
        self.gyro = wpilib.Gyro(0)
        self.aux_left = wpilib.Jaguar(6)
        self.aux_right = wpilib.Jaguar(4)
        self.window_motor = wpilib.Jaguar(5)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

    def autonomous(self):
        """does nothing as of yet"""
        pass

    def operatorControl(self):
        """Runs the motors with mecanum steering."""

        self.drive.setSafetyEnabled(True)

        while self.isOperatorControl() and self.isEnabled():
            precision = self.stick_right.getRawButton(1)
            x = precision_mode(self.stick_right.getX(), precision) # precision mode on x axis
            y = precision_mode(self.stick_right.getY(), precision) # precision mode on y axis
            z = precision_mode(self.stick_right.getZ(), precision) # precision mode on z axis

            aux = precision_mode(self.stick_left.getY(), precision) # precision mode on aux motors
            window_motor = precision_mode(self.stick_left.getX(), precision) # precision mode on window motor
            self.smart_dashboard.putNumber("Gyro",self.gyro.getAngle())
            
            gyro_angle = 0

            self.drive.mecanumDrive_Cartesian(x, y, z, 0)   # mecanum drive

            self.aux_left.set(aux) # auxiliary left miniCIM
            self.aux_right.set(aux)# auxiliary right miniCIM
            self.window_motor.set(window_motor) # random window motor that electrical hooked up

            wpilib.Timer.delay(.005)    # wait for a motor update time

    def test(self):
        """no tests yet, woo"""
        pass

if __name__ == "__main__":
    wpilib.run(Lopez_Jr)
