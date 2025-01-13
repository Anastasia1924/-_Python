from sqlalchemy import create_engine, inspect, text

class DBPage:
    def __init__(self, db_connection_string):
        self.engine = create_engine(db_connection_string)

    def delete_employee(self, id):
        with self.engine.connect() as connection:
            transaction = connection.begin()
            try:
                sql_delete = text("DELETE FROM employee WHERE id = :id")
                connection.execute(sql_delete, {"id": id})
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e
