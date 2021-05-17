from typing import Text
from pydantic import BaseModel, PositiveInt, constr
from sqlalchemy.sql.sqltypes import CHAR
#import models3


class Shipper(BaseModel):
    ShipperID: PositiveInt
    CompanyName: constr(max_length=40)
    Phone: constr(max_length=24)

    class Config:
        orm_mode = True

class Supplier(BaseModel):
    SupplierID: PositiveInt
    CompanyName: constr(max_length=40)
    ContactName: constr(max_length=30) = None
    ContactTitle: constr(max_length=30) = None
    Address: constr(max_length=60) = None
    City: constr(max_length=15) = None
    Region: constr(max_length=15) = None
    PostalCode: constr(max_length=10) = None
    Country: constr(max_length=15) = None
    Phone: constr(max_length=24) = None
    Fax: constr(max_length=24) = None
    HomePage: Text = None

    class Config:
        orm_mode = True

class Supplier1(BaseModel):
    SupplierID: PositiveInt
    CompanyName: constr(max_length=40)

    class Config:
        orm_mode = True

class Region(BaseModel):
    RegoinID: PositiveInt
    RegionDescription: constr(max_length=20)

    class Config:
        orm_mode = True

class Category(BaseModel):
    CategoryID: PositiveInt
    CategoryName: Text

    class Config:
        orm_mode = True

class Product(BaseModel):
    ProductID: PositiveInt
    ProductName: Text
    Category: Category
    Discontinued: int

    class Config:
        orm_mode = True

class SupplierNew(BaseModel):
    CompanyName: constr(max_length=40)
    ContactName: constr(max_length=30) = None
    ContactTitle: constr(max_length=30) = None
    Address: constr(max_length=60) = None
    City: constr(max_length=15) = None
    Region: constr(max_length=15) = None
    PostalCode: constr(max_length=10) = None
    Country: constr(max_length=15) = None
    Phone: constr(max_length=24) = None

class SupplierPut(BaseModel):
    CompanyName: constr(max_length=40)
    ContactName: constr(max_length=30)
    ContactTitle: constr(max_length=30)
    Address: constr(max_length=60)
    City: constr(max_length=15)
    Region: constr(max_length=15)
    PostalCode: constr(max_length=10)
    Country: constr(max_length=15)
    Phone: constr(max_length=24)
    Fax: constr(max_length=24) = None
    HomePage: Text = None

    class Config:
        orm_mode = True
