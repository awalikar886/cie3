def account_details(acc_no, hol_name, acc_type, bal):
    result = (
        f"acc_no: {acc_no}\n"
        f"hol_name: {hol_name}\n"
        f"acc_type: {acc_type}\n"
        f"bal: {bal}\n"
    )
    return result


if __name__ == "__main__":
    acc_no = "{141}"
    hol_name = "{akash}"
    acc_type = "{current}"
    bal = "4000}
    print(account_details(acc_no,hol_name,acc_type, bal))
