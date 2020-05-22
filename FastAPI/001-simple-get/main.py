from fastapi import FastAPI

app = FastAPI()

@app.get("/") # can be .put, .post, .head etc
async def root():
    return {"message": "Hello World"} 
    
# can send non async funcs as well
# Note: '/' needed before 123
@app.get("/123")
def somefunc():
	return 123
	
# can return Pydantic models as well.