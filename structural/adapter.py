"""
Adapter - allows objects with incompatible interfaces to collaborate
"""


class Target:
    """
    Defines the domain-specific interfaces
    """

    def request(self):
        return "target"


class Adaptee:
    """
    Defines an existing interface that needs adapting
    """

    def specific_request(self):
        return "custom request"


class Adapter(Target, Adaptee):
    """
    Adapts the interface Adaptee to the Target interface
    """

    def request(self):
        return f"transform {self.specific_request()}"


def call(target: Target):
    print(target.request())


if __name__ == '__main__':
    target = Target()
    call(target)

    adapter = Adapter()
    call(adapter)
