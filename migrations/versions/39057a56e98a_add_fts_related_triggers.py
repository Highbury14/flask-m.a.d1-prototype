"""Add FTS related Triggers

Revision ID: 39057a56e98a
Revises: d6a7938b2d87
Create Date: 2021-11-06 15:50:58.730489

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = '39057a56e98a'
down_revision = 'd6a7938b2d87'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    sql = text("""
            CREATE TRIGGER article_ai AFTER INSERT ON article BEGIN
              INSERT INTO article_search(rowid, title, content) VALUES (new.article_id, new.title, new.content);
            END;
        """)
    conn.execute(sql)
    sql = text("""
        CREATE TRIGGER article_ad AFTER DELETE ON article BEGIN
          INSERT INTO article_search(article_search, rowid, title, content) VALUES('delete', old.article_id, old.title, old.content);
        END;
    """)
    conn.execute(sql)

    sql = text("""
        CREATE TRIGGER article_au AFTER UPDATE ON article BEGIN
          INSERT INTO article_search(article_search, rowid, title, content) VALUES('delete', old.article_id, old.title, old.content);
          INSERT INTO article_search(rowid, title, content) VALUES (new.article_id, new.title, new.content);
        END;   
        """)
    conn.execute(sql)

    sql = text(""" INSERT INTO article_search(article_search) VALUES('rebuild') """)
    conn.execute(sql)    

def downgrade():
    conn = op.get_bind()
    sql = text(""" DROP TRIGGER article_ai """)
    conn.execute(sql)
    sql = text(""" DROP TRIGGER article_ad """)
    conn.execute(sql)
    sql = text(""" DROP TRIGGER article_au """)
    conn.execute(sql)
