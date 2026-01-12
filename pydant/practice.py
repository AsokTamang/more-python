import datetime
from pydantic import BaseModel, ValidationError,AfterValidator
from typing import Optional,Annotated,Any

data = {
    "customer_name": "asok",
    "reservation_date": "31 Dec 2025, Time 19:00",
    "number_of_guests": 8,
    "special_requests": "Table near the window"
}

def is_valid(value: Any) -> datetime.datetime:
    if type(value) == str:
        return datetime.datetime.strptime(value, "%d %b %Y, Time %H:%M")

    return value

Reservation_Date = Annotated[str, AfterValidator(is_valid)]  #here we are storing the process of changing the type in this variable

class Reservation(BaseModel):
    customer_name: str
    reservation_date: Reservation_Date
    number_of_guests: int
    special_requests: Optional[str] = None  # here we are making the special_requests var to be optinal


def create_reservation(data):
    try:
        r = Reservation(customer_name=data.get("customer_name"), reservation_date=data.get("reservation_date"),
                        number_of_guests=data.get("number_of_guests"))
        print(r)
    except ValidationError as e:
        print('Validation error occured',e)

create_reservation(data)




