from abc import ABC, abstractmethod


class MatchManager:
    def __init__(self):
        self.match = None
        self.active = True
        self.last_player = None

    def set_match(self, match):
        self.match = match

    def end_match(self):
        self.active = False


class MatchVisitTemplate(ABC):

    def process_visit(self, player, visit):
        """Skeleton of operations to perform. DON'T override me.

        The Template Method defines a skeleton of an algorithm in an operation,
        and defers some steps to subclasses.
        """

        status, message = self.validate_visit(player, visit)
        if status is False:
            return message

        self.check_winning_condition(visit)

        self.record_statistics()

        return self.format_summary()

    @abstractmethod
    def validate_visit(self, player, visit):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def check_winning_condition(self):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def record_statistics(self):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass

    @abstractmethod
    def format_summary(self):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass
