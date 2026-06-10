# Import required FastAPI modules
from fastapi import FastAPI, HTTPException

# Import modules for serving static files (CSS, JS)
from fastapi.staticfiles import StaticFiles


# Import Jinja2 for rendering HTML templates
from fastapi.templating import Jinja2Templates


# Import Request object required by Jinja2 templates
from fastapi import Request


# Create FastAPI application
app = FastAPI()


# Mount static folder to serve CSS and JavaScript files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure templates folder
templates = Jinja2Templates(directory="templates")

# Sample user data stored in memory
users = {
    1:
    {
        "name":"poojitha",
        "gender":"female"
    },
    2:
    {
        "name":"sai",
        "gender":"male"
    },
    3:
    {
        "name":"sri",
        "gender":"female"
    },
    4:
    {
        "name":"Devansh",
        "gender":"male"
    }
}

# Home page route
# Loads index.html when user visits "/"
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# Route to get all users
# Used by JavaScript to display user data in table
@app.get("/all-users")
def all_users():
    return users

# Route to get a specific user using user ID
@app.get("/users/{user_id}")
def get_users(user_id: int):
    if user_id in users:
        return f"Hello {users[user_id]}"
    else:
        raise HTTPException(status_code=404, detail="User not found")
        

# Route to add a new user
@app.post("/users-entry/{user_id}/{user_name}/{gender}")
def create_users(user_id: int, user_name: str, gender: str):

    # Check whether user already exists
    if user_id in users:
        return {"message": "User already exists"}

     # Add new user
    users[user_id] = {
        "name": user_name,
        "gender": gender
    }

    return {"message": "User created"}

# Route to update user name
@app.put("/users-update/{user_id}/{user_name}")
def update_users(user_id:int,user_name:str):
    # Check whether user exists
    if user_id in users:
        # Update only the name
        users[user_id]["name"] = user_name
        return {
            "message": f"User with ID {user_id} updated successfully to {user_name}"
        }
    else:        raise HTTPException(status_code=404, detail="User not found")

# Route to delete a user
@app.delete("/users-delete/{user_id}")
def delete_users(user_id:int):
    # Check whether user exists
    if user_id in users:
        del users[user_id]
        return {
            "message": f"User with ID {user_id} deleted successfully"
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")

