from fastapi import Body, FastAPI, HTTPException, Response, status
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

def find_index_post(id):
    for i,p in enumerate(my_post):
        if p['id'] == id:
            return i


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
def get_post(id:int,response :Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} not found")
    #  response.status_code = status.HTTP_404_NOT_FOUND
    #  return {"message":f"post with id {id} not found"}
    return {"post_detail": post}



#Deleting a post by id
@app.delete("/posts/{id}")
def delete_post(id:int):
    #Deleting a post by id
    #find the index in the array that has the required id
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} not found")
    my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#Updating a post by id
@app.put("/posts/{id}")

def update_post(id:int,post:Post):
    #Put request is used to update a post by id
    index = find_index_post(id)
    # we chgeck if the index is None
    if index == None:
        # if not found we raise an HTTPException with status code 404 and a message
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                             detail=f"post with id {id} not found")
    # we convert the pydantic model to a dictionary and update the post in the list of posts
    post_dict = post.dict()
    post_dict['id'] = id
    my_post[index] = post_dict
    return {"data": post_dict}


