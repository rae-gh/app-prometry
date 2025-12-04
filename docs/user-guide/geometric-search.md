# Geometric Search Language

PROMETRY uses a flexible and intuitive geometric search language to define calculations across protein structures.

## Overview

The geometric search language allows you to specify:

- Which atoms to measure
- What geometric parameters to calculate
- How to apply criteria and filters

## Basic Syntax

### Atom Specification

Atoms are specified using the format: `RESIDUE-ATOM`

**Examples:**
```
ALA-CA    # Alanine alpha carbon
PRO-N     # Proline backbone nitrogen
GLY-O     # Glycine carbonyl oxygen
LEU-CD1   # Leucine delta carbon 1
```

### Geometric Parameter Types

#### Distance (2 atoms)
```python
atoms = ["ALA-CA", "ALA-C"]
# Calculates distance between alpha carbon and carbonyl carbon
```

#### Angle (3 atoms)
```python
atoms = ["ALA-N", "ALA-CA", "ALA-C"]
# Calculates N-CA-C bond angle
```

#### Dihedral (4 atoms)
```python
atoms = ["ALA-N", "ALA-CA", "ALA-C", "ALA-O"]
# Calculates dihedral angle
```

## Wildcard Notation

Use wildcards to search across all residue types:

```python
# Any residue's CA-C distance
atoms = ["*-CA", "*-C"]

# Specific atom across all residues
atoms = ["*-N"]

# Mix specific and wildcard
atoms = ["PRO-CA", "*-CA"]  # Distance from proline CA to any CA
```

## Sequential Residue References

Reference consecutive residues using offsets:

```python
# Current and next residue
atoms = ["*-C", "*+1-N"]  # C to next N (peptide bond)

# Previous residue
atoms = ["*-1-C", "*-N"]  # Previous C to current N

# Multiple offsets
atoms = ["*-1-CA", "*-CA", "*+1-CA"]  # Three consecutive alpha carbons
```

## Common Geometric Parameters

### Backbone Angles

**Phi (φ) Angle**
```python
atoms = ["*-1-C", "*-N", "*-CA", "*-C"]
```

**Psi (ψ) Angle**
```python
atoms = ["*-N", "*-CA", "*-C", "*+1-N"]
```

**Omega (ω) Angle**
```python
atoms = ["*-CA", "*-C", "*+1-N", "*+1-CA"]
```

### Sidechain Angles

**Chi1 Angle (varies by residue)**
```python
# For most residues
atoms = ["*-N", "*-CA", "*-CB", "*-CG"]
```

### Distances

**CA-CA Distance**
```python
atoms = ["*-CA", "*-CA"]
```

**Hydrogen Bond Distance (potential)**
```python
atoms = ["*-N", "*-O"]  # N-H...O=C
```

**Disulfide Bond**
```python
atoms = ["CYS-SG", "CYS-SG"]
```

## Special Cases

### Proline

Proline has a unique cyclic structure:

```python
# Proline-specific geometry
atoms = ["PRO-N", "PRO-CA", "PRO-CB", "PRO-CG"]
```

### Glycine

Glycine lacks a beta carbon:

```python
# Glycine only has backbone atoms
atoms = ["GLY-N", "GLY-CA", "GLY-C"]
```

### Aromatic Residues

Aromatic residues (PHE, TYR, TRP, HIS) have ring atoms:

```python
# Phenylalanine ring
atoms = ["PHE-CG", "PHE-CD1", "PHE-CE1", "PHE-CZ"]
```

## Advanced Usage

### Chain-Specific Searches

```python
# Specify chain in criteria
criteria = {
    "chain": "A",
    "atoms": ["*-CA", "*-C"]
}
```

### Range-Based Searches

```python
# Search within residue range
criteria = {
    "residue_range": (10, 50),
    "atoms": ["*-N", "*-CA", "*-C"]
}
```

### Multiple Geometry Calculations

```python
# Calculate multiple parameters simultaneously
geometries = [
    ["*-1-C", "*-N", "*-CA", "*-C"],  # Phi
    ["*-N", "*-CA", "*-C", "*+1-N"],  # Psi
    ["*-CA", "*-C"]                    # CA-C distance
]
```

## Validation

PROMETRY validates your geometric definitions:

- **Atom count**: Must match geometry type (2, 3, or 4 atoms)
- **Atom names**: Must be valid PDB atom names
- **Residue names**: Must be valid three-letter codes
- **Sequential consistency**: Offset references must be valid

**Example Errors:**
```python
# ERROR: Wrong number of atoms for angle
atoms = ["ALA-CA", "ALA-C"]  # Need 3 atoms for angle

# ERROR: Invalid atom name
atoms = ["ALA-CX", "ALA-C"]  # CX is not a standard atom

# ERROR: Invalid residue code
atoms = ["ALX-CA", "ALX-C"]  # ALX is not valid
```

## Best Practices

1. **Be Specific**: Use explicit residue names when possible for clarity
2. **Comment Your Code**: Document what each geometric parameter represents
3. **Validate First**: Test on small structures before large-scale analysis
4. **Use Standards**: Follow IUPAC/PDB nomenclature
5. **Check Literature**: Verify atom names for unusual residues

## Examples Gallery

### Ramachandran Plot
```python
phi = ["*-1-C", "*-N", "*-CA", "*-C"]
psi = ["*-N", "*-CA", "*-C", "*+1-N"]
```

### Beta Sheet Geometry
```python
# CA-CA distance between strands
ca_distance = ["*-CA", "*-CA"]
# Apply distance criteria for ~4.8 Å
```

### Alpha Helix Parameters
```python
# i to i+4 hydrogen bond
hbond = ["*-N", "*+4-O"]
```

### Disulfide Bridge
```python
# Cysteine sulfur-sulfur distance
ss_bond = ["CYS-SG", "CYS-SG"]
```

## Next Steps

- Learn about [Criteria & Filters](criteria.md)
- Explore [Structure Search](structure-search.md)
- Check [API Reference](../api/core.md)
