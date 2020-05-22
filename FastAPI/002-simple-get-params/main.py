from fastapi import FastAPI

app = FastAPI()

""" The code below will cause "internal server error"
	Because input can be both str as well as int and
	we cannot add 1 to string.
	
		if not mentioned, input is taken as str by defalult.
		

@app.get("/addone/{input_num}")
async def func(input_num):
	return {"1 + {input_num}": 1+input_num}
"""

@app.get("/addone/{input_num}")
def func(input_num: int):
	return f"1 + {input_num} is : {1+input_num}"
