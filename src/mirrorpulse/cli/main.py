# CLI using Typer (built on Click). If Typer isn't installed, we fallback to argparse.
try:
    import typer
    app = typer.Typer(help="Mirrorpulse unified seed CLI")
except Exception:  # minimal fallback
    import argparse, sys, json
    def _fallback():
        p = argparse.ArgumentParser(description="Mirrorpulse CLI (fallback)")
        sub = p.add_subparsers(dest="cmd")

        runp = sub.add_parser("run", help="Run the seed engine")
        runp.add_argument("--input", required=True, help="Path to input JSON")

        sub.add_parser("info", help="Show package info")

        args = p.parse_args()
        if args.cmd == "run":
            from mirrorpulse.core.seed_engine import run_seed
            with open(args.input, "r", encoding="utf-8") as f:
                data = json.load(f)
            out = run_seed(data)
            print(json.dumps(out, ensure_ascii=False, indent=2))
        elif args.cmd == "info":
            from mirrorpulse.core.seed_engine import get_info
            print(json.dumps(get_info(), ensure_ascii=False, indent=2))
        else:
            p.print_help()

    if __name__ == "__main__":
        _fallback()
else:
    from typing import Optional
    import json
    from mirrorpulse.core.seed_engine import run_seed, get_info

    @app.command()
    def run(input: str):
        """Run the seed engine with an input JSON file."""
        with open(input, "r", encoding="utf-8") as f:
            data = json.load(f)
        out = run_seed(data)
        typer.echo(json.dumps(out, ensure_ascii=False, indent=2))

    @app.command()
    def info():
        """Show package info and ethics anchors."""
        import json as _j
        typer.echo(_j.dumps(get_info(), ensure_ascii=False, indent=2))

    if __name__ == "__main__":
        app()
