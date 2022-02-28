from typing import Any


class Searchable:
    def is_goal(self) -> bool:
        pass

    @property
    def siblings(self) -> Any:
        pass

    def step(self) -> bool:
        pass
