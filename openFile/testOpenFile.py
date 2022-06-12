import openpyxl as opx




def main():
    book = opx.open('Meta.xlsx', read_only=True)
    sheet = book.active
    count = [0] * sheet.max_column
    top = 0
    row = 1
    # for row in range(0, sheet.max_column):
    #     date = sheet[1][row].value
    #     for x in range(0, 1):
    #         count[top] = date
    #         top += 1
    # print(count)
    while top != sheet.max_column:
        date = sheet[1][top].value
        count[top] = date
        top += 1
    print(count)








        # count = [0]
        # count.append(date)
        # print(count)
    #num = [date]
    #print(num)




main()

