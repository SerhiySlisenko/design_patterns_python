from typing import List

from behavioral.state.state import State
from behavioral.state.state_impl.locked_state import LockedState


class LockContext:
    """
    The Context defines the interface of interest to clients.
    It also maintains a reference to an instance of a State subclass, which represents the current state of the Context.
    The Context forces the State to respond to user input instead of itself.
    The reaction may be different depending on which State is currently active.
    """

    def __init__(self, combination: List[int]) -> None:
        self.__password = "".join([str(c) for c in combination])
        self.pass_length = len(self.__password)
        self.__state = LockedState()
        self.trial_password = ''

    def set_state(self, state: State) -> None:
        self.__state = state

    def enter_digit(self, digit: int) -> None:
        self.__state.enter(self, digit)

    def reset_lock(self) -> None:
        self.__state.reset(self)

    def set_new_password(self, combination: List[int]) -> None:
        self.__state.set_password(self, combination)

    def is_password_matched(self) -> bool:
        is_matched = False
        if self.pass_length != len(self.trial_password):
            if self.__password.startswith(self.trial_password):
                is_matched = True
        else:
            if self.__password == self.trial_password:
                is_matched = True

        return is_matched

    def _update_pass(self, combination: List[int]) -> None:
        self.__password = "".join([str(c) for c in combination])
        self.pass_length = len(self.__password)
