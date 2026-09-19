from fastapi import Body, FastAPI, HTTPException, Response, status,Depends,APIRouter
from fastapi.params import Body
from typing import Optional,Dict,List
from pydantic import BaseModel
from random import randrange
from sqlalchemy.orm import Session

from app import oauth
from .. import models,schemas
from .. database import engine, get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db),
                current_user: int = Depends(oauth.get_current_user),
                limit: int =10,skip:int =0,search: Optional[str] = ""): 
    #raw SQL
    # cursor.execute(""" SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()  # using sqlalchemy ORM to get all posts from the database
    return posts



# @app.post("/createposts")
# def create_post(new_post :Post):
#     post_dict =new_post.dict() # converts the pydantic model to dictionary
#     post_dict['id'] = randrange(0,100000) # generates a random id for the post
#     my_post.append(post_dict) # appends the new post to the list of posts
#     return {"data": post_dict}
# #title string, content string, ctagerory, Boolean



@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db),
                 current_user: int = Depends(oauth.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,
    #                (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit() # commit the changes to the 
    #Pydantic model is used to validate the data and convert it to a dictionary
    new_post = models.Post(owner_id=current_user.id,**post.dict()) # create a new post object using the pydantic model
    db.add(new_post) # add the new post to the database session
    db.commit() # commit the changes to the database
    db.refresh(new_post) # refresh the new post to get the id from the database
    return new_post # return the new post object

    
#RETRIVING A POST BY ID
 
# @app.get("/posts/{id}")
# def get_post(id:int,response :Response):
#     post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"post with id {id} not found")
#     #  response.status_code = status.HTTP_404_NOT_FOUND
#     #  return {"message":f"post with id {id} not found"}
#     return {"post_detail": post}


@router.get("/{id}",response_model=schemas.Post)
def get_post(id:int,db: Session = Depends(get_db),
                current_user: int = Depends(oauth.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    # post=cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id).first() # using sqlalchemy ORM to get a post by id
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} not found")
    return post



#Deleting a post by id
@router.delete("/{id}",response_model=schemas.Post)
def delete_post(id:int,db: Session = Depends(get_db),
                current_user: int = Depends(oauth.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    #Deleting a post by id
    #find the index in the array that has the required id
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} not found")
    if post.owner_id != current_user.id:
     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="You are not the owner of this post")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#Updating a post by id
@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.UpdatePost,db: Session = Depends(get_db),
                current_user: int = Depends(oauth.get_current_user)):
    #Put request is used to update a post by id
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s 
    #                 RETURNING *""",
    #                (post.title,post.content,post.published,str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    # we chgeck if the index is None
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        # if not found we raise an HTTPException with status code 404 and a message
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                             detail=f"post with id {id} not found")
    if post.owner_id != current_user.id:
     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="You are not the owner of this post")
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    # we convert the pydantic model to a dictionary and update the post in the list of posts
    return post_query.first()