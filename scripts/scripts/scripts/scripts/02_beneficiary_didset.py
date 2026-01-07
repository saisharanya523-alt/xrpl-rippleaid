import json, time
from xrpl.models.transactions import DIDSet
from scripts._shared import load_state, wallet_from_seed, submit_tx, hexify
from rich import print

def main():
    st = load_state()
    b = wallet_from_seed(st["beneficiary"]["seed"])
    payload = {"schema": "rippleaid-v1", "created": int(time.time())}
    tx = DIDSet(
        account=b.classic_address,
        uri=hexify(f"ipfs://rippleaid/{b.classic_address}"),
        data=hexify(json.dumps(payload)),
    )
    print("[bold]Creating DID...[/bold]")
    submit_tx(tx, b)

if __name__ == "__main__":
    main()
