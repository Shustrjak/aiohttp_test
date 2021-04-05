from sqlalchemy import create_engine, MetaData
from web_docs.settings import config
from web_docs.db import table_documents


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[table_documents])


def sample_data(engine):
    conn = engine.connect()
    data = {'name': 'name_doc_19',
            'created': '2020-09-23 00:00:00',
            'updated': '2020-10-24 00:00:00'}
    conn.execute(table_documents.insert(), [data])
    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)
    create_tables(engine)
    sample_data(engine)
