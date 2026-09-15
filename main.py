from fastapi import Body, FastAPI
from fastapi.params import Body
from typing import Optional,Dict
from pydantic import BaseModel
from random import randrange


app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool
    rating : Optional[int] = None
    id : Optional[int] = None


my_post = [{"title":'title of post 1', "content":'content of post 1','id':1},
            {"title":'title of post 2', "content":'content of post 2',"id":2}]




def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def get_posts():
    return {"data": my_post}



@app.post("/createposts")
def create_post(new_post :Post):
    post_dict =new_post.dict() # converts the pydantic model to dictionary
    post_dict['id'] = randrange(0,100000) # generates a random id for the post
    my_post.append(post_dict) # appends the new post to the list of posts
    return {"data": post_dict}
#title string, content string, ctagerory, Boolean


#RETRIVING A POST BY ID
 
@app.get("/posts/{id}")
def get_post(id:int):
    print(type(id))
    post = find_post(id)
    
    return {"post_detail": f"post with id {id} is retrieved"}


