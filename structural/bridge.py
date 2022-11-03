"""
Bridge -
"""

from abc import ABC, abstractmethod


class Implementation(ABC):
    """
    The Implementation defines the interface for all implementation classes. It
    doesn't have to match the Abstraction's interface. In fact, the two
    interfaces can be entirely different. Typically the Implementation interface
    provides only primitive operations, while the Abstraction defines higher-
    level operations based on those primitives.
    """
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class Abstraction:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """

    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self) -> str:
        return ("Abstraction: Base operation with: \n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
    You can extend abstraction without implementation
    """
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ConcreteImplementationAAA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationBBB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationBBB: Here's the result on the platform B."


def call(abstraction: Abstraction):
    print(abstraction.operation())


if __name__ == '__main__':
    a = Abstraction(ConcreteImplementationAAA())
    call(a)

    b = Abstraction(ConcreteImplementationBBB())
    call(b)
