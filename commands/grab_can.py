__author__ = "nikolojedison"
from .set_claw_setpoint import SetClawSetpoint
import setpoints

class GrabCan(SetClawSetpoint):
    """Needs testing, w/ and w/o the sandpapers."""

    def __init__(self, robot):
        super().__init__(robot, setpoints.kCan)

    def isFinished(self):
        return super().isFinished() or self.robot.claw.current.getVoltage() > setpoints.kStall
