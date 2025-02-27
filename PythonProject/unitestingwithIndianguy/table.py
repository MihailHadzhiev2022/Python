from playwright.sync_api import sync_playwright,Page,expect


def test_table(page:Page):
    page.goto("http://uitestingplayground.com/dynamictable")


    #given chrome CPI %

    chrome_label = page.locator('p.bg-warning').inner_text()
    #get the % sign in the text
    percentage = chrome_label.split()[-1]

    #locate all column headers

    column_headers =page.get_by_role('columnheader')
    cpu_column = None

    for index in range(column_headers.count()):
        column_header = column_headers.nth(index)

        if column_header.inner_text() == "CPU":
            cpu_column = index
            break


    assert cpu_column != None
    rowgroup = page.get_by_role("rowgroup").last
    chrome_row = rowgroup.get_by_role("row").filter(has_text="Chrome")
    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)

    expect(chrome_cpu).to_have_text(percentage)