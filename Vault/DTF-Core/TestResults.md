# TestResults
**TestResults** is the datatype that [[Dut-Run]] **must return**

``` python
from pydantic import BaseModel, PositiveInt
class TestResults(BaseModel): 
	int: TestID
	str: TestSumarr
	dict TestResults
```