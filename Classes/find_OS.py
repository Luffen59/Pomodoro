
import platform

from Classes.implementation import Implementation
from Classes.implementation_windows import WindowsImplementation
from Classes.implementation_linux import LinuxImplementation
from Classes.implementation_macos import MacOSImplementation


class OSFinder:
    def __init__(self):
        self.implementations = {
            'Windows': WindowsImplementation,
            'Linux': LinuxImplementation,
            'Darwin': MacOSImplementation,
        }

    def get_platform_implementation(self):
        system = platform.system()
        implementation_class = self.implementations.get(system)

        if implementation_class:
            return implementation_class()
        else:
            raise NotImplementedError("Unsupported operating system")
