
from fastapi import FastAPI
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# while True:

#     try:
#         connection = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                       password='Davidgreen12345@', cursor_factory=RealDictCursor)
#         cursor = connection.cursor()
#         print("Connected to the database")
#         break
#     except Exception as e:
#         print("Could not connect to the database", e)
#         time.sleep(2)
