from enum import Enum


class BaseConsts(Enum):
    @classmethod
    def get_choices(cls):
        choices = {}

        for const in cls:
            choices[const.name] = const.value

        return choices
