from xrpl.models.transactions import Payment
from xrpl.models.amounts import IssuedCurrencyAmount
from scripts._shared import load_state, wallet_from_seed, submit_tx
from rich import print

def main():
    st = load_state()
    m = wallet_from_seed(st["merchant"]["seed"])
    tx = Payment(
        account=m.classic_address,
        destination=st["issuer"]["address"],
        amount=IssuedCurrencyAmount(currency=st["currency"], issuer=st["issuer"]["address"], value=st["purchase_amount"]),
    )
    print("[bold]Merchant redeems vouchers[/bold]")
    submit_tx(tx, m)

if __name__ == "__main__":
    main()
