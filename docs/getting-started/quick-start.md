# Quick Start

This guide will help you get started with PROMETRY quickly through practical examples.

## Basic Usage

### 1. Structure Search

Search for protein structures from the PDB database:

```python
from prometry import protein_search

# Search for a specific PDB structure
structure = protein_search.get_structure("1t29")

# Explore the structure
print(f"Structure: {structure.get_id()}")
print(f"Number of chains: {len(structure.get_chains())}")
```

### 2. Calculate Geometric Parameters

Calculate distances, angles, and dihedrals:

```python
from prometry import geometry

# Define atoms for geometric calculation
# Format: residue_name-atom_name
atoms = ["ALA-N", "ALA-CA", "ALA-C", "ALA-O"]

# Calculate dihedral angle (4 atoms)
dihedral = geometry.calculate_dihedral(structure, atoms)

# Calculate angle (3 atoms)
angle = geometry.calculate_angle(structure, atoms[:3])

# Calculate distance (2 atoms)
distance = geometry.calculate_distance(structure, atoms[:2])
```

### 3. Criteria-Based Search

Apply criteria to filter results:

```python
from prometry import criteria_search

# Define search criteria
criteria = {
    "residue": "PRO",  # Only proline residues
    "distance": {"min": 2.0, "max": 4.0},  # Distance range
    "chain": "A"  # Specific chain
}

# Perform search
results = criteria_search.search(structure, criteria)
```

### 4. Generate Dataframes

Create dataframes for analysis:

```python
import pandas as pd
from prometry import dataframe_maker

# Create a dataframe of geometric parameters
df = dataframe_maker.create_geometry_dataframe(
    pdb_code="1t29",
    geometry_type="dihedral",
    atoms=["CA", "C", "N", "CA"]
)

# Display results
print(df.head())

# Save to CSV
df.to_csv("results.csv", index=False)
```

## Web Application Examples

### Structure Visualization

1. Navigate to the [Structure Search](https://prometry.streamlit.app/Structure_Search) page
2. Enter a PDB code (e.g., "1t29")
3. View the 3D structure and explore chains and residues

### Correlation Analysis

1. Go to the [Correlation](https://prometry.streamlit.app/Correlation) page
2. Select geometric parameters (e.g., phi and psi angles for Ramachandran plot)
3. Apply filters and criteria
4. Generate and download the plot

### Contact Maps

1. Visit the [Contact Map](https://prometry.streamlit.app/Contact_Map) page
2. Input PDB structure
3. Set distance thresholds
4. Generate interactive contact maps

## Example: Ramachandran Plot

Create a classic Ramachandran plot:

```python
from prometry import dataframe_maker, plots
import matplotlib.pyplot as plt

# Create dataframe with phi and psi angles
df = dataframe_maker.create_ramachandran_data(
    pdb_code="1t29",
    chain="A"
)

# Create plot
fig, ax = plt.subplots(figsize=(8, 8))
plots.ramachandran_plot(df, ax=ax)
plt.title("Ramachandran Plot - 1T29 Chain A")
plt.savefig("ramachandran.png", dpi=300)
plt.show()
```

## Example: Hydrogen Bond Analysis

Identify potential hydrogen bonds:

```python
from prometry import criteria_search

# Define hydrogen bond criteria
hbond_criteria = {
    "donor": ["N", "O"],  # Donor atoms
    "acceptor": ["O", "N"],  # Acceptor atoms
    "distance": {"min": 2.5, "max": 3.5},  # Typical H-bond distance
    "angle": {"min": 120, "max": 180}  # Angle constraint
}

# Search for hydrogen bonds
hbonds = criteria_search.find_hydrogen_bonds(
    pdb_code="1t29",
    criteria=hbond_criteria
)

print(f"Found {len(hbonds)} potential hydrogen bonds")
```

## Tips for Getting Started

1. **Start Simple**: Begin with basic distance calculations before moving to complex searches
2. **Use Examples**: The web application provides working examples for each feature
3. **Explore Standard Atoms**: Familiarize yourself with [standard amino acid atoms](https://www.imgt.org/IMGTeducation/Aide-memoire/_UK/aminoacids/formuleAA/)
4. **Read Error Messages**: PROMETRY provides helpful error messages when criteria are incorrectly specified
5. **Download Examples**: Use the web app to generate and download example dataframes

## Next Steps

- Explore the [Geometric Search Language](../user-guide/geometric-search.md)
- Learn about [Criteria and Filters](../user-guide/criteria.md)
- Check out [Visualization Options](../user-guide/visualizations.md)
- Review the [API Reference](../api/core.md)
