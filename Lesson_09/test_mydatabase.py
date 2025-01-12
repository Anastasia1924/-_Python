from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"  # Изменено на 'postgresql'
db = create_engine(db_connection_string)

def test_add():
    connection = db.connect()
    transaction = connection.begin()

    sql_check = text("select count(*) from  employee")
    #добавление строки
    sql_insert = text("INSERT INTO public.employee (is_active, create_timestamp, change_timestamp, first_name, last_name, phone, company_id) VALUES(false, '2024-01-10 12:05:16.659 +0400', '2024-01-10 13:05:16.659 +0400', 'Anastasiia', 'Gosteeva', '+79278165385', 1)")

    result = connection.execute(sql_check)
    rows_before = result.mappings().all()
    count_before = rows_before[0]
    count_before_num = count_before['count']

    connection.execute(sql_insert)
    transaction.commit()

    result_after = connection.execute(sql_check)
    rows_after = result_after.mappings().all()
    count_after = rows_after[0]
    count_after_num = count_after['count']

    assert count_before_num < count_after_num

    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql_update = text("UPDATE employee SET is_active=true where id = 86")
    connection.execute(sql_update)
    transaction.commit()
    sql_check = text("select * from  employee where id = 86")
    result = connection.execute(sql_check)
    rows = result.mappings().all()
    rows1 = rows[0]
    current_is_active = rows1['is_active']
    assert current_is_active is True

    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql_delete = text("DELETE FROM employee WHERE id = 92")
    connection.execute(sql_delete)
    transaction.commit()
    sql_check = text("select * from  employee where id = 92")
    result = connection.execute(sql_check)
    rows = result.mappings().all()

    assert rows == []
