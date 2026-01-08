from account import account_details

def test_account_details():
     expected_output = (
         f"acc_no:141"\n
        f"hol_name:akash"\n
        f"acc_type:current"\n
        f"bal:4000"
    )
     assert account_details(141,"akash","current",4000)==expected_output

