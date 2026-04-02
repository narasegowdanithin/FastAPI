from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from newProject.models.models import Cart, CartItem, Product, User
from newProject.schemas.schemas import CartItemCreate, CartItemResponse
from newProject.dependencies.depencencies import get_db, get_current_user

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.post("/add", response_model=CartItemResponse)
def add_to_cart(
    item: CartItemCreate,
    db: Session = Depends(get_db),
    user : User = Depends(get_current_user) # injected user (for later, to link cart to user)
):
    
    
    product = db.query(Product).filter(Product.id == item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # create cart (for now simple, later link to user)
    #now added user_id to cart, so we can find cart by user
    # find user's cart
    cart = db.query(Cart).filter(Cart.user_id == user.id).first()
    # check product exists
    cart = db.query(Cart).first()
    if not cart:
        cart = Cart(user_id=user.id)
        db.add(cart)
        db.commit()
        db.refresh(cart)

    cart_item = CartItem(
        cart_id=cart.id,
        product_id=item.product_id,
        quantity=item.quantity
    )

    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)

    return cart_item

@router.get("/")
def view_cart(db: Session = Depends(get_db),
                user : User = Depends(get_current_user)):
    #cart = db.query(Cart).first()
    cart = db.query(Cart).filter(Cart.user_id == user.id).first()

    if not cart:
        return {"message": "Cart is empty"}

    return {
        "username" : user.username,
        "cart_id": cart.id,
        "items": [
            {
                "product": item.product.name,
                "price": item.product.price,
                "quantity": item.quantity
            }
            for item in cart.items
        ]
    }

@router.get("/")
def view_cart(db: Session = Depends(get_db)
                #user : User = Depends(get_current_user) # for later, to get user's cart
                ):
    cart = db.query(Cart).first()

    if not cart:
        return {"message": "Cart is empty"}

    return {
        "cart_id": cart.id,
        "items": [
            {
                "product": item.product.name,
                "price": item.product.price,
                "quantity": item.quantity
            }
            for item in cart.items
        ]
    }