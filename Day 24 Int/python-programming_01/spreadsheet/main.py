# from openpyxl import Workbook
# wb = Workbook()
#
# # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = 42
#
# # Rows can also be appended
# ws.append([1, 2, 3])
#
# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()
#
# # Save the file
# wb.save("sample.xlsx")


import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv_file["Sheet1"]

products_per_supplier = {}
total_value_per_supplier = {}
products_under_10_inv = {}

# how many rows
# print(product_list.max_row)


for product_row in range(2, product_list.max_row + 1):

    # calculation number of products per supplier

    sup_comp_name = product_list.cell(product_row, 4).value
    """using one line if else"""
    # products_per_supplier[sup_comp_name] = products_per_supplier[
    #                                            sup_comp_name] + 1 if sup_comp_name in products_per_supplier else 1

    if sup_comp_name in products_per_supplier:
        cur_num_product = products_per_supplier.get(sup_comp_name)
        products_per_supplier[sup_comp_name] = cur_num_product + 1
    else:
        products_per_supplier[sup_comp_name] = 1

    # calculation total value of inventory per supplier

    inve = product_list.cell(product_row, 2).value
    pric = product_list.cell(product_row, 3).value

    if sup_comp_name in total_value_per_supplier:
        total_value_per_supplier[sup_comp_name] += (inve * pric)
    else:
        total_value_per_supplier[sup_comp_name] = inve * pric

    x = product_list.cell(product_row, 1).value
    y = product_list.cell(product_row, 2).value

    if y < 10:
        products_under_10_inv[x] = y
    else:
        pass


# print(products_per_supplier)
print(total_value_per_supplier)
print(products_under_10_inv)