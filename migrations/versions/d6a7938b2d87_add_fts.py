"""Add FTS

Revision ID: d6a7938b2d87
Revises: a7798a17d124
Create Date: 2021-11-06 15:43:41.722889

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = 'd6a7938b2d87'
down_revision = 'a7798a17d124'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    sql = text("""CREATE VIRTUAL TABLE article_search USING fts5(title, content, content=article, content_rowid=article_id, tokenize="porter unicode61");""")
    conn.execute(sql)

def downgrade():
    op.drop_table("article_search")
