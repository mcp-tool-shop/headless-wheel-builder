"""Headless Wheel Builder - Universal Python wheel builder for CI/CD pipelines."""

from headless_wheel_builder.core.builder import BuildResult, build_wheel
from headless_wheel_builder.core.source import ResolvedSource, SourceSpec, SourceType

__version__ = "0.2.0"

__all__ = [
    "__version__",
    "build_wheel",
    "BuildResult",
    "SourceSpec",
    "SourceType",
    "ResolvedSource",
]


# Lazy import for GitHub module to avoid import overhead when not needed
def __getattr__(name: str):
    """Lazy import GitHub module."""
    if name == "github":
        from headless_wheel_builder import github

        return github
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
