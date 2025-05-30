from dtf_dut_base import DTF_DUT_Base

class ExampleDUT(DTF_DUT_Base):
    """
    Example DUT implementation with required and optional tests.
    """

    def dut_init(self):
        print("[init] ExampleDUT initialized.")

    def dut_reset(self):
        print("[reset] ExampleDUT reset.")

    def dut_echo(self):
        print("[echo] ExampleDUT alive.")
        return True

    def do_custom_150(self):
        print("[custom] TestID 150 running...")

    def _register_custom_tests(self):
        self.tests.register(150, self.do_custom_150)
