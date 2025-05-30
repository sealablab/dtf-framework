from collections.abc import Callable


# DTF_Dut_Interface
## the dtf_dut_interface specifies the very simple DTF-Test-Id (integer) to DUT-specific functionality.
class DTF_Dut_Interface:
    """the dtf_dut_interface specifies the very simple DTF-Test-Id (integer) to DUT-specific functionality."""

    def __init__(self):
        self._dispatch: dict[int, Callable] = {}

    def register(self, test_id: int, fn: Callable):
        if not callable(fn):
            raise TypeError(f"TestID {test_id} must be mapped to a callable.")
        if test_id in self._dispatch:
            raise ValueError(f"TestID {test_id} already registered.")
        self._dispatch[test_id] = fn

    def run(self, test_id: int, *args, **kwargs):
        fn = self._dispatch.get(test_id)
        if fn is None:
            raise KeyError(f"No handler registered for TestID {test_id}")
        return fn(*args, **kwargs)

    def __getitem__(self, test_id: int):
        return self._dispatch[test_id]

    def __contains__(self, test_id: int):
        return test_id in self._dispatch

    def keys(self):
        return self._dispatch.keys()

    def values(self):
        return self._dispatch.values()

    def items(self):
        return self._dispatch.items()

    def __repr__(self):
        return f"<DTF_Dut_Interface {sorted(self._dispatch.keys())}>"
