from pydantic import BaseModel


class User(BaseModel):  #basemodal is used for assigning the type to the properties of a class
    username: str
    age: int
    address: str


asok = User(
    username="asoktmg205@gmail.com",
    age=24,
    address='Kathmandu'
)
print(asok)