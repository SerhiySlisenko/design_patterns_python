from __future__ import annotations
from typing import List, TYPE_CHECKING

from behavioral.state.state import State

if TYPE_CHECKING:
    from behavioral.state.lock_context import LockContext


class ErrorState(State):
    """
    Concrete States implement various behaviors, associated with a state of the Context.
    Concrete States themselves can transfer the context into other States.
    From ErrorState the Context could be moved only to LockedState.
    """

    def enter(self, context: LockContext, digit: int) -> None:
        print("You cannot enter a new digit. You can only reset your entered combination as it is wrong.")

    def reset(self, context: LockContext) -> None:
        print("Reset of the entered combination is performed.")
        context.trial_password = ''
        from behavioral.state.state_impl.locked_state import LockedState
        context.set_state(LockedState())

    def set_password(self, context: LockContext, combination: List[int]) -> None:
        print("You cannot set a new password. You can only reset your entered combination.")
