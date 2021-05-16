from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import asc
import schemas
import models, models2


def get_shippers(db: Session):
    return db.query(models.Shipper).all()


def get_shipper(db: Session, shipper_id: int):
    return (
        db.query(models.Shipper).filter(models.Shipper.ShipperID == shipper_id).first()
    )

def get_suppliers(db: Session):
    return db.query(models.Supplier).all()

def get_supplier(db: Session, id: int):
    return (
        db.query(models.Supplier).filter(models.Supplier.SupplierID == id).first()
    )

def get_regions(db: Session):
    return db.query(models.Region).all()

def get_product(db: Session, id: int):
    return db.query(models.Product).filter(models.Product.SupplierID == id).order_by(models.Product.ProductID.desc()).all()

def post_supplier(db: Session, supplier_new: schemas.SupplierNew):
    supplier_add = models2.Supplier(
        CompanyName = supplier_new.CompanyName,
        ContactName = supplier_new.ContactName,
        ContactTitle = supplier_new.ContactTitle,
        Address = supplier_new.Address,
        City = supplier_new.City,
        PostalCode = supplier_new.PostalCode,
        Country = supplier_new.Country,
        Phone = supplier_new.Phone
    )
    db.add(supplier_add)
    db.commit()
    db.refresh(supplier_add)
    return supplier_add