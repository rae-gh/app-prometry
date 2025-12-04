# Visualizations

PROMETRY provides powerful visualization capabilities for protein structures and geometric analyses.

## Visualization Types

### 1. 3D Structure Visualization

Interactive 3D visualization of protein structures:

```python
from prometry import plots
import plotly.graph_objects as go

# Load structure
structure = get_structure("1t29")

# Create 3D plot
fig = plots.plot_structure_3d(
    structure,
    chain="A",
    color_by="secondary_structure"
)

fig.show()
```

**Coloring options:**
- `residue_type`: Color by amino acid
- `secondary_structure`: Color by DSSP assignment
- `b_factor`: Color by temperature factor
- `chain`: Color by chain
- `custom`: Provide custom color mapping

### 2. Contact Maps

Visualize residue-residue interactions:

```python
# Generate contact map
contact_map = plots.create_contact_map(
    structure,
    chain="A",
    distance_threshold=8.0,  # Ångströms
    atom_type="CA"           # Alpha carbons
)

# Display
fig = plots.plot_contact_map(contact_map)
fig.show()
```

### 3. Ramachandran Plots

Classic phi-psi angle distribution:

```python
# Create Ramachandran plot
fig = plots.ramachandran_plot(
    structure,
    chain="A",
    show_allowed_regions=True,
    color_by_residue=True
)

fig.show()
```

### 4. Distance Distributions

Histogram of geometric parameters:

```python
# Distance distribution
distances = calculate_distances(structure, ["CA", "CA"])

fig = plots.plot_distribution(
    distances,
    bins=50,
    xlabel="Distance (Å)",
    title="CA-CA Distance Distribution"
)

fig.show()
```

### 5. Correlation Plots

Compare two geometric parameters:

```python
# Phi vs Psi
phi_angles = calculate_phi(structure)
psi_angles = calculate_psi(structure)

fig = plots.scatter_plot(
    phi_angles,
    psi_angles,
    xlabel="Phi (degrees)",
    ylabel="Psi (degrees)",
    title="Ramachandran Plot"
)

fig.show()
```

## Plotting Libraries

### Plotly (Interactive)

Default for web application:

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=data['x'],
    y=data['y'],
    mode='markers',
    marker=dict(size=5, color='blue')
))

fig.update_layout(
    title="Interactive Plot",
    xaxis_title="X Axis",
    yaxis_title="Y Axis"
)

fig.show()
```

### Matplotlib (Static)

For publication-quality figures:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(data['x'], data['y'], alpha=0.6)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Static Plot')
plt.tight_layout()
plt.savefig('output.png', dpi=300)
plt.show()
```

### Seaborn (Statistical)

For statistical visualizations:

```python
import seaborn as sns

sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))

sns.violinplot(
    data=df,
    x='residue',
    y='angle',
    ax=ax
)

plt.title('Angle Distribution by Residue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## Customization

### Color Schemes

```python
# Predefined color schemes
color_schemes = {
    "hydrophobicity": {
        "ALA": "#ff0000",
        "VAL": "#ff3300",
        # ... more residues
    },
    "secondary_structure": {
        "H": "#FF0000",  # Helix - red
        "E": "#0000FF",  # Sheet - blue
        "C": "#00FF00"   # Coil - green
    }
}

# Apply color scheme
fig = plots.plot_structure_3d(
    structure,
    color_scheme=color_schemes["secondary_structure"]
)
```

### Layout Customization

```python
# Plotly layout
fig.update_layout(
    title="Custom Title",
    font=dict(size=14, family="Arial"),
    width=1200,
    height=800,
    showlegend=True,
    legend=dict(x=1, y=1),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Matplotlib style
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.size'] = 12
plt.rcParams['figure.dpi'] = 300
```

## Advanced Visualizations

### Multi-Panel Figures

```python
from matplotlib import pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(12, 12))

# Panel 1: Ramachandran
plots.ramachandran_plot(structure, ax=axes[0, 0])

# Panel 2: Distance distribution
plots.distance_histogram(structure, ax=axes[0, 1])

# Panel 3: Contact map
plots.contact_map(structure, ax=axes[1, 0])

# Panel 4: B-factor plot
plots.bfactor_plot(structure, ax=axes[1, 1])

plt.tight_layout()
plt.savefig('multi_panel.png', dpi=300)
```

### Animated Visualizations

```python
import plotly.graph_objects as go

# Create frames for animation
frames = []
for i, angle in enumerate(range(0, 360, 10)):
    frame = go.Frame(
        data=[go.Scatter3d(
            x=coords_rotated[i][:, 0],
            y=coords_rotated[i][:, 1],
            z=coords_rotated[i][:, 2]
        )],
        name=str(i)
    )
    frames.append(frame)

# Create figure with frames
fig = go.Figure(frames=frames)
fig.show()
```

### Heat Maps

```python
import seaborn as sns

# Create distance matrix
distance_matrix = calculate_distance_matrix(structure)

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    distance_matrix,
    cmap='viridis',
    cbar_kws={'label': 'Distance (Å)'},
    xticklabels=residue_labels,
    yticklabels=residue_labels
)
plt.title('Residue Distance Matrix')
plt.tight_layout()
plt.savefig('heatmap.png', dpi=300)
```

## Export Options

### Image Formats

```python
# Matplotlib
plt.savefig('figure.png', dpi=300)
plt.savefig('figure.pdf')
plt.savefig('figure.svg')

# Plotly
fig.write_image('figure.png', width=1200, height=800)
fig.write_image('figure.pdf')
fig.write_html('interactive.html')
```

### Data Export

```python
# Export underlying data
import pandas as pd

df = pd.DataFrame({
    'x': data_x,
    'y': data_y
})

df.to_csv('data.csv', index=False)
df.to_excel('data.xlsx', index=False)
df.to_json('data.json')
```

## Web Application Features

The PROMETRY web app provides:

1. **Interactive 3D Viewer**: Rotate, zoom, and explore structures
2. **Download Options**: PNG, SVG, PDF exports
3. **Customizable Plots**: Adjust colors, sizes, labels
4. **Data Tables**: View and download underlying data
5. **Plot Gallery**: Save multiple plots for comparison

## Performance Tips

### Large Structures

```python
# Subsample for visualization
structure_subset = sample_residues(structure, every_n=5)

# Use simpler representations
fig = plots.plot_structure_3d(
    structure,
    representation="cartoon",  # Faster than "stick"
    resolution="low"
)
```

### Multiple Plots

```python
# Batch generation
plots_config = [
    {"type": "ramachandran", "chain": "A"},
    {"type": "contact_map", "chain": "A"},
    {"type": "distance_dist", "atoms": ["CA", "CA"]}
]

for config in plots_config:
    fig = generate_plot(structure, **config)
    fig.savefig(f"{config['type']}.png")
```

## Best Practices

1. **Choose Appropriate Plot Type**: Match visualization to data type
2. **Label Clearly**: Always include axis labels and units
3. **Use Color Wisely**: Ensure colorblind-friendly palettes
4. **Export High Resolution**: Use DPI ≥ 300 for publications
5. **Document Settings**: Record all visualization parameters
6. **Test Interactivity**: Verify tooltips and zoom work as expected

## Example: Publication-Ready Figure

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set publication style
plt.style.use('seaborn-v0_8-paper')
sns.set_context("paper", font_scale=1.5)

# Create figure
fig, ax = plt.subplots(figsize=(6, 5))

# Plot data
ax.scatter(phi, psi, alpha=0.6, s=30, c='#2E86AB')

# Formatting
ax.set_xlabel('Phi (degrees)', fontweight='bold')
ax.set_ylabel('Psi (degrees)', fontweight='bold')
ax.set_title('Ramachandran Plot - Structure 1T29', fontweight='bold')
ax.set_xlim(-180, 180)
ax.set_ylim(-180, 180)
ax.axhline(0, color='k', linestyle='--', alpha=0.3, linewidth=0.5)
ax.axvline(0, color='k', linestyle='--', alpha=0.3, linewidth=0.5)
ax.grid(True, alpha=0.3)

# Save
plt.tight_layout()
plt.savefig('ramachandran_publication.png', dpi=300, bbox_inches='tight')
plt.savefig('ramachandran_publication.pdf', bbox_inches='tight')
```

## Next Steps

- Review [Geometric Search](geometric-search.md)
- Explore [Criteria & Filters](criteria.md)
- Check [API Reference](../api/core.md)
