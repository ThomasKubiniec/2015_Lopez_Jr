__author__ = 'nikolojedison'
from .set_claw_setpoint import SetClawSetpoint
import setpoints

class GrabTote(SetClawSetpoint):
    """Grabba da tote, man. Needs testing w. the sandpaper blocks."""

    def __init__(self, robot):
        super().__init__(robot, setpoints.kTote)

    def isFinished(self):
        #Finishes the command if it reaches the setpoint or current draw is above kStallPoint.
        return super().isFinished() or self.robot.claw.current.getVoltage() > setpoints.kStall
