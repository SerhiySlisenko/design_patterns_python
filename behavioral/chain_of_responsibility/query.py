from typing import Any

from behavioral.chain_of_responsibility.what_to_query_enum import WhatToQuery


class Query:
    """
    The class is responsible for containing possible fields of query.
    """
    def __init__(self, default_value: Any, what_to_query: WhatToQuery) -> None:
        self.value = default_value
        self.what_to_query = what_to_query
