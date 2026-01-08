def account_details(acc_no, hol_name, acc_type, bal):
    result = (
        f"acc_no: {acc_no}"
        f"hol_name: {hol_name}"
        f"acc_type: {acc_type}"
        f"bal: {bal}"
    )
    return result


if __name__ == "__main__":
    acc_no = 141
    hol_name = akash
    acc_type = current
    bal = 4000
    print(account_details(acc_no,hol_name,acc_type, bal))
