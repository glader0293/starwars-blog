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

    favorite_characters = relationship("FavoriteCharacter", back_populates="user", cascade="all, delete-orphan")
    favorite_planets = relationship("FavoritePlanet", back_populates="user",cascade="all, delete-orphan")

class Character(db.Model):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    favorited_by = relationship("FavoriteCharacter", back_populates="character", cascade="all, delete-orphan")

class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    favorited_by = relationship("FavoritePlanet", back_populates="planet", cascade="all, delete-orphan")

class FavoriteCharacter(db.Model):
    __tablename__ = 'favorite_character'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    character_id: Mapped[int] =mapped_column(ForeignKey('character.id'))

    user = relationship("User", back_populates="favorite_characters")
    character = relationship("Character", back_populates="favorited_by")

class FavoritePlanet(db.Model):
    __tablename__ = 'favorite_planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id')) #links the table object with the name of the table
    planet_id: Mapped[int] =mapped_column(ForeignKey('planet.id')) #links the table object with the name of the table

    user = relationship("User", back_populates="favorite_planets")
    planet = relationship("Planet", back_populates="favorited_by")