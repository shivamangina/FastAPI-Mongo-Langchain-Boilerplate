from fastapi import FastAPI


app = FastAPI()

# get request
@app.get("/")
def index():
    return {"data": {"name": "Ram"}} # Server Health Check


students = {
    1: {
        "name": "John",
        "age": 17,
        "city": "New York"},
    2: {
        "name": "Jane",
        "age": 16,
        "city": "Chicago"}

}

# Path Parameters
@app.get("/student/{student_id}")
def get_student(student_id: int): # Path(None, description="The ID of the student you want to view", gt=0, lt=3) issue with path
    return students[student_id]


# Query Parameters
@app.get("/studentbyname")
def get_student(name: str = None): # Path(None, description="The ID of the student you want to view", gt=0, lt=3) issue with path
    for student in students:
        if students[student]["name"] == name:
            return students[student]
    return {"data": "Not Found"}


# Query Parameters with path parameters



# Post Request Body


# Put method


# Delete method




# Pet Name generator using Lang chain
# https://www.youtube.com/watch?v=lG7Uxts9SXs&t=216s
