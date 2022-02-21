from typing import TYPE_CHECKING

from behavioral.hw_jira_workflow.state import State

if TYPE_CHECKING:
    from behavioral.hw_jira_workflow.jira_context import JiraContext


class InProgressState(State):
    """
    Described 'In Progress' state of JIRA
    """

    def stop_progress(self, jira_context: JiraContext) -> None:
        pass

    def resolve(self, jira_context: JiraContext) -> None:
        pass
