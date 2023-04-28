from sqlalchemy import Column, Integer, String
from blog.models.database import db
from blog.models.article_tag import article_tag_association_table
from sqlalchemy.orm import relationship


class Tag(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(32), nullable=False, default="", server_default="")

    tags = relationship(
        "Tag",
        secondary=article_tag_association_table,
        back_populates="articles",)