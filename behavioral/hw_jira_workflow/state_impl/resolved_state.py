from typing import TYPE_CHECKING

from behavioral.hw_jira_workflow.state import State

if TYPE_CHECKING:
    from behavioral.hw_jira_workflow.jira_context import JiraContext


class ResolvedState(State):
    """
    Described 'Resolved' state of JIRA.
    """

    def reopen(self, jira_context: JiraContext) -> None:
        pass

    def verify(self, jira_context: JiraContext) -> None:
        pass

