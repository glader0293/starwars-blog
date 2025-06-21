from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100))

    favorites = relationship("Favorite", back_populates="user", cascade="all, delete-orphan")

class Character(db.Model):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    item_id: Mapped[int] = mapped_column(Integer, nullable=False)
    item_type: Mapped[str] = mapped_column(String(50), nullable=False) 

    user = relationship("User", back_populates="favorites")

    @property
    def item(self):
        if self.item_type == 'character':
            return db.session.get(Character, self.item_id)
        elif self.item_type == 'planet':
            return db.session.get(Planet, self.item_id)
        return None