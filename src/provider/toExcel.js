import { utils, write, writeFile } from 'xlsx'


function toExcel(jsonData, filename) {
    let woksheet = utils.json_to_sheet(jsonData)
    let workbook = utils.book_new()

    utils.book_append_sheet(workbook, woksheet, filename)
    write(workbook, { bookType: 'xlsx', type: 'buffer' })
    write(workbook, { bookType: 'xlsx', type: 'binary' })
    writeFile(workbook, filename + ".xlsx")
};

export default toExcel;

