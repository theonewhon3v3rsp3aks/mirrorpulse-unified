# SEED_ENGINE — Integration Guide

Place your previous 'not-ordinary' code here by wiring it through two functions:

```python
def run_seed(payload: dict) -> dict:
    """Main entry point for your logic."""
    ...

def get_info() -> dict:
    """Return static metadata and anchors."""
    ...
```

## Tips
- **Determinism first.** Avoid hidden state; take inputs explicitly and return outputs explicitly.
- **No secrets in repo.** If your payload needs keys, read them from env vars at runtime.
- **Boundaries.** Respect the non-weaponization ETHICS.md.
- **Testing.** Add example payloads in `examples/` and assertions in `tests/`.
