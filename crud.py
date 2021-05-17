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

def put_supplier(db: Session, supplier: schemas.SupplierPut, supplier_id: int):
    db_supplier = db.query(models2.Supplier).filter(models2.Supplier.SupplierID == supplier_id).one_or_none()
    for var, value in vars(supplier).items():
        setattr(db_supplier, var, value) if value else None

    db.merge(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def delete_supplier(db: Session, supplier_id: int):
    db_delete = db.query(models2.Supplier).filter(models2.Supplier.SupplierID == supplier_id).first()
    db.delete(db_delete)
    db.commit()
    return 
    