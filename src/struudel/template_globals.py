from datetime import UTC, datetime
from typing import Any

from flask import Flask, g

from struudel.config import settings
from struudel.version import COMMIT, VERSION


def init_template_globals(app: Flask) -> None:
    @app.context_processor
    def inject_template_globals() -> dict[str, Any]:
        return {
            "current_user": g.user,
            "app_version": VERSION,
            "app_commit": COMMIT,
            "current_year": datetime.now(UTC).year,
            "retention_days": settings.poll_retention_days,
            "oidc_provider_name": settings.oidc_provider_name,
        }
