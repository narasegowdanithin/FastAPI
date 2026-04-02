from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from newProject.models.models import Cart,Order, OrderItem, CartItem , User
from newProject.dependencies.depencencies import get_db, get_current_user

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/checkout")
def checkout(db: Session = Depends(get_db),
             user: User = Depends(get_current_user)):

    #cart = db.query(Cart).first()
    cart = db.query(Cart).filter(Cart.user_id == user.id).first()

    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total_price = 0

    # create order for this user
    order = Order(user_id=user.id, total_price=0)
    db.add(order)
    db.commit()
    db.refresh(order)

    # convert cart → order items move items from cart to order items, calculate total
    for item in cart.items:
        total_price += item.product.price * item.quantity

        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        )

        db.add(order_item)

    # update total
    order.total_price = total_price

    # clear cart
    for item in cart.items:
        db.delete(item)

    db.commit()

    return {
        "user": user.username,
        "order_id": order.id,
        "total_price": total_price,
        "message": "Order placed successfully"
    }

@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/myOrders")
def get_my_orders(db: Session = Depends(get_db),user: User = Depends(get_current_user)):
    orders = db.query(Order).filter(Order.user_id == user.id).all()
    return [{
        "order_id": orders.id,
        "total_price": orders.total_price,
        "items": [
            {
                "product": item.product.name,
                "price": item.price,
                "quantity": item.quantity
            }
            for item in orders.items
        ]
    }]