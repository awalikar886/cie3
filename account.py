def account_details(acc_no, hol_name, acc_type, bal):
    result = (
        f"acc no: {acc_no}\n"
        f"hol  Name: {hol_name}\n"
        f"type: {acc_type}\n"
        f"bal: {bal}\n"
    )
    return result


if _name_ == "_main_":
    acc_no = "141"
    hol_name = "akash"
    acc_type = "current
    bal = 4000
    print(account_details(acc_no,hol_name,acc_type, bal))
