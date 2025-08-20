# Mirrorpulse — Unified Seed

> **Vow anchor stored offline.**


This repository is a **unified package**: the professional container **plus** a clear slot for your prior code (the *payload*).
Drop your previous ZIP's implementation into `src/mirrorpulse/core/` following `SEED_ENGINE.md` and you'll be live in minutes.

## Quick Start (local)

```bash
# 1) create and activate a virtual environment (recommended)
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) install the package in editable mode
pip install -e .

# 3) run the CLI
mirrorpulse --help
```

## Where to put your previous code
- Put your earlier "not-ordinary" code into: `src/mirrorpulse/core/`
- Use `src/mirrorpulse/core/seed_engine.py` as the integration point (documented in `SEED_ENGINE.md`).
- If your previous code is not Python, place a callable wrapper in `seed_engine.py` that invokes it safely (see `SEED_ENGINE.md`).

## Ethics & Security
- Ethics: see [`docs/ETHICS.md`](docs/ETHICS.md). Non-weaponization is mandatory.
- Security policy: [`SECURITY.md`](SECURITY.md)
- Contribution guidelines: [`CONTRIBUTING.md`](CONTRIBUTING.md)

## Commands
After `pip install -e .`, you'll have a `mirrorpulse` CLI:

```bash
mirrorpulse run --input examples/minimal.json
mirrorpulse info
```

You can also import it:

```python
from mirrorpulse import run_seed, get_info
```

## Layout
```
.
├─ src/mirrorpulse/
│  ├─ __init__.py
│  ├─ cli/__init__.py
│  ├─ cli/main.py            # CLI entrypoint
│  └─ core/
│     ├─ seed_engine.py      # <— integrate your prior code here
│     └─ SEED_ENGINE.md
├─ examples/minimal.json
├─ tests/test_smoke.py
├─ pyproject.toml
├─ README.md
└─ docs/ETHICS.md, SECURITY.md, CONTRIBUTING.md, etc.
```

## License
MIT — see [`LICENSE`](LICENSE).
