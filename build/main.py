
from fastapi import FastAPI
from MyService import MyService
import uvicorn
app = FastAPI()
myservice_func=MyService
@app.get("/")
def hello_world():
    msg="Welcome to my FastAPI project!"        "Please visit the /docs to see the API documentation."
    return msg

    
# WARNING:DO NOT EDIT THE BELOW LINE
app.add_api_route(
        path="/test",
        endpoint=myservice_func.predict,
        methods=['GET'],
    )

        
if __name__ == "__main__":
    uvicorn.run(
    app=app,
    host='0.0.0.0',
    port=5000
)