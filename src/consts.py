from enum import Enum
from typing import Type


class BaseConsts(Enum):
    @classmethod
    def get_choices(cls: Type['BaseConsts']) -> dict:
        choices = {}

        for const in cls:
            choices[const.name] = const.value

        return choices
