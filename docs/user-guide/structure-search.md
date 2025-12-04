# Structure Search

Learn how to search, retrieve, and explore protein structures using PROMETRY.

## Data Sources

### PDB Database

PROMETRY primarily works with structures from the [Protein Data Bank (PDB)](https://www.rcsb.org/):

```python
from prometry import structure_search

# Retrieve by PDB code
structure = structure_search.get_structure("1t29")
```

### AlphaFold Structures

Support for [AlphaFold](https://alphafold.ebi.ac.uk/) predicted structures:

```python
# AlphaFold structures (if available)
structure = structure_search.get_alphafold_structure("P12345")
```

### Local Files

Load structures from local PDB files:

```python
from Bio.PDB import PDBParser

parser = PDBParser()
structure = parser.get_structure("my_protein", "path/to/structure.pdb")
```

## Structure Hierarchy

PDB structures follow a hierarchical organization:

```
Model
  └── Chain (A, B, C...)
       └── Residue (1, 2, 3... or 1A, 1B...)
            └── Atom (N, CA, C, O...)
```

### Navigating the Hierarchy

```python
# Get all chains
for chain in structure.get_chains():
    print(f"Chain: {chain.id}")
    
    # Get residues in chain
    for residue in chain.get_residues():
        print(f"  Residue: {residue.resname} {residue.id[1]}")
        
        # Get atoms in residue
        for atom in residue.get_atoms():
            print(f"    Atom: {atom.name} at {atom.coord}")
```

## Search Methods

### By PDB Code

The most common search method:

```python
# 4-character PDB code
structure = structure_search.get_structure("1t29")

# Case-insensitive
structure = structure_search.get_structure("1T29")
```

### By Keywords

Search for structures matching specific criteria:

```python
# Search by protein name
results = structure_search.search_by_keyword("hemoglobin")

# Search by organism
results = structure_search.search_by_organism("Homo sapiens")

# Search by method
results = structure_search.search_by_method("X-RAY DIFFRACTION")
```

### Advanced Queries

Use the RCSB PDB search API for complex queries:

```python
# Multiple criteria
results = structure_search.advanced_search({
    "resolution": {"min": 0, "max": 2.0},
    "experimental_method": "X-RAY DIFFRACTION",
    "molecular_weight": {"min": 10000, "max": 50000}
})
```

## Structure Metadata

### Basic Information

```python
# Structure ID
print(structure.id)

# Number of models (usually 1 for X-ray, multiple for NMR)
print(len(structure))

# Chains present
chains = [chain.id for chain in structure.get_chains()]
print(f"Chains: {chains}")
```

### Header Information

```python
from Bio.PDB import PDBParser

parser = PDBParser()
structure = parser.get_structure("1t29", "1t29.pdb")
header = parser.get_header()

# Resolution
print(f"Resolution: {header['resolution']} Å")

# Experimental method
print(f"Method: {header['structure_method']}")

# Deposition date
print(f"Date: {header['deposition_date']}")
```

## Filtering and Selection

### By Chain

```python
# Get specific chain
chain_a = structure[0]["A"]

# Multiple chains
chains = [structure[0][chain_id] for chain_id in ["A", "B"]]
```

### By Residue Range

```python
# Get residues 10-50 from chain A
residues = [res for res in structure[0]["A"] 
            if 10 <= res.id[1] <= 50]
```

### By Residue Type

```python
# Get all proline residues
prolines = [res for res in structure[0]["A"] 
            if res.resname == "PRO"]

# Get all aromatic residues
aromatics = [res for res in structure[0]["A"] 
             if res.resname in ["PHE", "TYR", "TRP"]]
```

### By Atom Type

```python
# Get all alpha carbons
ca_atoms = [atom for atom in structure.get_atoms() 
            if atom.name == "CA"]

# Get backbone atoms
backbone = [atom for atom in structure.get_atoms() 
            if atom.name in ["N", "CA", "C", "O"]]
```

## Quality Filters

### Resolution

```python
# Filter by resolution
def get_high_resolution_structures(max_resolution=2.0):
    # Implementation depends on how you're searching
    return [pdb for pdb in search_results 
            if pdb.resolution <= max_resolution]
```

### R-factor

```python
# Filter by R-factor (crystallographic quality)
def filter_by_rfactor(structures, max_rfactor=0.25):
    return [s for s in structures 
            if s.rfactor <= max_rfactor]
```

## Working with Biological Assemblies

Many PDB structures require biological assembly transformations:

```python
# Get biological assembly (if different from asymmetric unit)
bio_assembly = structure_search.get_biological_assembly("1t29", assembly_id=1)
```

## Handling Missing Data

### Missing Residues

```python
# Check for missing residues
def find_missing_residues(chain):
    residues = list(chain.get_residues())
    missing = []
    
    for i in range(len(residues)-1):
        current = residues[i].id[1]
        next_res = residues[i+1].id[1]
        
        if next_res - current > 1:
            missing.extend(range(current+1, next_res))
    
    return missing
```

### Missing Atoms

```python
# Check if key atoms are present
def has_complete_backbone(residue):
    required = ["N", "CA", "C", "O"]
    present = [atom.name for atom in residue.get_atoms()]
    return all(atom in present for atom in required)
```

## Example: Complete Structure Analysis

```python
from prometry import structure_search

# Get structure
pdb_code = "1t29"
structure = structure_search.get_structure(pdb_code)

# Analyze structure
print(f"Structure: {pdb_code}")
print(f"Models: {len(structure)}")

for model in structure:
    print(f"\nModel {model.id}:")
    
    for chain in model.get_chains():
        residues = list(chain.get_residues())
        print(f"  Chain {chain.id}: {len(residues)} residues")
        
        # Count residue types
        from collections import Counter
        res_types = Counter(res.resname for res in residues)
        print(f"  Most common: {res_types.most_common(3)}")
        
        # Check completeness
        complete = sum(1 for res in residues if has_complete_backbone(res))
        print(f"  Complete residues: {complete}/{len(residues)}")
```

## Web Application Features

The PROMETRY web app provides interactive structure search:

1. **Structure Search Page**: Enter PDB code and visualize
2. **Chain Selection**: Choose specific chains to analyze
3. **Residue Browser**: Navigate through residues interactively
4. **3D Visualization**: Rotate and zoom structure
5. **Metadata Display**: View resolution, method, and other properties

## Best Practices

1. **Validate PDB Codes**: Check that PDB codes are current and valid
2. **Handle Obsolete Entries**: Be prepared for deprecated structures
3. **Check Resolution**: Higher resolution = more reliable atomic positions
4. **Inspect Chains**: Multi-chain complexes may need careful chain selection
5. **Consider Biological Assembly**: Use biological assembly for physiological context
6. **Document Selections**: Keep records of which structures and chains you analyze

## Next Steps

- Learn about [Geometric Search](geometric-search.md)
- Explore [Criteria & Filters](criteria.md)
- Check out [Visualizations](visualizations.md)
