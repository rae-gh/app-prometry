# Code Structure

This document provides an overview of the PROMETRY application architecture and code organization.

## Application Architecture

PROMETRY follows a modular Streamlit application structure:

```
app-prometry/
├── app/                    # Main application directory
│   ├── Home.py            # Entry point
│   ├── code/              # Core functionality
│   ├── shared/            # Shared utilities
│   ├── pages/             # Application pages
│   ├── data/              # Sample data
│   └── static/            # Static assets
├── docs/                   # Documentation (this folder)
├── paper/                  # Academic paper
└── requirements.txt        # Dependencies
```

## Core Components

### Entry Point: Home.py

The main application file that initializes the Streamlit app:

```python
# Home.py structure
import streamlit as st
from shared import config

# Page configuration
st.set_page_config(...)

# Session state initialization
if 'pdbs' not in st.session_state:
    st.session_state['pdbs'] = ""

# Main content
st.header("PROMETRY")
st.write("Description...")
```

### Code Module (`code/`)

Core functionality modules:

#### header.py
- Application header and branding
- Version information
- Navigation helpers

#### plots.py
- Plotting functions for various visualizations
- Matplotlib and Plotly integrations
- Custom plot styles

#### structures.py
- Structure loading and parsing
- BioPython integration
- Structure validation

### Shared Module (`shared/`)

Reusable components across pages:

#### config.py
```python
# Configuration management
def init():
    """Initialize application configuration"""
    
def get_settings():
    """Retrieve current settings"""
    
def save_settings(settings):
    """Persist settings"""
```

#### dataframe_maker.py
```python
# Data generation
def create_dataframe(pdb_codes, geometry, criteria):
    """Generate analysis dataframe"""
    
def create_correlation_df(pdb_codes, geo1, geo2):
    """Create correlation data"""
```

#### geo_plotter.py
```python
# Geometric plotting
def create_interactive_plot(data, x_col, y_col):
    """Create Plotly visualization"""
```

#### structure_explorer.py
```python
class StructureExplorer:
    """Explore protein structures"""
    
    def __init__(self, pdb_code):
        self.structure = load_structure(pdb_code)
    
    def get_secondary_structure(self):
        """Get DSSP assignment"""
    
    def calculate_geometry(self, atoms):
        """Calculate geometric parameters"""
```

#### simple_plotsheet.py
```python
# Simple plotting utilities
def create_simple_plot(data, plot_type):
    """Generate basic plots"""
```

#### validation_plotsheet.py
```python
# Validation and quality checks
def validate_structure(structure, criteria):
    """Run validation checks"""
```

### Pages Module (`pages/`)

Streamlit pages for different features:

```
pages/
├── 1_Structure_Search.py       # PDB structure search
├── 2_Correlation.py            # Correlation analysis
├── 3_Contact Map.py            # Contact map generation
├── 4_3d Space.py               # 3D visualization
├── 5_Validation.py             # Structure validation
├── 6_Criteria.py               # Criteria testing
├── 7_Citing.py                 # Citation information
└── 8_Help.py                   # Help documentation
```

Each page follows a similar structure:

```python
import streamlit as st
from shared import config, dataframe_maker

# Page configuration
st.set_page_config(...)

# Page header
st.header("Page Title")

# Input widgets
pdb_code = st.text_input("Enter PDB Code")

# Processing
if st.button("Process"):
    data = process_input(pdb_code)
    st.write(data)
    
# Visualization
if data is not None:
    fig = create_plot(data)
    st.plotly_chart(fig)
    
# Download options
st.download_button("Download CSV", data.to_csv())
```

## Data Flow

### Typical Request Flow

1. **User Input** → Page widget (text input, file upload, etc.)
2. **Validation** → Input validation and error handling
3. **Processing** → Data generation via `dataframe_maker`
4. **Analysis** → Geometric calculations, filtering
5. **Visualization** → Plot generation via `plots` or `geo_plotter`
6. **Output** → Display results, download options

```
User Input → Validation → Structure Loading → Geometry Calculation
                                              ↓
Display ← Plotting ← Filtering ← Data Generation
```

## Session State Management

PROMETRY uses Streamlit session state to persist data:

```python
# Initialize session state
if 'pdbs' not in st.session_state:
    st.session_state['pdbs'] = ""
    
if 'data' not in st.session_state:
    st.session_state['data'] = None

# Store data
st.session_state['data'] = new_data

# Retrieve data
data = st.session_state.get('data', None)
```

**Common session variables:**
- `pdbs`: Current PDB code(s)
- `geos`: Geometry definitions
- `data`: Generated dataframe
- `code_df`: Code snippets for reproducibility

## External Dependencies

### Core Libraries

#### BioPython
```python
from Bio.PDB import PDBParser, DSSP
from Bio.PDB.Structure import Structure
```
Used for:
- PDB file parsing
- Structure manipulation
- Secondary structure assignment (DSSP)

#### Prometry Library
```python
import maptial
from maptial.geo import pdbgeometry
```
Core library providing:
- Geometric calculations
- Structure search functionality
- Criteria filtering

#### Plotly
```python
import plotly.graph_objects as go
import plotly.express as px
```
Interactive visualizations

#### Pandas
```python
import pandas as pd
```
Data manipulation and analysis

#### NumPy/SciPy
```python
import numpy as np
from scipy import stats
```
Numerical computations

## Design Patterns

### Singleton Pattern (Config)

```python
class Config:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory Pattern (Plot Creation)

```python
def create_plot(plot_type, data, **kwargs):
    if plot_type == "ramachandran":
        return RamachandranPlot(data, **kwargs)
    elif plot_type == "contact_map":
        return ContactMapPlot(data, **kwargs)
    # ... more plot types
```

### Strategy Pattern (Geometry Calculation)

```python
class GeometryCalculator:
    def calculate(self, atoms):
        if len(atoms) == 2:
            return self._calculate_distance(atoms)
        elif len(atoms) == 3:
            return self._calculate_angle(atoms)
        elif len(atoms) == 4:
            return self._calculate_dihedral(atoms)
```

## Testing Structure

```
tests/
├── test_structures.py      # Structure loading tests
├── test_geometry.py         # Geometric calculation tests
├── test_dataframe.py        # Dataframe generation tests
├── test_plotting.py         # Visualization tests
└── test_criteria.py         # Criteria filtering tests
```

Example test:

```python
import pytest
from shared import dataframe_maker

def test_create_dataframe():
    df = dataframe_maker.create_dataframe(
        pdb_codes=["1t29"],
        geometry_definition="CA-CA",
        criteria={"chain": "A"}
    )
    
    assert not df.empty
    assert "distance" in df.columns
    assert len(df) > 0
```

## Deployment

### Streamlit Cloud

Deployed via GitHub integration:
1. Push to main branch
2. Automatic deployment to streamlit.app
3. Environment variables configured in Streamlit dashboard

### Configuration Files

#### requirements.txt
Lists all Python dependencies

#### .streamlit/config.toml
Streamlit-specific configuration:
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"

[server]
maxUploadSize = 200
enableCORS = false
```

## Performance Considerations

### Caching

```python
@st.cache_data
def load_structure(pdb_code):
    """Cached structure loading"""
    return fetch_and_parse_pdb(pdb_code)

@st.cache_resource
def get_prometry_instance():
    """Cached resource initialization"""
    return PrometryLib()
```

### Lazy Loading

```python
# Load data only when needed
if st.button("Calculate"):
    with st.spinner("Processing..."):
        data = expensive_calculation()
        st.session_state['data'] = data
```

### Progress Indicators

```python
progress_bar = st.progress(0)
for i, pdb in enumerate(pdb_codes):
    process_structure(pdb)
    progress_bar.progress((i + 1) / len(pdb_codes))
```

## Next Steps

- Review [Core API](core.md) for function details
- Check [Contributing Guidelines](../contributing/guidelines.md)
- See [Development Guide](../contributing/development.md)
