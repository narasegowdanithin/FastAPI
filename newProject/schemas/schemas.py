from pydantic import BaseModel,Field

class CategoryCreate(BaseModel):
    name: str


class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0) # price must be greater than 0
    category_id: int


class ProductResponse(BaseModel):
    id: int
    price: float

    class Config:
        from_attributes = True

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int


class CartItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    total_price: float

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True