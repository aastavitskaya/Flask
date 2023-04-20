"""empty message

Revision ID: a79449bbb0a7
Revises: e4d367914384
Create Date: 2023-04-20 14:03:10.443984

"""
from alembic import op
import sqlalchemy as sa
from blog.models.user import User
from blog.models.database import db


# revision identifiers, used by Alembic.
revision = 'a79449bbb0a7'
down_revision = 'e4d367914384'
branch_labels = None
depends_on = None


def upgrade():
    admin = User(username='admin', is_staff=True)
    db.session.add(admin)
    db.session.commit()


def downgrade():
    admin = User.query.filter_by(username="admin")
    db.session.delete(admin)
    db.session.commit()