from __future__ import annotations
from typing import List, TYPE_CHECKING

from behavioral.state.state import State


if TYPE_CHECKING:
    from behavioral.state.lock_context import LockContext


class OpenState(State):
    """
    Concrete States implement various behaviors, associated with a state of the Context.
    Concrete States themselves can transfer the context into other States.
    From OpenState the Context could be moved only to LockedState if set new password.
    """

    def enter(self, context: LockContext, digit: int) -> None:
        print("You cannot enter a new digit. You are already unlocked.")

    def reset(self, context: LockContext) -> None:
        print("You cannot reset entered combination. You are already unlocked.")

    def set_password(self, context: LockContext, combination: List[int]) -> None:
        print("Set new password and lock the safe.")
        context._update_pass(combination)

        from behavioral.state.state_impl.locked_state import LockedState
        context.set_state(LockedState())
