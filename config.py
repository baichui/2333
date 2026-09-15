# -*- coding: utf-8 -*-
"""NoneBot 版配置：读写插件目录下 config.json。"""

from __future__ import annotations

import json
from pathlib import Path

from nonebot import logger

from .data import XIAO_AI_NAME, all_guide_characters

CONFIG_PATH = Path(__file__).resolve().parent / "config.json"

_DEFAULT = {
    "wuwa_deed_chance": 0.3,
    "metric_labels": [],
    "character_weights": {name: (80 if name == XIAO_AI_NAME else 1) for name in all_guide_characters()},
}


def default_config() -> dict:
    import copy

    return copy.deepcopy(_DEFAULT)


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        cfg = default_config()
        try:
            save_config(cfg)
        except Exception as e:  # noqa: BLE001
            logger.warning(f"wuwa_luck: cannot write default config: {e}")
        return cfg
    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        logger.warning(f"wuwa_luck: config.json invalid, using defaults: {e}")
        return default_config()
    if not isinstance(raw, dict):
        return default_config()

    cfg = default_config()
    try:
        cfg["wuwa_deed_chance"] = float(raw.get("wuwa_deed_chance", 0.3))
    except Exception:  # noqa: BLE001
        pass
    labels = raw.get("metric_labels")
    if isinstance(labels, list):
        cfg["metric_labels"] = [str(x).strip() for x in labels if str(x).strip()]
    weights = raw.get("character_weights")
    if isinstance(weights, dict):
        for name in all_guide_characters():
            if name not in weights:
                continue
            try:
                w = float(weights[name])
            except Exception:  # noqa: BLE001
                continue
            cfg["character_weights"][name] = w
    return cfg


def save_config(cfg: dict) -> None:
    CONFIG_PATH.write_text(
        json.dumps(cfg, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def character_weights(cfg: dict | None = None) -> dict[str, float]:
    cfg = cfg if cfg is not None else load_config()
    raw = cfg.get("character_weights") or {}
    out: dict[str, float] = {}
    for name in all_guide_characters():
        if name not in raw:
            w = 80.0 if name == XIAO_AI_NAME else 1.0
        else:
            try:
                w = float(raw[name])
            except Exception:  # noqa: BLE001
                continue
        if w > 0:
            out[name] = w
    return out
