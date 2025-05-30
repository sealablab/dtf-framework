from abc import ABC, abstractmethod
from dtf_dut_interface import DTF_Dut_Interface

class DTF_DUT_Base(ABC):
    """
    Base class for all DUTs in the DTF ecosystem.
    Automatically registers init/reset/echo into the TestID dispatch table.
    """

    def __init__(self):
        self.tests = DTF_Dut_Interface()
        self.tests.register(100, self.dut_init)
        self.tests.register(101, self.dut_reset)
        self.tests.register(102, self.dut_echo)
        self._register_custom_tests()

    @abstractmethod
    def dut_init(self):
        """Required: TestID 100"""
        pass

    @abstractmethod
    def dut_reset(self):
        """Required: TestID 101"""
        pass

    @abstractmethod
    def dut_echo(self):
        """Required: TestID 102"""
        pass

    def _register_custom_tests(self):
        """Optional override: register extra test IDs (103–254)"""
        pass
