from fastapi import FastAPI
from create_tables import create_all
from routers import blog, user, authentication
from fastapi_pagination import add_pagination
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/create-table")
def read_root():
    create_all()
    return {"Message": "Tables created successfully"}


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)

add_pagination(app)
