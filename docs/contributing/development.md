# Development Guide

This guide will help you set up a development environment and contribute to PROMETRY.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- pip or conda
- Code editor (VS Code recommended)

### Clone Repository

```bash
git clone https://github.com/rae-gh/app-prometry.git
cd app-prometry
```

### Create Virtual Environment

Using venv:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Using conda:
```bash
conda create -n prometry python=3.10
conda activate prometry
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

For development, install additional tools:
```bash
pip install pytest pytest-cov black flake8 mypy
```

### Run Application Locally

```bash
streamlit run app/Home.py
```

The application will be available at `http://localhost:8501`

## Project Structure

Understanding the codebase:

```
app-prometry/
├── app/
│   ├── Home.py              # Main entry point
│   ├── code/                # Core modules
│   ├── shared/              # Shared utilities
│   ├── pages/               # Streamlit pages
│   ├── data/                # Sample data
│   └── static/              # Assets
├── docs/                    # MkDocs documentation
├── paper/                   # Academic paper
├── tests/                   # Test suite (to be created)
├── requirements.txt         # Dependencies
└── mkdocs.yml              # Documentation config
```

## Development Workflow

### Branch Strategy

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Create bugfix branch
git checkout -b bugfix/issue-description

# Create documentation branch
git checkout -b docs/topic-name
```

### Making Changes

1. **Write Code**: Implement your feature or fix
2. **Test**: Ensure all tests pass
3. **Document**: Update relevant documentation
4. **Commit**: Write clear commit messages
5. **Push**: Push to your branch
6. **Pull Request**: Create PR for review

### Commit Messages

Follow conventional commits:

```bash
# Feature
git commit -m "feat: add hydrogen bond detection"

# Bug fix
git commit -m "fix: correct angle calculation for edge cases"

# Documentation
git commit -m "docs: update installation guide"

# Refactor
git commit -m "refactor: simplify dataframe_maker logic"

# Test
git commit -m "test: add tests for geometry calculations"
```

## Code Style

### Python Style Guide

Follow PEP 8 with these conventions:

```python
# Imports
import standard_library
import third_party_package
from local_module import function

# Constants
MAX_DISTANCE = 10.0
DEFAULT_RESOLUTION = 2.0

# Functions
def calculate_distance(atom1, atom2):
    """Calculate distance between two atoms.
    
    Args:
        atom1: First atom object
        atom2: Second atom object
        
    Returns:
        Distance in Ångströms
    """
    pass

# Classes
class StructureExplorer:
    """Explore protein structures."""
    
    def __init__(self, pdb_code):
        """Initialize explorer with PDB code."""
        self.pdb_code = pdb_code
```

### Code Formatting

Use Black for automatic formatting:

```bash
# Format specific file
black app/shared/dataframe_maker.py

# Format entire project
black app/

# Check without modifying
black --check app/
```

### Linting

Use flake8 for style checking:

```bash
flake8 app/ --max-line-length=88 --extend-ignore=E203
```

### Type Hints

Use type hints for better code quality:

```python
from typing import List, Dict, Optional, Tuple

def create_dataframe(
    pdb_codes: List[str],
    geometry: str,
    criteria: Optional[Dict] = None
) -> pd.DataFrame:
    """Create geometry dataframe."""
    pass
```

Run type checking:
```bash
mypy app/
```

## Testing

### Writing Tests

Create tests in `tests/` directory:

```python
# tests/test_structures.py
import pytest
from code import structures

def test_load_pdb():
    """Test PDB loading functionality."""
    structure = structures.load_pdb("1t29")
    assert structure is not None
    assert len(list(structure.get_chains())) > 0

def test_invalid_pdb():
    """Test handling of invalid PDB codes."""
    with pytest.raises(structures.PDBNotFoundError):
        structures.load_pdb("INVALID")

@pytest.fixture
def sample_structure():
    """Fixture providing a sample structure."""
    return structures.load_pdb("1t29")

def test_chain_extraction(sample_structure):
    """Test chain extraction."""
    chains = structures.get_chains(sample_structure)
    assert "A" in chains
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_structures.py

# Run with coverage
pytest --cov=app tests/

# Generate coverage report
pytest --cov=app --cov-report=html tests/
```

### Test Coverage

Aim for >80% code coverage:

```bash
pytest --cov=app --cov-report=term-missing tests/
```

## Documentation

### Docstrings

Use Google-style docstrings:

```python
def calculate_dihedral(atom1, atom2, atom3, atom4):
    """Calculate dihedral angle between four atoms.
    
    The dihedral angle is calculated using the vectors formed by
    the four atoms, following standard geometric conventions.
    
    Args:
        atom1: First atom (BioPython Atom object)
        atom2: Second atom (axis start)
        atom3: Third atom (axis end)
        atom4: Fourth atom
        
    Returns:
        Dihedral angle in degrees, range [-180, 180]
        
    Raises:
        ValueError: If atoms are collinear
        
    Example:
        >>> dihedral = calculate_dihedral(n, ca, c, o)
        >>> print(f"Angle: {dihedral:.2f}°")
    """
    pass
```

### Building Documentation

The project uses MkDocs:

```bash
# Install MkDocs
pip install mkdocs mkdocs-material mkdocstrings

# Serve locally
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## Debugging

### Streamlit Debugging

Add debug information:

```python
import streamlit as st

# Display debug info
if st.checkbox("Show Debug Info"):
    st.write("Session State:", st.session_state)
    st.write("Data Shape:", st.session_state.get('data', pd.DataFrame()).shape)
```

### Logging

Use Python logging:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_structure(pdb_code):
    logger.info(f"Processing structure: {pdb_code}")
    try:
        result = expensive_operation(pdb_code)
        logger.info(f"Successfully processed {pdb_code}")
        return result
    except Exception as e:
        logger.error(f"Failed to process {pdb_code}: {e}")
        raise
```

### Performance Profiling

Profile slow operations:

```python
import cProfile
import pstats

def profile_function():
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Your code here
    result = slow_function()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)
```

## Adding New Features

### Adding a New Page

1. Create file in `app/pages/`:
```python
# app/pages/9_New_Feature.py
import streamlit as st
from shared import config

st.set_page_config(page_title="New Feature", layout="wide")

st.header("New Feature")
st.write("Description of the feature")

# Implementation
```

2. Add to documentation in `docs/user-guide/`

3. Update navigation if needed

### Adding New Geometry Calculation

1. Add to geometry module:
```python
# In appropriate module
def calculate_new_geometry(atoms):
    """Calculate new geometric parameter."""
    # Implementation
    pass
```

2. Add tests:
```python
def test_new_geometry():
    result = calculate_new_geometry(test_atoms)
    assert result > 0
```

3. Document in API reference

### Adding New Visualization

1. Create plot function:
```python
def create_new_plot(data, **kwargs):
    """Create new visualization."""
    fig = go.Figure()
    # Plot implementation
    return fig
```

2. Add to visualization guide

3. Add usage examples

## Common Issues

### Issue: Streamlit Session State

**Problem**: Session state not persisting

**Solution**: Always check initialization:
```python
if 'key' not in st.session_state:
    st.session_state['key'] = default_value
```

### Issue: BioPython PDB Parsing

**Problem**: Structure not loading correctly

**Solution**: Use proper error handling:
```python
try:
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(id, file)
except Exception as e:
    logger.error(f"Failed to parse PDB: {e}")
    raise
```

### Issue: Performance

**Problem**: Slow page loads

**Solution**: Use caching:
```python
@st.cache_data
def expensive_computation(params):
    # Heavy computation
    return result
```

## Release Process

### Version Numbering

Follow semantic versioning (MAJOR.MINOR.PATCH):

- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

### Creating a Release

1. Update version in `citation.cff`
2. Update CHANGELOG.md
3. Create git tag:
```bash
git tag -a v0.2.0 -m "Release version 0.2.0"
git push origin v0.2.0
```

4. Create GitHub release
5. Deploy to Streamlit Cloud (automatic)

## Next Steps

- Review [Contributing Guidelines](guidelines.md)
- Check [Code Structure](../api/code-structure.md)
- See [API Reference](../api/core.md)
