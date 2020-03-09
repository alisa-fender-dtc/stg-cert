import xlrd

class InputSpreadsheet():
    def __init__(self, input_file):
        self.input_file = input_file
        self.query_dict = self.convert_spreadsheet_to_query_dictionary()

    def convert_spreadsheet_to_query_dictionary(self):
        workbook = xlrd.open_workbook(self.input_file)
        sheet = workbook.sheet_by_index(0)
        num_rows = sheet.nrows
        num_cols = sheet.ncols
        headers = {}
        query_dict = {}

        for r in range(0, num_rows):
            if r == 0:
                for c in range (0, num_cols):
                    headers[c] = sheet.cell_value(r, c)
            else:
                query_dict[r] = {}
                for c in range (0, num_cols):
                    value = sheet.cell_value(r, c)
                    if headers[c].lower() == 'year' and value != '':
                        value = int(sheet.cell_value(r, c))

                    query_dict[r][headers[c]] = value


        # print(query_dict)
        return query_dict


# if __name__ == '__main__':
#     input_file = r"../../challenge10/search_input.xlsx"
#     insp = InputSpreadsheet(input_file)
#     query = insp.query_dict




