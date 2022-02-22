from __future__ import annotations

from typing import TYPE_CHECKING

from behavioral.hw_jira_workflow.state import State

if TYPE_CHECKING:
    from behavioral.hw_jira_workflow.jira_context import JiraContext


class ClosedState(State):
    """
    Described 'Closed' state of JIRA.
    """

    def reopen(self, jira_context: JiraContext) -> None:
        jira_context.change_assignee("")

        from . import OpenedState
        jira_context.set_state(OpenedState())
        print("JIRA state changed from 'Resolved' to 'Opened' state")