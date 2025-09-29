#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consolida cenários e revisões em um único Excel."""
from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "consolidated" / "exports" / "test_scenarios.xlsx"

def iter_scenarios(root: Path):
    for y in root.glob("modules/*/scenarios/*/scenario.yaml"):
        yield y

def load_yaml(p: Path):
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def latest_revision(revs: list[dict]):
    if not revs:
        return None
    # Assume entries chronological; take last
    return revs[-1]

def main():
    rows = []
    for scen_path in iter_scenarios(ROOT):
        scen = load_yaml(scen_path)
        module = scen.get("metadata", {}).get("module", "")
        scen_id = scen.get("metadata", {}).get("id", "")
        title = scen.get("metadata", {}).get("title", "")
        labels = scen.get("metadata", {}).get("labels", [])
        risk = scen.get("metadata", {}).get("risk", "")
        endpoints = scen.get("metadata", {}).get("endpoints", [])
        revs_path = scen_path.with_name("revisions.yaml")
        version = release = status = date = ""
        if revs_path.exists():
            revs = load_yaml(revs_path) or []
            last = latest_revision(revs)
            if last:
                date = last.get("date", "")
                version = last.get("version", "")
                release = last.get("release", "")
                status = last.get("status", "")
        rows.append({
            "module": module,
            "scenario_id": scen_id,
            "title": title,
            "labels": ", ".join(labels) if isinstance(labels, list) else labels,
            "risk": risk,
            "endpoints": ", ".join(endpoints) if isinstance(endpoints, list) else endpoints,
            "version": version,
            "release": release,
            "status": status,
            "last_updated": date,
            "path": str(scen_path.relative_to(ROOT)),
        })
    df = pd.DataFrame(rows).sort_values(["module","scenario_id"]).reset_index(drop=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(OUT, engine="xlsxwriter") as xw:
        df.to_excel(xw, index=False, sheet_name="scenarios")
    print(f"Excel gerado: {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
