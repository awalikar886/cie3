from account import account_details

def test_account_details():
     expected_output = (
        f"acc_no: {141}",
        f"hol_name: {akash}",
        f"acc_type: {current}",
        f"bal: {4000}"
    )
     assert account_details(141, "Akash", "current", 4000) == expected_output

