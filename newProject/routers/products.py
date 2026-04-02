from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from newProject.schemas.schemas import ProductCreate, ProductResponse
from newProject.models.models import Product, Category
from newProject.dependencies.depencencies import get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):

    category = db.query(Category).filter(Category.id == product.category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


@router.get("/", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()