# User Guide Overview

Welcome to the PROMETRY user guide. This section provides comprehensive documentation on how to use PROMETRY for protein structure analysis.

## What is PROMETRY?

PROMETRY is a Python library and web application designed to:

- Calculate geometric parameters of protein structures (distances, angles, dihedrals)
- Perform criteria-based searches across protein structures
- Generate publication-quality visualizations
- Create dataframes for further analysis or machine learning applications

## Core Concepts

### Geometric Parameters

PROMETRY calculates three types of geometric parameters:

1. **Distances**: Between 2 atoms (in Ångströms)
2. **Angles**: Formed by 3 atoms (in degrees)
3. **Dihedrals**: Formed by 4 atoms (in degrees)

### Atom Nomenclature

PROMETRY uses standard protein atom nomenclature:

- **Format**: `RESIDUE-ATOM` (e.g., `ALA-CA`, `PRO-N`)
- **Residues**: Three-letter codes for the 20 standard amino acids
- **Atoms**: Standard IUPAC/PDB atom names

Common backbone atoms:
- `N`: Backbone nitrogen
- `CA`: Alpha carbon
- `C`: Carbonyl carbon
- `O`: Carbonyl oxygen

### Criteria System

PROMETRY's criteria system allows you to:

- Filter by residue type
- Apply distance constraints
- Restrict to specific chains
- Define secondary structure requirements
- Specify resolution requirements

## Application Structure

The PROMETRY web application is organized into pages:

### 1. Structure Search
Search and visualize protein structures from the PDB database. Explore chains, residues, and atomic details.

### 2. Correlation
Generate correlation plots between geometric parameters. Create Ramachandran plots, angle-distance correlations, and more.

### 3. Contact Map
Visualize residue-residue contacts and interactions within protein structures.

### 4. 3D Space
Interactive 3D visualization of protein structures and geometric parameters.

### 5. Validation
Validate protein structures against geometric criteria and known structural preferences.

### 6. Criteria
Define and test custom criteria for structure searches.

### 7. Citing
Information on how to properly cite PROMETRY in publications.

### 8. Help
Detailed help documentation and examples.

## Common Use Cases

### Structural Analysis
- Analyze backbone and sidechain conformations
- Calculate inter-atomic distances
- Identify unusual geometric features

### Contact Analysis
- Generate contact maps
- Identify nearest neighbors
- Analyze residue-residue interactions

### Hydrogen Bond Detection
- Find potential hydrogen bonds
- Analyze H-bond networks
- Compare H-bonding patterns

### Quality Assessment
- Validate structure geometry
- Check against Engh & Huber parameters
- Identify structural anomalies

### Data Generation
- Create training datasets for machine learning
- Generate feature matrices
- Export data for external analysis

## Workflow Example

A typical PROMETRY workflow:

1. **Select Structure**: Choose PDB code or upload structure
2. **Define Geometry**: Specify atoms and geometric parameter type
3. **Apply Criteria**: Set filters and constraints
4. **Generate Data**: Create dataframe with results
5. **Visualize**: Plot results interactively
6. **Export**: Download data and figures

## Data Output

PROMETRY generates structured data in multiple formats:

- **CSV**: For spreadsheet analysis
- **JSON**: For programmatic access
- **PNG/SVG**: For publication-quality figures
- **Interactive HTML**: For web-based exploration

## Performance Considerations

### Web Application
- Optimized for structures up to ~1000 residues
- Large-scale analyses may time out
- Download data for local processing of large datasets

### Library Usage
- No size limitations when used as a Python library
- Parallel processing available for batch operations
- Memory-efficient streaming for large PDB files

## Best Practices

1. **Start Simple**: Begin with single structures before batch processing
2. **Validate Criteria**: Test criteria on known structures first
3. **Document Parameters**: Keep records of geometric definitions and criteria
4. **Check Units**: Distances in Ångströms, angles in degrees
5. **Cite Properly**: Follow citation guidelines when publishing

## Next Steps

Explore specific features in detail:

- [Geometric Search Language](geometric-search.md)
- [Structure Search](structure-search.md)
- [Criteria & Filters](criteria.md)
- [Visualizations](visualizations.md)
