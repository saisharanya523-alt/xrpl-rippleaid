# RippleAid — Verified Aid Vouchers on XRPL (DID + Authorized Vouchers + Payments)

**Tagline:** Fast, verifiable aid distribution using beneficiary DIDs + issuer-authorized voucher tokens on the XRP Ledger.

## Problem (Commercial + Realistic)
In disasters, aid distribution breaks due to:
- **Duplicate / fake claims** (hard to verify recipients quickly)
- **Cash leakage & theft risk**
- **Low transparency** (donors/NGOs can’t easily prove where value went)
- **Merchant acceptance friction** (no easy settlement & audit trail)

## Who adopts and why (Stakeholders)
### 1) Aid Provider (NGO / agency) — *Primary adopter*
Value:
- Fraud reduction via **issuer-authorized eligibility** (only verified wallets can hold vouchers)
- Instant distribution (no printing/logistics)
- Auditable trail (voucher issuance → spend → redemption → settlement)

### 2) Aid Receiver (Beneficiary)
Value:
- Receives vouchers safely on phone (or assisted onboarding by field staff)
- No personal data on-chain
- Simple “show QR / send payment” experience (MVP uses scripts; UI can be added)

### 3) Merchants
Value:
- Accept vouchers like “digital coupons”
- Redeem back to issuer and receive settlement (XRP in MVP; RLUSD-ready later)
- Clear records for accounting

## What this MVP builds (End-to-end demo)
1) **Beneficiary DID**
- Beneficiary creates a DID on XRPL (no PII; just an on-ledger DID anchor).

2) **Voucher token (Issued Currency)**
- NGO issues `FOOD` vouchers as an on-ledger issued asset.
- Beneficiary + Merchant create trustlines to hold `FOOD`.

3) **Eligibility enforcement (Authorized Trust Lines)**
- Issuer enables RequireAuth.
- Issuer authorizes trustlines for verified beneficiary + merchant.

4) **Closed-loop redemption**
- Issuer sends 50 `FOOD` to beneficiary.
- Beneficiary pays merchant 10 `FOOD`.
- Merchant redeems 10 `FOOD` back to issuer.
- Issuer settles merchant in XRP.

## XRPL features used (for Devpost)
- **DIDSet**: beneficiary identity anchor (no personal data on-chain)
- **Issued Currencies + Trustlines**: `FOOD` voucher tokens (TrustSet + Payment)
- **Authorized Trust Lines**: issuer enforces eligibility before vouchers can be held
- **Payments**: voucher distribution/spend + XRP settlement

## Repo layout
- `scripts/` — guaranteed-working demo scripts
- `demo.md` — exact commands to run the demo
- `state.local.json` — created locally by script (NOT committed)

## How to run (recommended: GitHub Codespaces)
1. Copy `.env.example` → `.env` and keep defaults.
2. Install deps:
   ```bash
   pip install -r requirements.txt
