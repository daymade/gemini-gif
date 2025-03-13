# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2025-03-14

### Added
- Command-line entry point in `pyproject.toml` to enable direct usage of `gemini-gif` command
- Improved error handling for API requests
- Better progress visualization during GIF generation

### Fixed
- Fixed command-line tool installation issue
- Resolved dependency conflicts in package configuration

### Changed
- Updated package metadata in `pyproject.toml`
- Improved documentation with bilingual examples

## [0.1.0] - 2025-03-13

### Added
- Initial release of Gemini GIF Generator
- Core functionality to generate animated GIFs using Google's Gemini API
- Command-line interface
- Support for customizing animation subject, style, and frame rate
- Automatic retry logic to ensure multiple frames are generated
- Progress bars for better user experience
- Programmatic API for integration into other projects 