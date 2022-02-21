from typing import List

from behavioral.hw_jira_workflow.state import State
from behavioral.hw_jira_workflow.jira import Jira
from behavioral.hw_jira_workflow.state_impl.opened_state import OpenedState


class JiraContext:
    """
    The Context defines the interface of interest to clients.
    It also maintains a reference to an instance of a State subclass, which represents the current state of the Context.
    The Context forces the State to respond to user input instead of itself.
    The reaction may be different depending on which State is currently active.
    """

    def __init__(self, jira: Jira) -> None:
        self.__jira = jira
        self.__state = OpenedState()

    def set_state(self, state: State) -> None:
        self.__state = state

    def start_work_on_jira(self) -> None:
        self.__state.start_progress(self)

    def stop_work_on_jira(self) -> None:
        self.__state.stop_progress(self)

    def resolve_jira(self) -> None:
        self.__state.resolve(self)

    def reopen_jira(self) -> None:
        self.__state.reopen(self)

    def verify_jira(self) -> None:
        self.__state.verify(self)

    def close_jira(self, closer_name) -> None:
        self.__state.close(self, closer_name)
