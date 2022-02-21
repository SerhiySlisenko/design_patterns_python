from typing import TYPE_CHECKING

from behavioral.hw_jira_workflow.state import State

if TYPE_CHECKING:
    from behavioral.hw_jira_workflow.jira_context import JiraContext


class OpenedState(State):
    """
    Described 'Opened' state of JIRA
    """

    def start_progress(self, jira_context: JiraContext) -> None:
        pass

    def resolve(self, jira_context: JiraContext) -> None:
        pass
