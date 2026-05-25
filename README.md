# qBittorrent Builds

This repository provides build scripts for compiling the qBittorrent BitTorrent client and creating Debian packages (.deb). Packages are produced when the GitHub Actions workflow is run manually; published artifacts appear under **Releases**.

## GitHub Actions

Workflow `.github/workflows/build.yaml` runs **only** on **`workflow_dispatch`**. Pushes to `main` do **not** trigger builds — use **Actions** → run workflow → choose **`all`** or a specific version.

## Features

- Builds via GitHub Actions (manual trigger)
- Debian packages that install qBittorrent in `/opt/Krate/vendor/qbittorrent-nox_${VERSION}_lt_${LIBTORRENT_VERSION}`
- CI uses a **single reference image**; **one `.deb` per matrix row**, intended for recent **Debian and Ubuntu** on **amd64**; packaging follows the static-build approach from **[userdocs/qbittorrent-nox-static](https://github.com/userdocs/qbittorrent-nox-static)**
- Version matrix: **5.2.0** with libtorrent **1.2.20** and **2.0.12**; **5.1.4** with libtorrent **2.0.11** and **1.2.20**
- Automated metadata generation
- Package signing and verification

## Supported Versions

| qBittorrent | libtorrent (Rasterbar) |
| ----------- | ---------------------- |
| 5.2.0       | 1.2.20, 2.0.12         |
| 5.1.4       | 2.0.11, 1.2.20         |

## Build Process

When you start the workflow, the job sequence includes:
1. Environment setup with all required dependencies
2. Download and compilation of qBittorrent
3. Creation of Debian packages
4. Generation of JSON metadata
5. Package signing and verification
6. Create or update the GitHub Release (when the workflow completes successfully)

## Available Packages

Packages are available in the GitHub Releases of this repository. Each release includes:
- A `.deb` file installable with `dpkg -i`
- A `.json` file containing package metadata
- Documentation and changelog
- Package signatures

### Package Structure

The Debian package installs qBittorrent in a dedicated directory structure:
- Base installation path: `/opt/Krate/vendor/qbittorrent-nox_${VERSION}_lt_${LIBTORRENT_VERSION}`
- Binaries in `/opt/Krate/vendor/qbittorrent-nox_${VERSION}_lt_${LIBTORRENT_VERSION}/usr/bin`
- Libraries in `/opt/Krate/vendor/qbittorrent-nox_${VERSION}_lt_${LIBTORRENT_VERSION}/usr/lib`
- Documentation in `/opt/Krate/vendor/qbittorrent-nox_${VERSION}_lt_${LIBTORRENT_VERSION}/usr/share/doc/qbittorrent`

The package uses Debian alternatives to manage the binaries, making them available in the system PATH.

## Installation

### Manual Installation
1. Download the `.deb` matching the qBittorrent / libtorrent pair you need from the [GitHub Releases](../../releases)
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

### Automated Installation
The packages can be installed automatically using the JSON metadata and package management tools.

## Build Configuration

The build process is configured through:
- `build.yaml`: GitHub Actions workflow configuration
- `matrix.py`: Build matrix configuration for upstream versions (single reference OS in CI)

## Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, new features, or improvements.

## Support

For questions, issues, or support, please use the GitHub Issues section of this repository.

## License

This repository is licensed under the terms specified in the LICENSE file.

qBittorrent is distributed under the terms of the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.html) or later. 
