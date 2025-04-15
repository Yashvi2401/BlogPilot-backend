from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <-- Add this
from create_tables import create_all
from routers import blog, user, authentication
from fastapi_pagination import add_pagination
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",  # Local development frontend
    "https://blog-pilot.vercel.app"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],              # Allow all HTTP methods
    allow_headers=["*"],              # Allow all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/create-table")
async def read_root():
    await create_all()
    return {"Message": "Tables created successfully"}

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)

add_pagination(app)
