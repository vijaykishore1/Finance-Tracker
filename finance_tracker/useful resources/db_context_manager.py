import sqlite3


class Sqlite:
    def __init__(self, file="sqlite.db"):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    with Sqlite("../db/ExpenseManager.db") as cur:
        print(cur.execute("select sqlite_version();").fetchall()[0][0])
