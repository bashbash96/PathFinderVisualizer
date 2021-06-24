from abc import ABC, abstractmethod


class PathFinderStrategy(ABC):
    """
       The Strategy interface declares operations common to all supported versions
       of some algorithm.

       The Context uses this interface to call the algorithm defined by Concrete
       Strategies.
    """

    @abstractmethod
    def find(self, window, wait, grid, start, end):
        pass


class Context:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy):
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    def get_strategy(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    def set_strategy(self, strategy):
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def find(self, window, wait, grid, start, end):
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        return self._strategy.find(window, wait, grid, start, end)
