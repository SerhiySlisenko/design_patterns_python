class Jira:
    """
     Contains some of the important components of the Jira.
     """
    def __init__(self, key: str, reporter: str) -> None:
        self.key = key
        self.reporter = reporter
        self.assignee = ""
        self.closer = ""

    def __str__(self) -> str:
        return f"Jira: {self.key})"

    def __repr__(self) -> str:
        return f"Jira: {self.key})"
