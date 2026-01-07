from xrpl.models.transactions import Payment
from xrpl.models.amounts import IssuedCurrencyAmount
from scripts._shared import load_state, wallet_from_seed, submit_tx
from rich import print

def main():
    st = load_state()
    b = wallet_from_seed(st["beneficiary"]["seed"])
    tx = Payment(
        account=b.classic_address,
        destination=st["merchant"]["address"],
        amount=IssuedCurrencyAmount(currency=st["currency"], issuer=st["issuer"]["address"], value=st["purchase_amount"]),
    )
    print("[bold]Beneficiary pays merchant[/bold]")
    submit_tx(tx, b)

if __name__ == "__main__":
    main()
