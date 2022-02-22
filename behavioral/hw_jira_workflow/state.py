from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from jira_context import JiraContext


class State(ABC):
    """
    The base State class declares methods that all Concrete State should implement.
    We create default for all methods realisation.
    """

    def start_progress(self, context: JiraContext) -> None:
        print("start progress command - is not allowed!")

    def stop_progress(self, context: JiraContext) -> None:
        print("stop progress command - is not allowed!")

    def resolve(self, context: JiraContext) -> None:
        print("resolve command - is not allowed!")

    def reopen(self, context: JiraContext) -> None:
        print("reopen command - is not allowed!")

    def verify(self, context: JiraContext) -> None:
        print("verify command - is not allowed!")

    def close(self, context: JiraContext) -> None:
        print("close command - is not allowed!")
