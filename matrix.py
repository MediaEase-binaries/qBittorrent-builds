#!/usr/bin/env python3
import json
from typing import Dict, List, Tuple


def create_matrix() -> Dict:
    distro = {"os_key": "debian-13", "os": "debian", "codename": "trixie"}

    # (qbittorrent_version, libtorrent_version)
    builds: List[Tuple[str, str]] = [
        ("5.2.0", "1.2.20"),
        ("5.2.0", "2.0.12"),
        ("5.1.4", "2.0.11"),
        ("5.1.4", "1.2.20"),
    ]

    matrix = []
    for version, lt_version in builds:
        binary_url = (
            f"https://github.com/userdocs/qbittorrent-nox-static/releases/download/"
            f"release-{version}_v{lt_version}/x86_64-qbittorrent-nox"
        )
        artifact_name = (
            f"krate-qbittorrent-{version}-{distro['os']}-{distro['codename']}-libtorrent-{lt_version}"
        )
        deb_package_name = f"krate-qbittorrent_{version}_lt_{lt_version}-1_amd64.deb"
        install_base = f"/opt/Krate/vendor/qbittorrent-nox_{version}_lt_{lt_version}"

        matrix.append(
            {
                "version": version,
                "os": distro["os_key"],
                "codename": distro["codename"],
                "libtorrent_version": lt_version,
                "binary_url": binary_url,
                "artifact_name": artifact_name,
                "deb_package_name": deb_package_name,
                "install_base": install_base,
                "distro": f"{distro['os']}-{distro['codename']}",
            }
        )

    return {"include": matrix}


if __name__ == "__main__":
    print(json.dumps(create_matrix(), indent=2))
