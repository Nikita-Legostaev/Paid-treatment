from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Product_feature_association(Base):
    __tablename__='product_feature_association'

    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), primary_key=True)
    feature_id: Mapped[int] = mapped_column(ForeignKey('product_features.id'), primary_key=True)