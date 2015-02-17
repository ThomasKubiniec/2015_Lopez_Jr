__author__ = 'nikolojedison'
#***************************
#*|\    | | |  /   /  /   |*
#*| \   | | | /      /    |*
#*|  \  | | |/      /     |*
#*|   \ | | |\      ---/  |*
#*|    \| | | \       /   |*
#*|     | | |  \     /    |*
#*|     | | |   \   /     |*
#***************************
#(ascii art, pay no mind.)
#2/12 21:30 - a little tired due to last night, but still going. Waiting on robot.
#2/13 17:53 - waiting on robot, again. Things are working fine in programming though.
#2/13 22:00 - working on setpoints, slowly but surely.
#2/14 13:40 - waiting on more things.
#2/14 23:30 - got the mapping done on the joysticks - waiting on auton testing and a gamepad for presets
#2/15 21:05 - post-ICC. This'll prove interesting.
#2/16 15:06 - gamepad is finally here, recalculated setpoints. Still deciding on what is going to map where.
#2/17 09:53 - Getting close on implementing the gamepad. Noticed that this is the first dev log with only 3 digits.

import wpilib
from networktables import NetworkTable
from wpilib.buttons import JoystickButton, InternalButton
from commands.lift_go_to_level import LiftGoToLevel
from commands.open_claw import OpenClaw
from commands.close_claw import CloseClaw
from commands.center_claw import CenterClaw
from commands.manual_claw import ManualClaw
from commands.manual_lift import ManualLift
from commands.manual_mast import ManualMast
from commands.mast_back import MastBack
from commands.mast_forward import MastForward
from commands.grab_tote import GrabTote
from commands.grab_can import GrabCan
from commands.turn import Turn
from commands.lift_stuff import LiftStuff
from commands.shaker import Shaker
from commands.mast_button import MastButton
from commands.tote_loader import ToteLoader
from commands.super_strafe_64 import SuperStrafe64 #Only on Nintendo64.
from pov_button import POVButton
from commands.drive_straight import DriveStraight

class KeyButton(InternalButton):
    def __init__(self, table, code):
        def listener(table, key, value, isNew):
            if isNew and key=="Keys":
                if code in value:
                    self.setPressed(True)
                else:
                    self.setPressed(False)
        table.addTableListener(listener)


class OI:
    """OI! Put yo button maps hea!"""
    def __init__(self, robot):
        """Warning: Metric tonnes of code here. May need to be tidied up a wee bit."""

        self.stick_left = wpilib.Joystick(0)
        self.stick_right = wpilib.Joystick(1)
        self.pad = wpilib.Joystick(2)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

#        print('Key pressed:', self.smart_dashboard.getNumber('Key'))

        #Buttons? Aw, man, I love buttons! *bleep bloop* Key, numeric array

        # Create some buttons on the left stick (which is really not, but I don't wanna disturb the preexisting code).
        left_trigger = JoystickButton(self.stick_left, 1)
        left_thumb = JoystickButton(self.stick_left, 2)
        left_three = JoystickButton(self.stick_left, 3)
        left_four = JoystickButton(self.stick_left, 4)
        left_five = JoystickButton(self.stick_left, 5)
        left_six = JoystickButton(self.stick_left, 6)
        left_seven = JoystickButton(self.stick_left, 7)
        left_eight = JoystickButton(self.stick_left, 8)
        left_nine = JoystickButton(self.stick_left, 9)
        left_ten = JoystickButton(self.stick_left, 10)
        left_eleven = JoystickButton(self.stick_left, 11)
        left_twelve = JoystickButton(self.stick_left, 12)
        #Create some POV stuff on the left stick, based on angles and the hat switch
        left_north = POVButton(self.stick_left, 0)
        left_northeast = POVButton(self.stick_left, 45)
        left_east = POVButton(self.stick_left, 90)
        left_southeast = POVButton(self.stick_left, 135)
        left_south = POVButton(self.stick_left, 180)
        left_southwest = POVButton(self.stick_left, 225)
        left_west = POVButton(self.stick_left, 270)
        left_northwest = POVButton(self.stick_left, 315)

        #Create some buttons on the ambi stick, see line 48 starting col 49 (Logitech Attack 3)
        right_north = POVButton(self.stick_right, 0)
        right_south = POVButton(self.stick_right, 180)
        right_east = POVButton(self.stick_right, 90)
        right_west = POVButton(self.stick_right, 270)
        right_trigger = JoystickButton(self.stick_right, 1)
        right_thumb = JoystickButton(self.stick_right, 2)
        right_three = JoystickButton(self.stick_right, 3)
        right_four = JoystickButton(self.stick_right, 4)
        right_five = JoystickButton(self.stick_right, 5)
        right_six = JoystickButton(self.stick_right, 6)
        right_seven = JoystickButton(self.stick_right, 7)
        right_eight = JoystickButton(self.stick_right, 8)
        right_nine = JoystickButton(self.stick_right, 9)
        right_ten = JoystickButton(self.stick_right, 10)
        right_eleven = JoystickButton(self.stick_right, 11)
        right_twelve = JoystickButton(self.stick_right, 12)

        #Keypad Buttons
        g1 = KeyButton(self.smart_dashboard, 10)
        g2 = KeyButton(self.smart_dashboard, 11)
        g3 = KeyButton(self.smart_dashboard, 12)
        g4 = KeyButton(self.smart_dashboard, 13)
        g5 = KeyButton(self.smart_dashboard, 14)
        g6 = KeyButton(self.smart_dashboard, 15)
        g7 = KeyButton(self.smart_dashboard, 16)
        g8 = KeyButton(self.smart_dashboard, 17)
        g9 = KeyButton(self.smart_dashboard, 18)
        g10 = KeyButton(self.smart_dashboard, 19)
        g11 = KeyButton(self.smart_dashboard, 20)
        g12 = KeyButton(self.smart_dashboard, 21)
        g13 = KeyButton(self.smart_dashboard, 22)
        g14 = KeyButton(self.smart_dashboard, 23)
        g15 = KeyButton(self.smart_dashboard, 24)
        g16 = KeyButton(self.smart_dashboard, 25)
        g17 = KeyButton(self.smart_dashboard, 26)
        g18 = KeyButton(self.smart_dashboard, 27)
        g19 = KeyButton(self.smart_dashboard, 28)
        g20 = KeyButton(self.smart_dashboard, 29)
        g21 = KeyButton(self.smart_dashboard, 30)
        g22 = KeyButton(self.smart_dashboard, 31)
        topshift = KeyButton(self.smart_dashboard, 32)
        bottomshift = KeyButton(self.smart_dashboard, 33)
        extra1 = KeyButton(self.smart_dashboard, 34)
        extra2 = KeyButton(self.smart_dashboard, 35)
        #25 buttons of stuff on the wall, 25 buttons 'n stuff...
        #Keypresses table = smartdashboard field = Keypresses

        # Connect buttons & commands

        #Bump commands
        left_south.whenPressed(DriveStraight(robot, 0, .25, timeout = .25))
        left_north.whenPressed(DriveStraight(robot, 0, -.25, timeout = .25))
        left_east.whenPressed(DriveStraight(robot, .25, 0, timeout = .35))
        left_west.whenPressed(DriveStraight(robot, -.25, 0, timeout = .35))
        #Mast control
        right_three.whileHeld(MastButton(robot, .38))
        right_four.whileHeld(MastButton(robot, -.38))
        right_east.whenPressed(SuperStrafe64(robot, SuperStrafe64.kLeft))
        right_south.whenPressed(SuperStrafe64(robot, SuperStrafe64.kBack))
        right_north.whenPressed(SuperStrafe64(robot, SuperStrafe64.kForward))
        right_west.whenPressed(SuperStrafe64(robot, SuperStrafe64.kRight))

        left_thumb.whileHeld(Shaker(robot)) #like a Polaroid picture
        left_five.whenPressed(ToteLoader(robot))

        #Generic lift stuff
        left_six.whenPressed(LiftStuff(robot, 1, .1))
        left_four.whenPressed(LiftStuff(robot, -1, .1))
        #Lift presets
        right_eleven.whenPressed(LiftGoToLevel(robot, 1))
        right_nine.whenPressed(LiftGoToLevel(robot, 2))
        right_seven.whenPressed(LiftGoToLevel(robot, 3))
        right_eight.whenPressed(LiftGoToLevel(robot, 4))
        right_ten.whenPressed(LiftGoToLevel(robot, 5))
        right_twelve.whenPressed(LiftGoToLevel(robot, 6))
        #right_trigger.whenPressed() #does some cool 2" lifting and stuff

        #g1 - lift level 1
        #g2 - lift level 2
        #g3 - lift level 3
        #g4 - lift level 4
        #g5 - lift level 5
        #g6 - lift level 6
        #g7 - lift level 7
        #g8 - lift bottom level
        #g9 - auto movement (should find out what this is)
        #g10 - "
        #g11 - "
        #g12 - "
        #g13 - "
        #g14 - "
        #g15 - full open clamp
        #g16 - standing can width
        #g17 - tote width
        #g18 - laying down can width
        #g19 - full closed clamp
        #g20 - full back tilt
        #g21 - leveled paddles
        #g22 - full forward tilt
        #top shift - all levels -.015 for platform stacking
        #bottom shift - all levels +.045 for setdown

    def getJoystickLeft(self):
        """This is the left joystick."""
        return self.stick_left

    def getJoystickRight(self):
        """This is the right joystick."""
        return self.stick_right
