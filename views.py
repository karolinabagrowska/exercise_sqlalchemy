from starlette import responses, status
from models import Supplier
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import PositiveInt
from sqlalchemy.orm import Session

import crud, schemas
from database import get_db
#import models3

router = APIRouter()


@router.get("/shippers/{shipper_id}", response_model=schemas.Shipper)
async def get_shipper(shipper_id: PositiveInt, db: Session = Depends(get_db)):
    db_shipper = crud.get_shipper(db, shipper_id)
    if db_shipper is None:
        raise HTTPException(status_code=404, detail="Shipper not found")
    return db_shipper


@router.get("/shippers", response_model=List[schemas.Shipper])
async def get_shippers(db: Session = Depends(get_db)):
    return crud.get_shippers(db)

@router.get("/suppliers/{id}", response_model=schemas.Supplier)
async def get_supplier(id: PositiveInt, db: Session = Depends(get_db)):
    db_supplier = crud.get_supplier(db, id)
    if db_supplier is None:
        raise HTTPException(status_code=404)
    return db_supplier

@router.get("/suppliers", response_model=List[schemas.Supplier1])
async def get_suppliers(db: Session = Depends(get_db)):
    return crud.get_suppliers(db)

@router.get("/regions", response_model=schemas.Region)
async def get_regions(db: Session = Depends(get_db)):
    return crud.get_regions

@router.get("/suppliers/{id}/products", response_model=List[schemas.Product])
async def get_suppliers_product(id: int, db: Session = Depends(get_db)):
    check_id = crud.get_supplier(db, id)
    if check_id is None:
        raise HTTPException(status_code=404)
    else:

        return crud.get_product(db, id)


@router.post("/suppliers", response_model=schemas.Supplier, status_code=status.HTTP_201_CREATED)
async def post_supplier(supplier_new: schemas.SupplierNew, db: Session = Depends(get_db)):
    return crud.post_supplier(db, supplier_new)
    
@router.put("/suppliers/{supplier_id}")
async def put_supplier(supplier: schemas.SupplierPut, supplier_id: int, db: Session = Depends(get_db)):
    check_id = crud.get_supplier(db, supplier_id)
    if check_id is None:
        raise HTTPException(status_code=404)
    return crud.put_supplier(db, supplier, supplier_id)

@router.delete("/suppliers/{supplier_id}", status_code=status.HTTP_204_NO_CONTENT, response_class= Response)
async def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    check_id = crud.get_supplier(db, supplier_id)
    if check_id is None:
        raise HTTPException(status_code=404)
    return crud.delete_supplier(db, supplier_id)

