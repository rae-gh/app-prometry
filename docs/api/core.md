# Core API Reference

This section documents the core modules and functions in the PROMETRY application.

## Module Structure

```
app/
├── Home.py                 # Main application entry point
├── code/                   # Core functionality modules
│   ├── header.py          # Header and configuration
│   ├── plots.py           # Plotting functions
│   └── structures.py      # Structure handling
├── shared/                # Shared utilities
│   ├── config.py          # Configuration management
│   ├── dataframe_maker.py # Data generation
│   ├── geo_plotter.py     # Geometry plotting
│   ├── structure_explorer.py  # Structure analysis
│   └── validation_plotsheet.py # Validation tools
└── pages/                 # Application pages
    └── ...
```

## Core Modules

### config.py

Configuration and initialization:

```python
from shared import config

# Initialize application
config.init()

# Access configuration
settings = config.get_settings()
```

**Key Functions:**
- `init()`: Initialize application state
- `get_settings()`: Retrieve current settings
- `update_settings(new_settings)`: Update configuration

### structures.py

Structure handling and parsing:

```python
from code import structures

# Load structure
structure = structures.load_pdb("1t29")

# Get structure information
info = structures.get_structure_info(structure)

# Extract chains
chains = structures.get_chains(structure)
```

**Key Functions:**
- `load_pdb(pdb_code)`: Load PDB structure
- `get_structure_info(structure)`: Extract metadata
- `get_chains(structure)`: List all chains
- `get_residues(chain)`: Get residues in chain
- `get_atoms(residue)`: Get atoms in residue

### dataframe_maker.py

Generate dataframes for analysis:

```python
from shared import dataframe_maker

# Create geometry dataframe
df = dataframe_maker.create_dataframe(
    pdb_codes=["1t29"],
    geometry_definition="CA-CA",
    criteria={"chain": "A"}
)

# Create correlation dataframe
df_corr = dataframe_maker.create_correlation_df(
    pdb_codes=["1t29"],
    geo1="phi",
    geo2="psi"
)
```

**Key Functions:**
- `create_dataframe(pdb_codes, geometry_definition, criteria)`: Generate geometry data
- `create_correlation_df(pdb_codes, geo1, geo2)`: Create correlation data
- `create_contact_map_df(pdb_code, chain, distance_threshold)`: Generate contact map data

**Parameters:**
- `pdb_codes`: List of PDB codes
- `geometry_definition`: String defining atoms (e.g., "CA-CA", "N-CA-C")
- `criteria`: Dictionary of filtering criteria
- `chain`: Chain identifier
- `distance_threshold`: Maximum distance in Ångströms

### plots.py

Plotting and visualization:

```python
from code import plots
import matplotlib.pyplot as plt

# Create Ramachandran plot
fig, ax = plt.subplots()
plots.ramachandran(ax, phi_angles, psi_angles)

# Create distance histogram
plots.distance_histogram(ax, distances)

# Create contact map
plots.contact_map(ax, contact_matrix)
```

**Key Functions:**
- `ramachandran(ax, phi, psi)`: Plot Ramachandran diagram
- `distance_histogram(ax, distances, bins)`: Plot distance distribution
- `contact_map(ax, matrix)`: Plot contact map
- `scatter_with_density(ax, x, y)`: Density scatter plot

### geo_plotter.py

Geometric plotting utilities:

```python
from shared import geo_plotter

# Create interactive plot
fig = geo_plotter.create_interactive_plot(
    data=df,
    x_col="phi",
    y_col="psi",
    color_col="residue"
)

# Add annotations
geo_plotter.add_region_annotations(fig, regions)
```

**Key Functions:**
- `create_interactive_plot(data, x_col, y_col)`: Create Plotly figure
- `add_region_annotations(fig, regions)`: Add labeled regions
- `customize_layout(fig, title, labels)`: Customize appearance

### structure_explorer.py

Structure exploration and analysis:

```python
from shared import structure_explorer

# Explore structure
explorer = structure_explorer.StructureExplorer("1t29")

# Get secondary structure
ss = explorer.get_secondary_structure()

# Calculate distances
distances = explorer.calculate_distances(["CA", "CA"])

# Find neighbors
neighbors = explorer.find_neighbors(residue, distance=5.0)
```

**Key Classes:**

#### StructureExplorer

```python
class StructureExplorer:
    def __init__(self, pdb_code, chain=None):
        """Initialize with PDB code and optional chain."""
        
    def get_secondary_structure(self):
        """Get DSSP secondary structure assignment."""
        
    def calculate_distances(self, atom_pairs):
        """Calculate distances between atom pairs."""
        
    def find_neighbors(self, residue, distance):
        """Find neighboring residues within distance."""
        
    def get_geometry(self, atoms):
        """Calculate geometric parameter for atom set."""
```

### validation_plotsheet.py

Validation and quality assessment:

```python
from shared import validation_plotsheet

# Validate structure
validation = validation_plotsheet.validate_structure(
    structure,
    criteria="engh_huber"
)

# Create validation plot
fig = validation_plotsheet.create_validation_plot(validation)
```

**Key Functions:**
- `validate_structure(structure, criteria)`: Run validation
- `create_validation_plot(validation)`: Visualize results
- `check_bond_lengths(structure)`: Validate bond lengths
- `check_bond_angles(structure)`: Validate bond angles

## Data Structures

### Geometry Definition

```python
GeometryDefinition = {
    "atoms": List[str],      # List of atom specifications
    "type": str,             # "distance", "angle", or "dihedral"
    "criteria": Dict         # Optional filtering criteria
}
```

### Criteria Dictionary

```python
Criteria = {
    "residue": str | List[str],           # Residue type(s)
    "chain": str | List[str],             # Chain ID(s)
    "residue_range": Tuple[int, int],     # Residue number range
    "secondary_structure": str | List[str], # DSSP codes
    "distance": Dict[str, float],         # Distance constraints
    "angle": Dict[str, float],            # Angle constraints
    "resolution": Dict[str, float],       # Resolution requirements
    "b_factor": Dict[str, float]          # B-factor limits
}
```

### Structure Information

```python
StructureInfo = {
    "pdb_code": str,
    "resolution": float,
    "method": str,
    "chains": List[str],
    "num_residues": int,
    "num_atoms": int
}
```

## Utility Functions

### Common Calculations

```python
# Calculate phi angle
phi = calculate_phi(residue, prev_residue)

# Calculate psi angle
psi = calculate_psi(residue, next_residue)

# Calculate distance
dist = calculate_distance(atom1, atom2)

# Calculate angle
angle = calculate_angle(atom1, atom2, atom3)

# Calculate dihedral
dihedral = calculate_dihedral(atom1, atom2, atom3, atom4)
```

### Data Processing

```python
# Filter dataframe
filtered = filter_dataframe(df, criteria)

# Merge dataframes
merged = merge_geometry_data(df1, df2)

# Export data
export_to_csv(df, filename)
export_to_json(df, filename)
```

## Error Handling

Common exceptions:

```python
try:
    structure = load_pdb("invalid")
except PDBNotFoundError:
    print("PDB code not found")
    
try:
    df = create_dataframe([], "CA-CA")
except InvalidGeometryError:
    print("Invalid geometry definition")
    
try:
    result = apply_criteria(structure, invalid_criteria)
except CriteriaError:
    print("Invalid criteria specified")
```

## Examples

### Complete Workflow

```python
from shared import config, dataframe_maker, structure_explorer
from code import plots
import matplotlib.pyplot as plt

# Initialize
config.init()

# Load and explore structure
explorer = structure_explorer.StructureExplorer("1t29", chain="A")
ss = explorer.get_secondary_structure()

# Create dataframe
df = dataframe_maker.create_correlation_df(
    pdb_codes=["1t29"],
    geo1="phi",
    geo2="psi"
)

# Filter by criteria
criteria = {"secondary_structure": "H", "chain": "A"}
df_filtered = df[df["ss"] == "H"]

# Plot
fig, ax = plt.subplots(figsize=(8, 8))
plots.ramachandran(ax, df_filtered["phi"], df_filtered["psi"])
plt.title("Helical Residues - Ramachandran Plot")
plt.savefig("helix_ramachandran.png", dpi=300)
```

## Next Steps

- Review [Code Structure](code-structure.md) for detailed architecture
- Check [User Guide](../user-guide/overview.md) for usage examples
- See [Contributing Guidelines](../contributing/guidelines.md) for development
