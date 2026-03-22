"""Package provides utility modules and functions to support the main application.

These utilities include functions for downloading, file management, URL handling,
progress tracking, and more.

Modules:
    - config: Constants and settings used across the project.
    - crawler_utils: Asynchronous utilities for crawling manga chapters and metadata.
    - download_utils: Functions for handling downloads.
    - file_utils: Utilities for managing file operations.
    - format_utils: Utilities for processing and formatting strings or URLs.
    - general_utils: Miscellaneous utility functions.
    - pdf_generator: Tools for generating PDF files from manga chapters.
    - progress_utils: Tools for progress tracking and reporting.

This package is designed to be reusable and modular, allowing its components to be
easily imported and used across different parts of the application.
"""

# src/__init__.py

from .version import __author__, __title__, __version__, version_info

__all__ = [
    "__author__",
    "__title__",
    "__version__",
    "config",
    "crawler_utils",
    "download_utils",
    "file_utils",
    "format_utils",
    "general_utils",
    "pdf_generator",
    "progress_utils",
    "version_info",
]
