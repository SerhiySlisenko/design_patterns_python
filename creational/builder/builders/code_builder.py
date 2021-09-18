from __future__ import annotations

from creational.builder.class_type import Class
from creational.builder.field_type import Field


class CodeBuilder:
    """
    The CodeBuilder is the builder to create python class with optional fields
    """
    def __init__(self, root_name: str):
        self.__class = Class(root_name)

    def add_field(self, name: str, value: str) -> CodeBuilder:
        self.__class.fields.append(Field(name, value))
        return self

    def __str__(self):
        return self.__class.__str__()

