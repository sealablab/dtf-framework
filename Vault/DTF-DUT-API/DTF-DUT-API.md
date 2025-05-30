
# DUT-API 
* Dut-Init  -> bool
* Dut-Reset -> none
* Dut-Test(int i) -> json dict
## Dut-Init
Dut-init performs any one-time initialization of resources required to to communicate with the DUT, as well as any 'one-time' setup for a given target. This would include things like
* initialize a digilent HS2 JTAG connection to the DUT
* Open up a serial port to the DUT
* ..more exotic things like PCI 


## Dut-Reset
Dut-Reset should perform a 'soft-reset' on the dut. This may be accomplishes in a variety of ways, all of which will be target specific and depend on Dut-Init having opened whatever necessary comms channel is used. 

## Dut-Test(int TestID)
A programmer targetting a new DUT will 'export' (for lack of a better word) a handful of functions. 

The goal of exposing these functions through a numerically defined TestID is that the (internal) DUT state and naming scheme should be completely irrelevant to the overall testing pipeline


Suggest a filesystem layout-naming convention that would it make it easy to run tests from both the CLI and as well as a simple FastAPI server. 

## DUTTest:
DUTTest will, when given a path/name of a specific DUT:
	* Invoke DUT-Init, Dut-Reset, Dut-Test(testID=1)
	* 

## DUTTestServer
The DUTTestServer will, when given a path/name of a specific DUT:

Expose the three mentioned mandatory API calls from a simple FastAPI server at obvious endpoints

## DUTTestClient
The DUTTestClient when given a **DUTTestServer** IP and port will:

Exercise * Invoke DUT-Init, Dut-Reset, Dut-Test(testID=1)

* Invoke DUT-Init, Dut-Reset, Dut-Test(testID=1) on the specified server

