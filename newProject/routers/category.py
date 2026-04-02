from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from newProject.schemas.schemas import CategoryCreate, CategoryResponse
from newProject.models.models import Category
from newProject.dependencies.depencencies import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()