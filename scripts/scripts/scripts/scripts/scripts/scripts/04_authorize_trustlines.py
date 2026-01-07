from xrpl.models.transactions import TrustSet, TrustSetFlag
from xrpl.models.amounts import IssuedCurrencyAmount
from scripts._shared import load_state, wallet_from_seed, submit_tx
from rich import print

def authorize(issuer_wallet, holder, currency):
    tx = TrustSet(
        account=issuer_wallet.classic_address,
        limit_amount=IssuedCurrencyAmount(currency=currency, issuer=holder, value="0"),
        flags=TrustSetFlag.TF_SET_AUTH,
    )
    submit_tx(tx, issuer_wallet)

def main():
    st = load_state()
    issuer = wallet_from_seed(st["issuer"]["seed"])
    ccy = st["currency"]
    print("[bold]Authorizing verified trustlines[/bold]")
    authorize(issuer, st["beneficiary"]["address"], ccy)
    authorize(issuer, st["merchant"]["address"], ccy)

if __name__ == "__main__":
    main()
