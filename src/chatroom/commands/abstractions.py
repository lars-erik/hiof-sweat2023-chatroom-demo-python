from typing import TypeVar, Generic


class Command:
    pass

TCommand = TypeVar('TCommand', bound=Command)

class CommandHandler(Generic[TCommand]):
    def execute(self, command:TCommand):
        pass

