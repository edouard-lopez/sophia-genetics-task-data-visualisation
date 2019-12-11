from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.feeder import Feeder

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/user-usage")
def user_usage():
    return Feeder().user_usage()

@app.get("/domain-x")
def domainX():
    return Feeder().domainX()

@app.get("/domain-y")
def domainY():
    return Feeder().domainY()

@app.get("/categories-y")
def categoriesY():
    return Feeder().categoriesY()



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}