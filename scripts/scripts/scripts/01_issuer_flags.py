from xrpl.models.transactions import AccountSet, AccountSetAsfFlag
from scripts._shared import load_state, wallet_from_seed, submit_tx
from rich import print

def main():
    st = load_state()
    issuer = wallet_from_seed(st["issuer"]["seed"])

    print("[bold]Enable RequireAuth + DefaultRipple[/bold]")
    tx1 = AccountSet(account=issuer.classic_address, set_flag=AccountSetAsfFlag.ASF_REQUIRE_AUTH)
    submit_tx(tx1, issuer)
    tx2 = AccountSet(account=issuer.classic_address, set_flag=AccountSetAsfFlag.ASF_DEFAULT_RIPPLE)
    submit_tx(tx2, issuer)

if __name__ == "__main__":
    main()
