from xrpl.models.transactions import Payment
from xrpl.models.amounts import IssuedCurrencyAmount
from scripts._shared import load_state, wallet_from_seed, submit_tx
from rich import print

def main():
    st = load_state()
    issuer = wallet_from_seed(st["issuer"]["seed"])
    tx = Payment(
        account=st["issuer"]["address"],
        destination=st["beneficiary"]["address"],
        amount=IssuedCurrencyAmount(currency=st["currency"], issuer=st["issuer"]["address"], value=st["voucher_issue_amount"]),
    )
    print("[bold]Issuing vouchers[/bold]")
    submit_tx(tx, issuer)

if __name__ == "__main__":
    main()
