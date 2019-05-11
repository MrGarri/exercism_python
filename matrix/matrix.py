class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = self._get_rows(matrix_string)
        self.columns = self._get_columns(self.rows)

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]

    @staticmethod
    def _get_rows(matrix_string):
        rows = []
        for row in matrix_string.splitlines():
            values = [int(value) for value in row.split()]
            rows.append(values)

        return rows

    @staticmethod
    def _get_columns(rows):
        columns = []
        for i in range(0, len(rows[0])):
            columns.append([row[i] for row in rows])

        return columns
