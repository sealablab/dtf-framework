# TestCommand
**TestCommand**  consists of 
[[TestID]]


is the datatype that [[Dut-Run]] **must return**

``` python
from pydantic import BaseModel, PositiveInt
class TestResults(BaseModel): 
	int: TestID
	dict TestResults
```