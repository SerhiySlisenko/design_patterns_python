class CodeBuilder:
    def __init__(self, root_name: str):
        self.root_name = root_name
        self.fields = []

    def add_field(self, name: str, value: str):
        self.fields.append(f"{' '*4}self.{name} = {value}")
        return self

    def __str__(self):
        return self.print()

    def print(self):
        lines = list()
        lines.append(f"class {self.root_name}:")
        if self.fields:
            lines.append(f"{' '*2}def __init__(self):")
            for field in self.fields:
                lines.append(field)
        else:
            lines.append(f"{' '*2}pass")
        return '\n'.join(lines)
