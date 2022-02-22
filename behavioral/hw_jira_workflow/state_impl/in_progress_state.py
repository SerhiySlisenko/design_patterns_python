from __future__ import annotations

from typing import TYPE_CHECKING

from behavioral.hw_jira_workflow.state import State

if TYPE_CHECKING:
    from behavioral.hw_jira_workflow.jira_context import JiraContext


class InProgressState(State):
    """
    Described 'In Progress' state of JIRA
    """

    def stop_progress(self, jira_context: JiraContext) -> None:
        from . import OpenedState
        jira_context.set_state(OpenedState())
        print("JIRA state changed from 'In Progress' to 'Opened' state")

    def resolve(self, jira_context: JiraContext) -> None:
        jira_context.change_assignee(jira_context.get_reporter())

        from . import ResolvedState
        jira_context.set_state(ResolvedState())
        print("JIRA state changed from 'In Progress' to 'Resolved' state")
