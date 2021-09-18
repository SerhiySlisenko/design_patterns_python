class Class:
    """
    Contains some of the important components of the class that are required
    in order to construct the class object (could be extended to add e.g. methods).
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.fields = []

    def __str__(self) -> str:
        lines = list()
        lines.append(f"class {self.name}:")
        if not self.fields:
            lines.append(f"{' '*2}pass")
        else:
            lines.append(f"{' '*2}def __init__(self):")
            for field in self.fields:
                lines.append(f"{' '*4}{field}")

        return '\n'.join(lines)
