# qBittorrent Builds

This repository provides automated build scripts for compiling the qBittorrent BitTorrent client and creating Debian packages (.deb) for multiple Linux distributions. All builds are automated via GitHub Actions and are available in the GitHub Releases section.

## Features

- Automated builds via GitHub Actions
- Debian packages that install qBittorrent in `/opt/MediaEase/binaries/installed/qbittorrent_${VERSION}_lt_${LIBTORRENT_VERSION}`
- Support for multiple Linux distributions:
  - Debian 11 (Bullseye)
  - Debian 12 (Bookworm)
  - Ubuntu 22.04 LTS
  - Ubuntu 24.04 LTS
- Multiple version support with different stability levels:
  - Oldstable (4.6.7)
  - Stable (5.0.3, 5.0.4, 5.0.5)
  - Next (5.1.0)
- Qt5 and Qt6 support
- Automated metadata generation
- Package signing and verification

## Supported Versions & Distributions

| Version    | Stability  | Debian 11 | Debian 12 | Ubuntu 22.04 | Ubuntu 24.04 |
|------------|------------|-----------|-----------|--------------|--------------|
| 5.1.0      | next       |     ✘     |     ✔     |      ✘       |      ✔       |
| 5.0.5      | stable     |     ✔     |     ✔     |      ✔       |      ✔       |
| 5.0.4      | stable     |     ✔     |     ✔     |      ✔       |      ✔       |
| 5.0.3      | stable     |     ✔     |     ✔     |      ✔       |      ✔       |
| 4.6.7      | oldstable  |     ✔     |     ✘     |      ✔       |      ✘       |

## Build Process

The build process is fully automated and includes:
1. Environment setup with all required dependencies
2. Download and compilation of qBittorrent
3. Creation of Debian packages
4. Generation of JSON metadata
5. Package signing and verification
6. Automated release creation

## Available Packages

Packages are available in the GitHub Releases of this repository. Each release includes:
- A `.deb` file installable with `dpkg -i`
- A `.json` file containing package metadata
- Documentation and changelog
- Package signatures

### Package Structure

The Debian package installs qBittorrent in a dedicated directory structure:
- Base installation path: `/opt/MediaEase/binaries/installed/qbittorrent_${VERSION}_lt_${LIBTORRENT_VERSION}`
- Binaries in `/opt/MediaEase/binaries/installed/qbittorrent_${VERSION}_lt_${LIBTORRENT_VERSION}/usr/bin`
- Libraries in `/opt/MediaEase/binaries/installed/qbittorrent_${VERSION}_lt_${LIBTORRENT_VERSION}/usr/lib`
- Documentation in `/opt/MediaEase/binaries/installed/qbittorrent_${VERSION}_lt_${LIBTORRENT_VERSION}/usr/share/doc/qbittorrent`

The package uses Debian alternatives to manage the binaries, making them available in the system PATH.

## Installation

### Manual Installation
1. Download the appropriate .deb package for your distribution from the [GitHub Releases](../../releases)
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

### Automated Installation
The packages can be installed automatically using the JSON metadata and package management tools.

## Build Configuration

The build process is configured through:
- `build.yaml`: GitHub Actions workflow configuration
- `matrix.py`: Build matrix configuration for different versions and distributions

## Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, new features, or improvements.

## Support

For questions, issues, or support, please use the GitHub Issues section of this repository.

## License

This repository is licensed under the terms specified in the LICENSE file.

qBittorrent is distributed under the terms of the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.html) or later. 
