# Criteria & Filters

Learn how to apply criteria and filters to refine your protein structure searches and analyses.

## Overview

PROMETRY's criteria system allows you to:

- Filter results by structural properties
- Apply distance constraints
- Restrict to specific residue types
- Define secondary structure requirements
- Set quality thresholds

## Basic Criteria

### Residue Type Filtering

Filter by specific amino acids:

```python
criteria = {
    "residue": "PRO"  # Only proline residues
}

# Multiple residues
criteria = {
    "residue": ["PRO", "GLY", "ALA"]
}

# Exclude residues
criteria = {
    "exclude_residue": ["GLY", "PRO"]
}
```

### Chain Selection

Restrict analysis to specific chains:

```python
criteria = {
    "chain": "A"
}

# Multiple chains
criteria = {
    "chain": ["A", "B"]
}
```

### Residue Range

Specify residue number ranges:

```python
criteria = {
    "residue_range": (10, 50)  # Residues 10-50
}

# Multiple ranges
criteria = {
    "residue_ranges": [(10, 50), (100, 150)]
}
```

## Geometric Criteria

### Distance Constraints

Apply distance filters:

```python
criteria = {
    "distance": {
        "min": 2.0,  # Minimum distance in Ångströms
        "max": 4.0   # Maximum distance in Ångströms
    }
}

# Only minimum
criteria = {
    "distance": {"min": 3.0}
}

# Only maximum
criteria = {
    "distance": {"max": 5.0}
}
```

### Angle Constraints

Filter by angle values:

```python
criteria = {
    "angle": {
        "min": 90,   # Degrees
        "max": 180
    }
}
```

### Dihedral Constraints

Apply dihedral angle criteria:

```python
# Ramachandran regions
criteria = {
    "phi": {"min": -180, "max": 0},    # Alpha helix region
    "psi": {"min": -60, "max": 50}
}

# Specific dihedral ranges
criteria = {
    "dihedral": {"min": -120, "max": -60}
}
```

## Secondary Structure Filters

### By Secondary Structure Type

Filter by secondary structure assignment:

```python
criteria = {
    "secondary_structure": "H"  # Alpha helix
}

# Multiple types
criteria = {
    "secondary_structure": ["H", "G", "I"]  # All helices
}
```

**Common DSSP codes:**
- `H`: Alpha helix
- `G`: 3-10 helix
- `I`: Pi helix
- `E`: Extended strand (beta sheet)
- `B`: Isolated beta-bridge
- `T`: Turn
- `S`: Bend
- `C`: Coil/loop

### Secondary Structure Combinations

```python
# Only structured regions
criteria = {
    "secondary_structure": ["H", "E"]  # Helices and sheets only
}

# Only unstructured
criteria = {
    "secondary_structure": ["C", "T", "S"]  # Loops and turns
}
```

## Quality Criteria

### Resolution

Filter by structure resolution:

```python
criteria = {
    "resolution": {
        "max": 2.0  # Maximum 2.0 Å resolution
    }
}

# High-resolution only
criteria = {
    "resolution": {"max": 1.5}
}
```

### B-factor (Temperature Factor)

Filter by atomic mobility:

```python
criteria = {
    "b_factor": {
        "max": 50  # Well-ordered atoms only
    }
}
```

### Occupancy

Require full occupancy:

```python
criteria = {
    "occupancy": {
        "min": 1.0  # 100% occupancy
    }
}
```

## Combining Criteria

### Multiple Criteria

Combine different criteria types:

```python
criteria = {
    "residue": ["ALA", "VAL", "LEU"],  # Hydrophobic
    "chain": "A",
    "secondary_structure": "H",         # Alpha helix
    "b_factor": {"max": 40},
    "distance": {"min": 3.0, "max": 5.0}
}
```

### Logical Operations

Use AND/OR logic:

```python
# AND (all criteria must be met)
criteria_and = {
    "operator": "AND",
    "conditions": [
        {"residue": "PRO"},
        {"secondary_structure": ["C", "T"]}
    ]
}

# OR (any criteria can be met)
criteria_or = {
    "operator": "OR",
    "conditions": [
        {"residue": "GLY"},
        {"residue": "PRO"}
    ]
}
```

## Application-Specific Criteria

### Hydrogen Bonds

Identify potential hydrogen bonds:

```python
hbond_criteria = {
    "donor_acceptor_distance": {"min": 2.5, "max": 3.5},
    "angle": {"min": 120, "max": 180},
    "donor_atoms": ["N", "O"],
    "acceptor_atoms": ["O", "N"]
}
```

### Salt Bridges

Find ionic interactions:

```python
salt_bridge_criteria = {
    "residue_pairs": [
        (["LYS", "ARG"], ["ASP", "GLU"])  # Positive-negative pairs
    ],
    "distance": {"max": 4.0}
}
```

### Disulfide Bonds

Identify disulfide bridges:

```python
disulfide_criteria = {
    "residue": "CYS",
    "atoms": ["SG", "SG"],
    "distance": {"min": 1.8, "max": 2.2}
}
```

### Contact Maps

Define residue contacts:

```python
contact_criteria = {
    "atoms": ["CA", "CA"],  # Alpha carbon distance
    "distance": {"max": 8.0},
    "exclude_sequential": 4  # Exclude i to i+4 neighbors
}
```

## Validation Criteria

### Ramachandran Validation

Check phi-psi angles against allowed regions:

```python
ramachandran_criteria = {
    "allowed_regions": [
        {"phi": (-180, -90), "psi": (-60, 50)},   # Alpha-R
        {"phi": (-180, -90), "psi": (90, 180)},   # Beta
        {"phi": (45, 90), "psi": (-60, 50)}       # Alpha-L
    ]
}
```

### Engh & Huber Validation

Validate against ideal geometry:

```python
engh_huber_criteria = {
    "bond_length": {
        "CA-C": {"mean": 1.525, "std": 0.021}
    },
    "bond_angle": {
        "N-CA-C": {"mean": 111.2, "std": 2.8}
    }
}
```

## Example: Complete Criteria Application

```python
from prometry import structure_search, criteria_filter

# Define comprehensive criteria
criteria = {
    # Structure quality
    "resolution": {"max": 2.0},
    "b_factor": {"max": 50},
    
    # Region of interest
    "chain": "A",
    "residue_range": (10, 100),
    
    # Residue selection
    "exclude_residue": ["GLY", "PRO"],
    "secondary_structure": "H",
    
    # Geometric constraints
    "distance": {"min": 3.0, "max": 5.0},
    "angle": {"min": 90, "max": 120}
}

# Apply criteria
structure = structure_search.get_structure("1t29")
filtered_results = criteria_filter.apply(structure, criteria)

print(f"Found {len(filtered_results)} results matching criteria")
```

## Performance Tips

1. **Order Matters**: Apply most restrictive criteria first
2. **Pre-filter**: Use chain/residue filters before geometric calculations
3. **Cache Results**: Store intermediate filtered results
4. **Batch Processing**: Apply same criteria to multiple structures efficiently

## Common Pitfalls

### Over-constraining

```python
# TOO RESTRICTIVE - May return no results
criteria = {
    "residue": "ALA",
    "secondary_structure": "H",
    "distance": {"min": 5.0, "max": 5.1},  # Very narrow range
    "angle": {"min": 109, "max": 110}
}
```

### Missing Units

```python
# WRONG - No units specified (assumed)
criteria = {
    "distance": {"min": 2, "max": 4}  # Assumed Ångströms
}

# BETTER - Comment units
criteria = {
    "distance": {"min": 2.0, "max": 4.0}  # Ångströms
}
```

### Incompatible Criteria

```python
# WRONG - Glycine can't be in helix typically
criteria = {
    "residue": "GLY",
    "secondary_structure": "H"  # Unlikely to find results
}
```

## Next Steps

- Explore [Geometric Search](geometric-search.md)
- Learn about [Visualizations](visualizations.md)
- Check the [API Reference](../api/core.md)
