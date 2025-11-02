from __future__ import annotations
import logging
import os
import structlog
from mapigen.config import MapigenConfig


def setup_logging(config: MapigenConfig | None = None) -> None:
    """Initialize structured logging for Mapigen."""
    log_level = (config.log_level if config else "INFO").upper()
    level = getattr(logging, log_level, logging.INFO)
    env = os.getenv("MAPIGEN_ENV", "local").lower()

    use_json = env in ("ci", "docker", "prod", "production") or log_level == "DEBUG"
    renderer = (
        structlog.processors.JSONRenderer()
        if use_json
        else structlog.dev.ConsoleRenderer()
    )

    logging.basicConfig(format="%(message)s", level=level)

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            renderer,
        ],
        wrapper_class=structlog.make_filtering_bound_logger(level),
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    structlog.get_logger("mapigen").info(
        "Logging initialized",
        level=log_level,
        mode="json" if use_json else "console",
        env=env,
    )
