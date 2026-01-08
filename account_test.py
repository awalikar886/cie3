from account import account_details

def test_account_details():
     expected_output = (
        "acc_no: 141\n",
        "hol_name: Akash\n",
        "acc_type: current\n",
        "bal: 4000\n"
    )
    
assert account(141, "Akash", "current", 4000)==expected_output
