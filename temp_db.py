import sqlite3


def update_table_work_cost():
    """Обновление таблицы "work_cost" в БД в соответствии с таблицей "fieldlist". Сравнение по артикулам."""

    values_ = []
    connect_to_db = sqlite3.connect('fieldlist_var2.db')
    cursor_connect_to_db = connect_to_db.cursor()
    cursor_connect_to_db.execute("SELECT articul from fieldlist")
    for row in cursor_connect_to_db:
        values_.append(row)
        print(values_)

    sql_ = "insert into work_cost (detail) values (?)"
    for i in range(len(list(values_))):
        val = values_[i]
        cursor_connect_to_db.execute(sql_, val)
    # connect_to_db.commit()


if __name__ == "__main__":
    update_table_work_cost()


