# Installation

## Requirements

- **QGIS ≥ 3.10** (a current LTR version is recommended)
- **GRASS** and the **GRASS Provider** must be installed and enabled in QGIS (Settings → Manage/Install Plugins)

!!! warning "Work locally, not on a network drive/cloud"
    Input and output data should be **local**, not on a network drive or cloud storage (OneDrive, etc.). With synced folders, (temporary) output files can sometimes fail to be written or read, leading to hard-to-diagnose errors.

## Two versions

| Version | Description |
| --- | --- |
| **TBk Plugin** (current) | Latest version, updated continuously. Includes all features, including the regionwise computation. [Download ↗](https://nextcloud.bfh.science/index.php/s/Fmmr55zssrLAnfH) |
| **TBk Core** (stable) | Proven version with all features up to October 2025, tested with QGIS 3.16–3.44. **No longer under active development** and does **not** include the regionwise computation. Can be installed **in parallel** with the current version. [Download ↗](https://nextcloud.bfh.science/index.php/s/Pw46A2GCqMDt2Gn) |

## Installing as a ZIP file

The plugin is installed as a ZIP file:

1. In QGIS: **Plugins → Manage and Install Plugins…**
2. **Install from ZIP** tab
3. Select the downloaded `.zip` file and install

After installation, the TBk tools appear in the **Processing Toolbox** under the **TBk** provider, organized into groups a–f (see [Tools](tools.md)).

Since TBk Plugin and TBk Core can be installed in parallel, both providers may appear in the toolbox at the same time — distinguishable by the group/provider name.
