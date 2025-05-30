# Dut-RUN
**Dut-RUN** 

**Dut-RUN** is responsible for running a target specific

A programmer targetting a new DUT will 'export' (for lack of a better word) a handful of functions. 

The goal of exposing these functions through a numerically defined TestID is that the (internal) DUT state and naming scheme should be completely irrelevant to the overall testing pipeline

**Dut-RUN** will assume that:
* [[DUT-Reset]] and [[DUT-Init]] have previously been called on the device.

