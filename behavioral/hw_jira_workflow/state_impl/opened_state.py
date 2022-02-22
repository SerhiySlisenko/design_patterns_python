from __future__ import annotations

from typing import TYPE_CHECKING

from behavioral.hw_jira_workflow.state import State

if TYPE_CHECKING:
    from behavioral.hw_jira_workflow.jira_context import JiraContext


class OpenedState(State):
    """
    Described 'Opened' state of JIRA
    """

    def start_progress(self, jira_context: JiraContext) -> None:
        from . import InProgressState
        jira_context.set_state(InProgressState())
        print("JIRA state changed from 'Opened' to 'In Progress' state")

    def resolve(self, jira_context: JiraContext) -> None:
        jira_context.change_assignee(jira_context.get_reporter())

        from . import ResolvedState
        jira_context.set_state(ResolvedState())
        print("JIRA state changed from 'Opened' to 'Resolved' state")
