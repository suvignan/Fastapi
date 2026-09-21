from fastapi import  FastAPI
from . import models
from .database import engine
from .routers import post,users,auth
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# as we are using alembic for migrations, we don't need to create the tables manually, so we can comment this line
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"] # this is used to allow all origins to access the api, this is not recommended for production, but for development it is fine


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
      # if you want to allow only specific methods, you can specify them here, for example: ["GET", "POST"]
    allow_headers=["*"], 
    # if you want to allow only specific headers, you can specify them here, for example: ["Content-Type", "Authorization"]
)


app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):

#     posts=db.query(models.Post).all() 
#     return {'data': posts}


