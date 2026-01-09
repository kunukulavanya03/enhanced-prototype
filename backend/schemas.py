from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class FieldsBase(BaseModel):
    HARDCODED: int
    to: datetime
    hover: str
    Context: datetime
    sm: str
    selected: str
    id: str
    focus: str
    button: str
    skeleton: str
    normal: str
    placeholder: str
    file: str
    selection: str

class FieldsCreate(FieldsBase):
    pass

class FieldsResponse(FieldsBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DataBase(BaseModel):
    HARDCODED: int
    to: datetime
    hover: str
    Context: datetime
    sm: str
    selected: str
    id: str
    focus: str
    button: str
    skeleton: str
    normal: str
    placeholder: str
    file: str
    selection: str

class DataCreate(DataBase):
    pass

class DataResponse(DataBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DatabaseBase(BaseModel):
    HARDCODED: int
    to: datetime
    hover: str
    Context: datetime
    sm: str
    selected: str
    id: str
    focus: str
    button: str
    skeleton: str
    normal: str
    placeholder: str
    file: str
    selection: str

class DatabaseCreate(DatabaseBase):
    pass

class DatabaseResponse(DatabaseBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class RestaurantBase(BaseModel):
    HARDCODED: int
    to: datetime
    hover: str
    Context: datetime
    sm: str
    selected: str
    id: str
    focus: str
    button: str
    skeleton: str
    normal: str
    placeholder: str
    file: str
    selection: str

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantResponse(RestaurantBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    HARDCODED: int
    to: datetime
    hover: str
    Context: datetime
    sm: str
    selected: str
    id: str
    focus: str
    button: str
    skeleton: str
    normal: str
    placeholder: str
    file: str
    selection: str

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class FunctionBase(BaseModel):
    HARDCODED: int
    to: datetime
    hover: str
    Context: datetime
    sm: str
    selected: str
    id: str
    focus: str
    button: str
    skeleton: str
    normal: str
    placeholder: str
    file: str
    selection: str

class FunctionCreate(FunctionBase):
    pass

class FunctionResponse(FunctionBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

