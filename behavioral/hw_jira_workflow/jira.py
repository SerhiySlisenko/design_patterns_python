class Jira:
    """
     Contains some of the important components of the Jira.
     """
    def __init__(self, key: str, reporter: str) -> None:
        self.key = key
        self.reporter = reporter
        self.assignee = ""

    def __str__(self) -> str:
        return f"Jira: '{self.key}' - reporter is '{self.reporter}', assignee is " \
               f"'{self.assignee if self.assignee != '' else 'Unassigned'}')"

    def __repr__(self) -> str:
        return f"Jira: {self.key})"
