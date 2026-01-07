from xrpl.models.transactions import TrustSet
from xrpl.models.amounts import IssuedCurrencyAmount
from scripts._shared import load_state, wallet_from_seed, submit_tx
from rich import print

def create_trust(wallet, issuer_addr, currency):
    tx = TrustSet(
        account=wallet.classic_address,
        limit_amount=IssuedCurrencyAmount(currency=currency, issuer=issuer_addr, value="1000"),
    )
    submit_tx(tx, wallet)

def main():
    st = load_state()
    issuer_addr = st["issuer"]["address"]
    currency = st["currency"]
    print("[bold]Creating trustlines[/bold]")
    create_trust(wallet_from_seed(st["beneficiary"]["seed"]), issuer_addr, currency)
    create_trust(wallet_from_seed(st["merchant"]["seed"]), issuer_addr, currency)

if __name__ == "__main__":
    main()
