import json, os
from dataclasses import dataclass
from dotenv import load_dotenv
from rich import print
from xrpl.clients import JsonRpcClient
from xrpl.transaction import submit_and_wait
from xrpl.wallet import Wallet
from xrpl.utils import str_to_hex, xrp_to_drops

STATE_PATH = "state.local.json"

@dataclass
class Cfg:
    json_rpc_url: str
    explorer_tx_base: str

def cfg() -> Cfg:
    load_dotenv()
    return Cfg(
        json_rpc_url=os.getenv("JSON_RPC_URL", "https://s.altnet.rippletest.net:51234/"),
        explorer_tx_base=os.getenv("EXPLORER_TX_BASE", "https://testnet.xrpl.org/transactions/"),
    )

def client() -> JsonRpcClient:
    return JsonRpcClient(cfg().json_rpc_url)

def load_state(path=STATE_PATH):
    with open(path, "r") as f:
        return json.load(f)

def save_state(data, path=STATE_PATH):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def wallet_from_seed(seed): return Wallet.from_seed(seed)
def hexify(s): return str_to_hex(s)
def drops(xrp): return xrp_to_drops(xrp)

def submit_tx(tx, wallet):
    c = client()
    resp = submit_and_wait(tx, c, wallet)
    h = resp.result.get("hash") or resp.result.get("tx_json", {}).get("hash")
    link = cfg().explorer_tx_base.rstrip("/") + "/" + h
    print(f"[green]Validated:[/green] {h}\n{link}")
    return h
