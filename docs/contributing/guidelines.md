# Contributing Guidelines

Thank you for your interest in contributing to PROMETRY! This document provides guidelines for contributing to the project.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. All contributors are expected to:

- Be respectful and considerate
- Welcome newcomers and help them get started
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Bugs

Before creating a bug report:
1. Check the [existing issues](https://github.com/rae-gh/app-prometry/issues)
2. Verify you're using the latest version
3. Collect relevant information (OS, Python version, error messages)

Create a bug report with:
- **Clear title**: Summarize the issue
- **Description**: Detailed explanation of the problem
- **Steps to reproduce**: Minimal example demonstrating the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: Python version, OS, dependencies
- **Screenshots**: If applicable

Example:
```markdown
### Bug: Distance calculation returns negative values

**Description**
When calculating CA-CA distances for structure 1t29, some values are negative.

**To Reproduce**
```python
from shared import dataframe_maker
df = dataframe_maker.create_dataframe(["1t29"], "CA-CA", {"chain": "A"})
print(df[df['distance'] < 0])
```

**Expected**: All distances should be positive
**Actual**: Found 3 negative distances

**Environment**: Python 3.10, Ubuntu 22.04
```

### Suggesting Features

Feature requests should include:
- **Clear use case**: Why is this feature needed?
- **Proposed solution**: How should it work?
- **Alternatives**: Other approaches considered
- **Additional context**: Examples, mockups, or references

### Submitting Pull Requests

1. **Fork the repository**
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following the code style
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Commit your changes** with clear messages
7. **Push to your fork**
8. **Open a Pull Request**

## Pull Request Guidelines

### PR Title

Use conventional commit format:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add hydrogen bond detection algorithm
fix: correct angle calculation for edge cases
docs: update installation instructions
refactor: simplify dataframe_maker logic
```

### PR Description

Include:
- **Summary**: What does this PR do?
- **Motivation**: Why is this change needed?
- **Changes**: List of key modifications
- **Testing**: How was this tested?
- **Screenshots**: For UI changes
- **Related issues**: Link to related issues

Template:
```markdown
## Summary
Adds hydrogen bond detection functionality

## Motivation
Users requested ability to identify potential H-bonds (#123)

## Changes
- Added `find_hydrogen_bonds()` function
- Updated criteria system to support H-bond parameters
- Added tests for H-bond detection
- Updated documentation

## Testing
- Added unit tests with >90% coverage
- Manually tested with structures 1t29, 2pah, 3cln
- Validated against literature values

## Related Issues
Closes #123
```

### PR Checklist

Before submitting, ensure:
- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] Commit messages are clear and descriptive
- [ ] No unnecessary files included
- [ ] PR targets the correct branch

## Code Review Process

### What to Expect

1. **Initial Review**: Maintainer will review within 1-2 weeks
2. **Feedback**: You may receive change requests
3. **Iteration**: Make requested changes
4. **Approval**: Once approved, PR will be merged
5. **Release**: Changes included in next release

### Review Criteria

Reviewers will check:
- **Functionality**: Does it work as intended?
- **Tests**: Are there adequate tests?
- **Code Quality**: Is it readable and maintainable?
- **Documentation**: Is it properly documented?
- **Performance**: Are there performance implications?
- **Breaking Changes**: Does it maintain backward compatibility?

## Development Guidelines

### Code Style

Follow PEP 8 and project conventions:

```python
# Good
def calculate_distance(atom1, atom2):
    """Calculate distance between two atoms.
    
    Args:
        atom1: First atom
        atom2: Second atom
        
    Returns:
        Distance in Ångströms
    """
    vector = atom2.coord - atom1.coord
    return np.linalg.norm(vector)

# Bad
def calc_dist(a1,a2):
    v=a2.coord-a1.coord
    return np.linalg.norm(v)
```

### Testing Requirements

All new code must include tests:

```python
def test_calculate_distance():
    """Test distance calculation."""
    # Create test atoms
    atom1 = create_test_atom([0, 0, 0])
    atom2 = create_test_atom([3, 4, 0])
    
    # Calculate distance
    distance = calculate_distance(atom1, atom2)
    
    # Assert expected result
    assert abs(distance - 5.0) < 0.001

def test_calculate_distance_edge_cases():
    """Test distance calculation edge cases."""
    # Same position
    atom1 = create_test_atom([0, 0, 0])
    atom2 = create_test_atom([0, 0, 0])
    assert calculate_distance(atom1, atom2) == 0.0
    
    # Very large distance
    atom3 = create_test_atom([1000, 1000, 1000])
    assert calculate_distance(atom1, atom3) > 1000
```

### Documentation Requirements

Document all public APIs:

```python
def create_dataframe(
    pdb_codes: List[str],
    geometry_definition: str,
    criteria: Optional[Dict] = None
) -> pd.DataFrame:
    """Create a dataframe with geometric parameters.
    
    This function loads PDB structures, calculates geometric parameters
    according to the definition, and applies optional criteria filters.
    
    Args:
        pdb_codes: List of 4-character PDB codes
        geometry_definition: Atom specification string (e.g., "CA-CA")
        criteria: Optional dictionary of filtering criteria
        
    Returns:
        DataFrame with columns: pdb, chain, residue, value
        
    Raises:
        ValueError: If geometry_definition is invalid
        PDBNotFoundError: If PDB code doesn't exist
        
    Example:
        >>> df = create_dataframe(
        ...     pdb_codes=["1t29"],
        ...     geometry_definition="CA-CA",
        ...     criteria={"chain": "A"}
        ... )
        >>> print(df.head())
    """
    pass
```

## Specific Contribution Areas

### Adding Geometric Calculations

1. Implement in appropriate module
2. Add comprehensive tests
3. Document formula and references
4. Add usage examples
5. Update API documentation

### Adding Visualizations

1. Create plot function
2. Support multiple output formats (Plotly, Matplotlib)
3. Allow customization (colors, labels, size)
4. Add interactive features where appropriate
5. Include example plots in documentation

### Adding Application Pages

1. Follow existing page structure
2. Use session state appropriately
3. Include help text and examples
4. Add download options for data
5. Ensure mobile-friendly layout
6. Update navigation if needed

### Improving Documentation

Documentation improvements are always welcome:
- Fix typos and clarify explanations
- Add examples and use cases
- Create tutorials
- Improve API documentation
- Add diagrams and visualizations

## Communication

### GitHub Issues

Use GitHub issues for:
- Bug reports
- Feature requests
- Documentation improvements
- General discussions

### Discussions

Use GitHub Discussions for:
- Questions about usage
- Design discussions
- Sharing use cases
- Community support

### Contact

For direct communication:
- Email: rachelalcraft@gmail.com
- GitHub: @RachelAlcraft

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Acknowledged in release notes
- Credited in academic citations (for significant contributions)

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

## Questions?

If you have questions about contributing:
1. Check existing documentation
2. Search closed issues
3. Ask in GitHub Discussions
4. Contact the maintainers

Thank you for contributing to PROMETRY!
