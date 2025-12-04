# Installation

This guide will help you set up PROMETRY on your system.

## Requirements

- Python 3.8 or higher
- pip package manager

## Installation Methods

### Using pip (Recommended)

Install PROMETRY directly from PyPI:

```bash
pip install prometry
```

### From Source

Clone the repository and install:

```bash
git clone https://github.com/rae-gh/app-prometry.git
cd app-prometry
pip install -r requirements.txt
```

## Required Dependencies

The main dependencies include:

- **streamlit**: Web application framework
- **prometry**: Core library for geometric calculations
- **biopython**: Biological data structures and file parsing
- **plotly**: Interactive visualizations
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **scipy**: Scientific computing
- **matplotlib & seaborn**: Plotting libraries

For the complete list, see `requirements.txt` in the repository.

## Running the Application Locally

After installation, run the Streamlit application:

```bash
streamlit run app/Home.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Verify Installation

Test your installation by running:

```python
import prometry
import streamlit as st
print("PROMETRY is ready to use!")
```

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'prometry'`

**Solution**: Ensure you've activated the correct Python environment and installed the package:
```bash
pip install --upgrade prometry
```

**Issue**: `urllib3` version conflicts

**Solution**: The application requires `urllib3==1.26.6`. Install it explicitly:
```bash
pip install urllib3==1.26.6
```

**Issue**: Streamlit port already in use

**Solution**: Specify a different port:
```bash
streamlit run app/Home.py --server.port 8502
```

## Next Steps

- Follow the [Quick Start Guide](quick-start.md) to begin using PROMETRY
- Explore the [User Guide](../user-guide/overview.md) for detailed features
- Check out the [examples](https://prometry.streamlit.app) on the live application
