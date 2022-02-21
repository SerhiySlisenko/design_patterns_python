from typing import TYPE_CHECKING

from behavioral.hw_jira_workflow.state import State

if TYPE_CHECKING:
    from behavioral.hw_jira_workflow.jira_context import JiraContext


class ClosedState(State):
    """
    Described 'Closed' state of JIRA.
    """

    def reopen(self, jira_context: JiraContext) -> None:
        pass
