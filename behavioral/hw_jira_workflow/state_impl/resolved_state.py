from __future__ import annotations

from typing import TYPE_CHECKING

from behavioral.hw_jira_workflow.state import State

if TYPE_CHECKING:
    from behavioral.hw_jira_workflow.jira_context import JiraContext


class ResolvedState(State):
    """
    Described 'Resolved' state of JIRA.
    """

    def reopen(self, jira_context: JiraContext) -> None:
        jira_context.change_assignee("")

        from . import OpenedState
        jira_context.set_state(OpenedState())
        print("JIRA state changed from 'Resolved' to 'Opened' state")

    def verify(self, jira_context: JiraContext) -> None:
        if jira_context.get_assignee().lower() in (jira_context.get_reporter().lower(), 'senior'):
            jira_context.change_assignee("Manager")

            from . import VerifiedState
            jira_context.set_state(VerifiedState())
            print("JIRA state changed from 'Resolved' to 'Verified' state")
        else:
            print("Only reporter or any senior can verify JIRA. Please change assignee!")

