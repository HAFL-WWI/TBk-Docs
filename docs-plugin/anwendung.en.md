# Usage

## Where do I find the tools?

After installation, all TBk tools appear in QGIS's **Processing Toolbox** under the **TBk** provider. There they are organized into six (plus two internal) groups, also sorted alphabetically so they appear in a typical processing order:

- **a Main Workflows** — ready-made end-to-end workflows
- **b Preprocessing** — prepare input data
- **c Stand Delineation (Core)** — core algorithm for stand delineation
- **d Postprocessing Geometry** — geometry post-processing
- **e Postprocessing Attributes** — compute/add attributes
- **f Additional Modules** — optional add-on modules

Details on the individual tools: see [Tools](tools.md). Typical order/interaction of the tools: see [Workflows](workflows.md).

## Basic operation

Every TBk tool is a regular QGIS Processing algorithm:

1. Double-click the tool in the toolbox (opens the parameter dialog)
2. Set the input layers/parameters
3. If needed, expand **Advanced Parameters** (usually have sensible defaults, generally no need to change them)
4. **Run**

Since the tools are regular Processing algorithms, they can also be used from the **QGIS Python console** (`processing.run(...)`) or in the **Model Designer** — e.g. to assemble your own variants of the standard workflows.

## Output location

Most tools require an **output folder** to be specified — if it isn't set, the result ends up in a temporary folder and is hard to find again.

The main workflow ([Generate BK](workflows.md)) creates a timestamped subfolder by default:

```
{output folder}/{YYYYMMDD-HHMM}/
├── TBk_Bestandeskarte.gpkg      Result: the stand map
├── TBk_Project.qgz              QGIS project for visualization
├── bk_process/                  Intermediate results
└── dg_layers/                   Crown coverage raster layers
```

Creating the timestamped subfolder can be disabled via the advanced parameter **"Create subfolder with timestamp"**.

## Cleaning up temporary data

The **"Delete temporary files and fields"** checkbox is enabled by default and deletes intermediate results/fields after a successful run. For debugging, it can be helpful to disable it in order to inspect intermediate steps.

## Configuration via TOML files (advanced)

All parameters of a tool can alternatively be set via a **`.toml` configuration file** (parameter `config_file`). Values from the file override any values set in the dialog. This is useful for making runs reproducible or for controlling batch processing outside the QGIS UI. The structure of the TOML file directly matches the tools' parameter names — see [Datasets](datensaetze.md) for the most important keys.
