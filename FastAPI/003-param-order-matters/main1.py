from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
    
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}
    
"""
Because path operations(.get, .post etc.) are evaluated 
in order,
	api "thinks" `me` is also some kind of `user_id`.
	So, order matters!
	
See main2.py for correct implementatuon
"""