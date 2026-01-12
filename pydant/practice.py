import datetime
from pydantic import BaseModel
from typing import Optional

data = {
    "customer_name": "asok",
    "reservation_date": "2026-08-24",
    "number_of_guests": 8,
}
class Reservation(BaseModel):
    customer_name: str
    reservation_date: datetime.date
    number_of_guests: int
    special_requests: Optional[str] = None  # here we are making the special_requests var to be optinal

r=Reservation(customer_name= data.get("customer_name"),reservation_date=data.get("reservation_date"),number_of_guests=data.get("number_of_guests"))
print(r)
