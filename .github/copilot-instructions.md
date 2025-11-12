# GitHub Copilot Instructions

## Project Overview

This is an **AI/ML educational repository** for course IA1-20252 at UIS (Universidad Industrial de Santander). It contains Jupyter notebooks for teaching and practicing fundamental AI/ML concepts including:
- Python fundamentals, NumPy, Pandas
- Genetic Algorithms
- Data visualization (Matplotlib, Seaborn, Plotly)
- Statistics and probability
- Classification and regression models
- Deep learning

## Repository Structure

```
notebooks_IA1/
├── XX_std_*.ipynb           # Course notes/lessons (01-06)
├── Taller_std_XX_*.ipynb    # Student assignments/workshops (01-07)
└── .github/
    └── copilot-instructions.md
```

**Naming Convention:**
- `XX_std_Notes_*.ipynb` - Lecture notes and tutorials
- `Taller_std_XX_20252_*.ipynb` - Graded assignments/workshops
- XX = sequential number (01, 02, etc.)

## Standard Notebook Structure

Every notebook follows this consistent pattern:

### 1. Header Cell (Markdown)
```python
<img src="https://gitlab.com/bivl2ab/academico/cursos-uis/ai/ai-uis-student/raw/master/imgs/banner_IA.png" width="1000px" height="200px">
```

### 2. Configuration Cell (Python)
```python
#@title Execute this cell
#@markdown Please include your student id
import sys
import inspect

group_id = "IA1-20252-XX" #@param {type:"string"}
assignment_id = group_id +'.topic_name'
student_id = "XXXXXXX" #@param {type:"string"}
```

**Important:** Group IDs follow pattern `IA1-20252-C1` or `IA1-20252-E1`

### 3. Grading Utilities Cell
Every assignment notebook includes a standard `check_solution_and_evaluate()` function that:
- Sends student solutions to `https://bivlabgrader.azurewebsites.net/api/CheckAndEvaluateSolution`
- Uses POST requests with payload: `{func_str, assignment_id, student_id}`
- Returns formatted JSON responses via `pprint_json_response()`

**Never modify** cells marked with `#@markdown Please dont modify any line in this cell`

## Tech Stack

### Core Libraries
- **numpy** - Array operations, random seeds always set to 21
- **pandas** - DataFrames, data manipulation
- **matplotlib.pyplot** - Basic plotting
- **seaborn** - Statistical visualizations (theme: `sns.set_theme()`)
- **plotly** - Interactive visualizations (used with cufflinks in offline mode)

### ML/DL Libraries (in later notebooks)
- **scikit-learn** - Classification, regression, statistics
- **tensorflow/keras** or **pytorch** - Deep learning

### Standard Imports Pattern
```python
import numpy as np
np.random.seed(21)  # ALWAYS set seed to 21
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
import warnings
warnings.filterwarnings('ignore')
```

## Critical Patterns

### Random Seed
**ALWAYS** set `np.random.seed(21)` in notebooks - this is a course requirement for reproducibility.

### Google Colab Compatibility
Many notebooks include Colab-specific cells:
```python
#@title 1. MONTAR EL DRIVE { display-mode: "form" }
import os
from google.colab import drive
drive.mount('/content/drive')
os.chdir('/content/drive/My Drive/ai-uis-student-master')
```

### File Writing Pattern
Notebooks often save Python code to files using:
```python
%%writefile code/ga.py
```

### Exercise Structure
Exercises use anchor links: `<a name="eje1"></a>` and are marked with icon:
```markdown
<img src="https://gitlab.com/bivl2ab/academico/cursos-uis/ai/ai-2-uis-student/-/raw/master/imgs/icon1.png" width="200">
```

## Data Sources

Common datasets referenced:
- California Housing: `https://storage.googleapis.com/mledu-datasets/california_housing_train.csv`
- Titanic dataset for pandas/visualization exercises
- Custom datasets from course GitLab repository

## Debugging & Testing

- Use `check_solution_and_evaluate()` to validate student solutions
- All code cells should be executable independently (idempotent)
- Include visualization outputs inline for verification
- Use `#@title` and `#@markdown` for Colab form-style interfaces

## Best Practices

1. **Never break the grading infrastructure** - Don't modify utility cells
2. **Maintain consistent formatting** - Follow the established cell structure
3. **Use type hints** - Functions should specify parameter types: `def foo(x: int) -> float:`
4. **Include markdown explanations** - Every code block should have context
5. **Keep notebook linear** - Cells should execute top-to-bottom without errors
6. **Preserve existing student IDs** - Don't overwrite them when editing notebooks

## Assignment vs Notes Differences

**Notes (`XX_std_Notes_*.ipynb`):**
- Educational content with theory
- Example solutions provided
- More detailed explanations

**Talleres (`Taller_std_XX_*.ipynb`):**
- Student exercises with `#@title **code student**` cells
- Solutions submitted to grading server
- Context-rich problem statements

## When Adding New Content

1. Copy the standard header and configuration cells
2. Increment the notebook number appropriately
3. Set the correct `assignment_id` pattern
4. Include the grading utilities if it's an assignment
5. Set `np.random.seed(21)`
6. Follow the outline structure with markdown sections