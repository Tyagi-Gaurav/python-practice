row_start = "<tr>"
row_end = "</tr>"


def __to_html(deal):
    table_start = "<table class=\"tg\">"
    headers_list = [row_start]
    __add_table_header(headers_list)
    for i in range(0, len(deal.odd)):
        headers_list.append("<th class=\"tg-0lax\">" + deal.odd[i].event_name + "</th>")
    headers_list.append(row_end)

    headers_list.append(row_start)
    __add_table_header(headers_list, "Odds")
    for i in range(0, len(deal.odd)):
        headers_list.append("<th class=\"tg-0lax\">" + str(deal.odd[i].f_odd) + "</th>")
    headers_list.append(row_end)

    __add_generic_row(headers_list, "Returns", deal.returns)
    __add_generic_row(headers_list, "Roi", deal.roi_array)

    table_end = "</table>"
    return table_start + ''.join(headers_list) + table_end


def __add_generic_row(headers_list, heading, arr):
    headers_list.append(row_start)
    __add_table_header(headers_list, heading)
    for i in range(0, len(arr)):
        headers_list.append("<th class=\"tg-0lax\">" + str(arr[i]) + "</th>")
    headers_list.append(row_end)


def __add_table_header(headers_list, header=""):
    headers_list.append("<th class=\"tg-0lax\">" + header + "</th>")


def __css():
    return "<style type=\"text/css\"> \
                .tg  {border-collapse:collapse;border-spacing:0;} \
                .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} \
                .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;} \
                .tg .tg-0lax{text-align:left;vertical-align:top} \
            </style>"


def formatter(matched_deals):
    tables = ["<html>", "<body>", __css()]
    for deal in matched_deals:
        tables.append(__to_html(deal))
    tables.append("</body></html>")
    return ''.join(tables)
