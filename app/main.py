from fastapi import FastAPI
from routers import blog, user, authentication
from fastapi_pagination import add_pagination
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)

add_pagination(app)
