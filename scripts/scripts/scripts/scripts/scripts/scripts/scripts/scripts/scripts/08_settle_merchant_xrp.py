from xrpl.models.transactions import Payment
from scripts._shared import load_state, wallet_from_seed, submit_tx, drops
from rich import print

def main():
    st = load_state()
    issuer = wallet_from_seed(st["issuer"]["seed"])
    tx = Payment(
        account=issuer.classic_address,
        destination=st["merchant"]["address"],
        amount=drops(float(st["xrp_settlement"])),
    )
    print("[bold]Settling merchant in XRP[/bold]")
    submit_tx(tx, issuer)

if __name__ == "__main__":
    main()
