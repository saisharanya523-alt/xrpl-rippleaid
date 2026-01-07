from xrpl.wallet import generate_faucet_wallet
from rich import print
from scripts._shared import client, save_state

def main():
    c = client()
    print("[bold]Funding 3 Testnet wallets...[/bold]")
    issuer = generate_faucet_wallet(c)
    beneficiary = generate_faucet_wallet(c)
    merchant = generate_faucet_wallet(c)

    data = {
        "issuer": {"address": issuer.classic_address, "seed": issuer.seed},
        "beneficiary": {"address": beneficiary.classic_address, "seed": beneficiary.seed},
        "merchant": {"address": merchant.classic_address, "seed": merchant.seed},
        "currency": "FOOD",
        "voucher_issue_amount": "50",
        "purchase_amount": "10",
        "xrp_settlement": 1.0,
    }
    save_state(data)
    print("[yellow]state.local.json saved (DO NOT COMMIT)[/yellow]")
    print(data)

if __name__ == "__main__":
    main()
