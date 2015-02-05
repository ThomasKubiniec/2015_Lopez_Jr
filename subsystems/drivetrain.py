import math

import wpilib
from wpilib.command import Subsystem
from commands.mecanum_drive_with_joystick import MecanumDriveWithJoystick
from drive_control import drive_control
from imu_simple import IMUSimple

class GyroDummy:
    """Makes the sim happy. Written by Aux."""
    n = 0
    def getYaw(self):
        n = self.n
        n = n+1
        if n > 180:
            n = n-360
        elif n < -180:
            m = n+360
        self.n = n
        return n

class Drivetrain(Subsystem):
    '''Class drivetrain uses a few Talons to run a 'bot.
    '''

    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.drive = wpilib.RobotDrive(3, 1, 2, 0)
        self.drive.setExpiration(0.1)

        self.drive.setInvertedMotor(self.drive.MotorType.kFrontRight, True)
        self.drive.setInvertedMotor(self.drive.MotorType.kRearRight, True)

        if robot.isReal():
            self.gyro = IMUSimple()
        else:
            self.gyro = GyroDummy()


    def initDefaultCommand(self):
        '''When no other command is running let the operator drive around
           using the joystick'''
        self.setDefaultCommand(MecanumDriveWithJoystick(self.robot))

    def log(self):
        wpilib.SmartDashboard.putNumber("Gyro", self.gyro.getYaw())

    def driveJoystick(self, joystick):
        precision = joystick.getRawButton(1)
        x = drive_control(joystick.getX(), precision)
        y = drive_control(joystick.getY(), precision)
        z = drive_control(joystick.getZ(), precision)
        self.driveManual(x,y,z)

    def driveManual(self, x, y , rotation):
        self.drive.mecanumDrive_Cartesian(x, y, rotation, 0)
