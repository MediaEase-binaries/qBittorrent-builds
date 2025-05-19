#!/usr/bin/env python3
import json
from typing import Dict, List

def create_matrix() -> Dict:
    # Define the supported distributions and their configurations
    SUPPORTED_DISTROS = {
        # Older distributions with libtorrent 1.2 only
        "debian-11": {
            "versions": ["4.6.7", "5.0.1", "5.0.2", "5.0.3", "5.0.4"],
            "libtorrent_series": ["1.2"],
            "os": "debian",
            "codename": "bullseye",
            "artifact_name": "qbittorrent-nox-{version}-{os}-{codename}-libtorrent-{libtorrent_version}",
            "deb_package_name": "qbittorrent-nox-{version}_lt_{libtorrent_version}-1build1_{os}_{architecture}.deb",
            "install_base": "/opt/MediaEase/binaries/installed/qbittorrent_{version}_lt_{libtorrent_version}"
        },
        "ubuntu-22.04": {
            "versions": ["4.6.7", "5.0.1", "5.0.2", "5.0.3", "5.0.4"],
            "libtorrent_series": ["1.2"],
            "os": "ubuntu",
            "codename": "jammy",
            "artifact_name": "qbittorrent-nox-{version}-{os}-{codename}-libtorrent-{libtorrent_version}",
            "deb_package_name": "qbittorrent-nox-{version}_lt_{libtorrent_version}-1build1_{os}_{architecture}.deb",
            "install_base": "/opt/MediaEase/binaries/installed/qbittorrent_{version}_lt_{libtorrent_version}"
        },
        # Newer distributions with both libtorrent versions possible
        "debian-12": {
            "versions": ["5.0.3", "5.0.4", "5.0.5", "5.1.0"],
            "libtorrent_series": ["1.2", "2.0"],
            "os": "debian",
            "codename": "bookworm",
            "artifact_name": "qbittorrent-nox-{version}-{os}-{codename}-libtorrent-{libtorrent_version}",
            "deb_package_name": "qbittorrent-nox-{version}_lt_{libtorrent_version}-1build1_{os}_{architecture}.deb",
            "install_base": "/opt/MediaEase/binaries/installed/qbittorrent_{version}_lt_{libtorrent_version}"
        },
        "ubuntu-24.04": {
            "versions": ["5.0.3", "5.0.4", "5.0.5", "5.1.0"],
            "libtorrent_series": ["1.2", "2.0"],
            "os": "ubuntu",
            "codename": "noble",
            "artifact_name": "qbittorrent-nox-{version}-{os}-{codename}-libtorrent-{libtorrent_version}",
            "deb_package_name": "qbittorrent-nox-{version}_lt_{libtorrent_version}-1build1_{os}_{architecture}.deb",
            "install_base": "/opt/MediaEase/binaries/installed/qbittorrent_{version}_lt_{libtorrent_version}"
        }
    }

    # Define version-specific configurations
    VERSION_CONFIGS = {
        "4.6.7": {
            "stability": "oldstable",
            "libtorrent_versions": {
                "1.2": "1.2.19"
            }
        },
        "5.0.1": {
            "stability": "stable",
            "libtorrent_versions": {
                "1.2": "1.2.19",
                "2.0": "2.0.10"
            }
        },
        "5.0.2": {
            "stability": "stable",
            "libtorrent_versions": {
                "1.2": "1.2.19",
                "2.0": "2.0.10"
            }
        },
        "5.0.3": {
            "stability": "stable",
            "libtorrent_versions": {
                "1.2": "1.2.20",
                "2.0": "2.0.11"
            }
        },
        "5.0.4": {
            "stability": "stable",
            "libtorrent_versions": {
                "1.2": "1.2.20",
                "2.0": "2.0.11"
            }
        },
        "5.0.5": {
            "stability": "stable",
            "libtorrent_versions": {
                "1.2": "1.2.20",
                "2.0": "2.0.11"
            }
        },
        "5.1.0": {
            "stability": "next",
            "libtorrent_versions": {
                "2.0": "2.0.11"
            }
        }
    }

    matrix = []

    # Generate matrix entries
    for os_key, config in SUPPORTED_DISTROS.items():
        for version in config["versions"]:
            if version in VERSION_CONFIGS:
                # For each supported libtorrent series in this distribution
                for lt_series in config["libtorrent_series"]:
                    if version == "5.1.0" and lt_series == "1.2":
                        continue
                        
                    if lt_series in VERSION_CONFIGS[version]["libtorrent_versions"]:
                        lt_version = VERSION_CONFIGS[version]["libtorrent_versions"][lt_series]
                        binary_url = f"https://github.com/userdocs/qbittorrent-nox-static/releases/download/release-{version}_v{lt_version}/x86_64-qbittorrent-nox"
                        
                        artifact_name = config["artifact_name"].format(
                            version=version,
                            os=config["os"],
                            codename=config["codename"],
                            libtorrent_version=lt_version
                        )

                        deb_package_name = config["deb_package_name"].format(
                            version=version,
                            os=config["os"],
                            codename=config["codename"],
                            libtorrent_version=lt_version,
                            architecture="amd64"
                        )

                        install_base = config["install_base"].format(
                            version=version,
                            libtorrent_version=lt_version
                        )
                        
                        entry = {
                            "version": version,
                            "stability": VERSION_CONFIGS[version]["stability"],
                            "os": os_key,
                            "libtorrent_version": lt_version,
                            "binary_url": binary_url,
                            "artifact_name": artifact_name,
                            "deb_package_name": deb_package_name,
                            "install_base": install_base,
                            "distro": config["os"] + "-" + config["codename"]
                        }
                        matrix.append(entry)

    return {"include": matrix}

if __name__ == "__main__":
    print(json.dumps(create_matrix(), indent=2)) 
