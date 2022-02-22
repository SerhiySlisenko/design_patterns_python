from __future__ import annotations

from typing import TYPE_CHECKING

from behavioral.hw_jira_workflow.state import State

if TYPE_CHECKING:
    from behavioral.hw_jira_workflow.jira_context import JiraContext


class VerifiedState(State):
    """
    Described 'Verified' state of JIRA.
    """

    def reopen(self, jira_context: JiraContext) -> None:
        jira_context.change_assignee("")

        from . import OpenedState
        jira_context.set_state(OpenedState())
        print("JIRA state changed from 'Verified' to 'Opened' state")

    def close(self, jira_context: JiraContext) -> None:
        if jira_context.get_assignee().lower() == 'manager':

            from . import ClosedState
            jira_context.set_state(ClosedState())
            print("JIRA state changed from 'Verified' to 'Closed' state")
        else:
            print("Only manager can close JIRA. Please change assignee!")
