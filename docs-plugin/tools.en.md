# Tools

Overview of all TBk tools in the QGIS Processing Toolbox, organized by the groups as they appear there. Within **c**, **d** and **e**, the core tools are additionally numbered (`1`, `2`, `3`, …) — matching their typical order in the [Generate BK workflow](workflows.md).

## a — Main Workflows

Ready-made end-to-end workflows that automatically run several individual tools in the correct order. In the normal case, it's enough to use one of these two tools directly instead of running the individual steps manually.

| Tool | Description |
| --- | --- |
| **Generate BK** | Main workflow: generates the finished stand map from VHM/MG rasters and a perimeter. Details: see [Workflows](workflows.md). |
| **Generate BK Regionwise** | Like *Generate BK*, but splits the perimeter into sub-regions based on an attribute field, processes them individually and then merges the results back together. This lets stand boundaries be aligned to predefined regions (e.g. logging/access units, ownership boundaries or development boundaries) — the perimeter must already be split into these regions beforehand. Details: [Workflows](workflows.md#variant-generate-bk-regionwise). |

## b — Preprocessing

Prepares raw data into the raster inputs that *Generate BK* needs.

| Tool | Description |
| --- | --- |
| **TBk prepare VHM (and MG)** | Processes the vegetation height model (VHM) and, optionally, the coniferous-proportion raster (mixture degree/MG) into the inputs required by *Generate BK*: `VHM_detail`, `VHM_10m`, `VHM_150cm`, `MG_10m`, `MG_10m_binary`. ⚠️ On scaling the mixture degree (0–10,000 vs. 0–100, deciduous/coniferous direction), see the [caution box in Workflows](workflows.md#phase-1-preprocessing). |

## c — Stand Delineation (Core)

The actual core algorithm: pixel-wise classification based on the vegetation height model, followed by polygonization.

| Tool | Description |
| --- | --- |
| **1 Delineate Stand** | Stand classification based on a vegetation height raster (typically a 10×10m maximum-height raster from LiDAR or stereo aerial image correlation data). Result: raw, classified stand polygons. |
| **2 Simplify and Clean** | Cleans up the raw classification: **unconditionally** eliminates polygons below the minimum area (always merged into the largest neighbour by area, regardless of height similarity) and simplifies the stand boundaries based on the simplification tolerance. |

## d — Postprocessing Geometry

Geometric post-processing of the classified stands.

| Tool | Description |
| --- | --- |
| **3 Merge similar neighbours** | Merges small stands into a neighbouring stand of similar dominant height (hdom) — unlike *Simplify and Clean*, only if the hdom values are similar within the tolerance; dissimilar small stands are left untouched. Iterates until no more candidates qualify. |
| **3b Merge similar neighbours graph-based** | Graph-based alternative to *Merge similar neighbours*: builds a similarity graph (edges between small stands and similar, adjacent neighbours) and dissolves connected components in a single pass. Difference from the iterative approach: a chain of small stands between two similar large stands is merged in one step instead of over several passes. |
| **4 Clip to perimeter and eliminate gaps** | Clips the result to the project perimeter and closes any gaps that result. |

## e — Postprocessing Attributes

Computes and adds the content attributes of the stand map.

| Tool | Description |
| --- | --- |
| **5 Calculate crown coverage** | Calculates the crown coverage (DG) per stand from the 150cm VHM. |
| **6 Add coniferous proportion** | Adds the coniferous proportion (NH, in %) per stand from the mixture-degree raster. |
| **Append stand attributes** | Adds further stand attributes (vegetation zone, forest site) via spatial join. |

## f — Additional Modules

Optional add-on modules, usually applied **after** the main workflow to an already-generated stand map.

| Tool | Description |
| --- | --- |
| **TBk postprocess local density** | Detects zones of different local density (crown-coverage classes) within the stand polygons, e.g. to delineate particularly dense or sparse sub-areas. Configurable percentage thresholds and moving-window radii per class; small holes/slivers are filtered out, optionally smoothed ("buffer smoothing"). |
| **TBk postprocess ddom SD estimate** | Estimates the dominant breast-height diameter (ddom) and, based on it, the development stage (SD/Stade de développement) from hdom, coniferous proportion (NH) and forest site/site quality. |
| **TBk postprocess V estimate** | Estimates the growing stock (volume) from hdom, crown coverage (DG) and coniferous proportion (NH). |
| **TBk postprocess OS Change** | Computes the change in the upper layer between two TBk map states (development of the crown-coverage layer, `dg_layer`). |
| **TBk WIS.2 Web prep export (KML)** | Prepares a stand map for export to WIS.2 Web. |
| **TBk WIS.2 Desktop export (XML)** | Exports a generated stand map for WIS.2 Desktop. |
| **TBk WIS.2 Web import CSV** | Imports data from a WIS.2 Web CSV export. |

!!! note "Not covered in this overview"
    The groups **g Utility** (e.g. project/layout creation, merging multiple stand maps, generic spatial join — including *Tree species from raster*, which despite living in the source code next to the attribute tools is UI-wise grouped under Utility) and **y Legacy** (predecessor tools from before modularization) are not part of this first version of the technical documentation.
