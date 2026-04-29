"""
Public API contract for src/portfolio_env.

This .pyi file is the source of truth for what `from portfolio_env import ...`
exposes. Implementation MUST match these signatures exactly. Tests in
tests/contract/test_public_api.py verify this stub against the runtime
package via importlib + inspect.

Stability guarantee: any change to symbols here is a contract change and
requires a spec amendment (Constitution Principle V).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import gymnasium
import numpy as np

# Re-export from feature 001. SMCParams is owned by smc_features' spec; we
# re-export the symbol here so PortfolioEnvConfig stays self-describing and
# downstream code only needs `from portfolio_env import SMCParams`.
from smc_features import SMCParams as SMCParams


# ---------------------------------------------------------------------------
# Configuration dataclasses (frozen)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class RewardConfig:
    """Reward function knobs. See data-model.md §2.1.

    Setting both lambdas to 0 reduces reward to pure log-return (used by
    SC-007 ablation test).
    """
    lambda_mdd: float = 1.0
    lambda_turnover: float = 0.0015


@dataclass(frozen=True)
class PortfolioEnvConfig:
    """Static environment configuration. See data-model.md §2.2.

    `render_mode` follows Gymnasium 0.29+ convention: passed at __init__,
    stored on the env instance, never as a parameter to render().
    """
    data_root: Path
    assets: tuple[str, ...] = ("NVDA", "AMD", "TSM", "MU", "GLD", "TLT")
    include_smc: bool = True
    reward_config: RewardConfig = field(default_factory=RewardConfig)
    position_cap: float = 0.4
    base_slippage_bps: float = 5.0
    initial_nav: float = 1.0
    start_date: date | None = None
    end_date: date | None = None
    smc_params: SMCParams = field(default_factory=SMCParams)
    render_mode: str | None = None  # None or "ansi" (FR-027)


# ---------------------------------------------------------------------------
# Environment class
# ---------------------------------------------------------------------------

class PortfolioEnv(gymnasium.Env):
    """Multi-asset portfolio allocation environment.

    Observation: Box(shape=(63,) or (33,), dtype=float32). See data-model.md §3.
    Action:      Box(shape=(7,), dtype=float32, low=0, high=1). See §4.
    Reward:      log(NAV_t/NAV_{t-1}) - lambda_mdd*drawdown - lambda_turnover*turnover.

    All reset/step return values follow Gymnasium 0.29+ five-tuple convention.
    `metadata = {"render_modes": ["ansi"], "render_fps": 0}`.
    """

    metadata: dict[str, Any]
    observation_space: gymnasium.spaces.Box
    action_space: gymnasium.spaces.Box
    config: PortfolioEnvConfig
    render_mode: str | None

    def __init__(self, config: PortfolioEnvConfig) -> None:
        """Construct env.

        `self.render_mode` is set from `config.render_mode` to comply with
        Gymnasium 0.29+ env_checker (SC-003).
        """
        ...

    def reset(
        self,
        *,
        seed: int | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[np.ndarray, dict[str, Any]]:
        """Reset environment to t=0. See data-model.md §5 for state semantics.

        Args:
            seed: synchronizes 4-layer PRNG (research R1). None means
                non-reproducible run.
            options: reserved for future use (e.g., custom start_date override).

        Returns:
            (observation, info) where info["is_initial_step"] is True.
        """
        ...

    def step(
        self,
        action: np.ndarray,
    ) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
        """Advance one trading day.

        Args:
            action: shape (7,), float32. Will be processed via the FR-014
                pipeline: NaN check (raise), L1 normalize, position cap.

        Returns:
            (observation, reward, terminated, truncated, info) per Gymnasium 0.29+
            convention. truncated is always False (FR-017).
        """
        ...

    def render(self) -> str | None:
        """Render current step.

        Behavior depends on `self.render_mode` (set at __init__):
        - "ansi": returns a one-line text summary (date, NAV, weights, reward
          components).
        - None: returns None (no-op).

        Per Gymnasium 0.29+, this method takes no `mode` parameter — `render_mode`
        is fixed at construction time.
        """
        ...

    def close(self) -> None: ...


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def info_to_json_safe(info: dict[str, Any]) -> dict[str, Any]:
    """Convert numpy arrays/scalars in info dict to JSON-serializable types.

    Round-trip lossless for float64 (FR-026, SC-008). Used by feature 005
    inference service and feature 007 war-room frontend.
    """
    ...


def make_default_env(data_root: Path | str, *, include_smc: bool = True) -> PortfolioEnv:
    """Convenience constructor with sensible defaults for quickstart demos.

    Equivalent to:
        PortfolioEnv(PortfolioEnvConfig(
            data_root=Path(data_root),
            include_smc=include_smc,
        ))
    """
    ...


__all__ = [
    "PortfolioEnv",
    "PortfolioEnvConfig",
    "RewardConfig",
    "SMCParams",
    "info_to_json_safe",
    "make_default_env",
]
