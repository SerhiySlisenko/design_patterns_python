from __future__ import annotations
from typing import List, TYPE_CHECKING

from behavioral.state.state import State
from behavioral.state.state_impl.error_state import ErrorState
from behavioral.state.state_impl.open_state import OpenState

if TYPE_CHECKING:
    from behavioral.state.lock_context import LockContext


class LockedState(State):
    """
    Concrete States implement various behaviors, associated with a state of the Context.
    Concrete States themselves can transfer the context into other States.
    From LockedState the Context could be moved to any other State.
    """

    def enter(self, context: LockContext, digit: int) -> None:
        context.trial_password += f'{digit}'
        print(f"Enter {digit}. Entered passphrase: {context.trial_password}")
        print("Check if password correct...")
        if context.pass_length != len(context.trial_password):
            if not context.is_password_matched():
                print("Password is not correct. Please reset entered combination.")
                context.set_state(ErrorState())
            else:
                print("You have entered the correct digit! Move on and enter the next digit.")
        else:
            if context.is_password_matched():
                print("Password is correct. Now safe is opened.")
                context.set_state(OpenState())
            else:
                print("Password is not correct. Please reset entered combination.")
                context.set_state(ErrorState())

    def reset(self, context: LockContext) -> None:
        print("Reset of the entered combination is performed.")
        context.trial_password = ''
        context.set_state(LockedState())

    def set_password(self, context: LockContext, combination: List[int]) -> None:
        print("You cannot set a new password while safe is locked.")
