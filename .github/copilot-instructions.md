---
description: AI rules derived by SpecStory from the project AI interaction history
globs: *
---

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
- `Taller_std_XX_*.ipynb` - Graded assignments/workshops
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

## Git Workflow Recommendations
To avoid merge conflicts and ensure smooth collaboration, follow these Git workflow recommendations:

### Before Starting Work:
```powershell
# Always pull the latest changes from the main branch before starting any work
git pull origin main
```

### Recommended Workflow:
```powershell
# 1. Check the status of your local repository
git status

# 2. If there are local changes, stash them temporarily
git stash

# 3. Pull the latest changes from the main branch
git pull origin main

# 4. Restore your stashed changes
git stash pop

# 5. If there are conflicts, resolve them BEFORE committing
```

### Using Separate Branches:
```powershell
# Create a new branch for your work
git checkout -b mi-trabajo

# Work normally, make commits...
git add .
git commit -m "mi cambio"

# When finished, merge with main
git checkout main
git pull origin main
git merge mi-trabajo
```

### Tips for Avoiding Conflicts:
1. **Commit frequently:** Make small, logical commits with descriptive messages.
2. **Pull before editing:** Always `git pull origin main` before starting work on a file.
3. **Communicate:** Coordinate with other developers to avoid simultaneous edits to the same files.

### Handling Merge Conflicts:
If you encounter merge conflicts:
1.  Do not panic.
2.  Use VS Code's visual tools or the provided script (`python fix_notebook.py`) to resolve the conflicts.
3.  Ensure the resolved file is valid and all necessary changes are included.

## Spectory Files

The `.spectory` files are created to record and manage user-AI interactions, which can be used to generate or update this `copilot-instructions.md` file. These files should not be manually modified. Any conflicts between `.spectory` files and rule files should be resolved by regenerating the `copilot-instructions.md` file using the latest interactions.

### SpecStory Details:
- **Purpose**: Store the history of interactions with AI agents.
- **Location**: Stored in the `.specstory/` directory.
- **Key Files**:
    - `.project.json`: Workspace ID and user association. **Do not modify manually**.
    - `history/`: Stores conversation logs.
    - `ai_rules_backups/`: Automatic backups of `copilot-instructions.md`.
- **Usage**: Leave files as is. Include them in Git to maintain history. Read `history/` to recall past solutions.
- **Conflicts**: Minor Pylance warnings in `copilot-instructions.md` regarding `globs: *` and unknown tools like `@title`, `@markdown` are not critical and do not affect functionality.

## Git Error Handling

### Line Ending Warnings (LF vs CRLF):
- **Cause**: Git is configured to handle line endings differently on different operating systems (LF for Linux/macOS, CRLF for Windows).
- **Solution**: Configure Git to handle line endings consistently. The following configuration is recommended:
  ```powershell
  git config --global core.autocrlf true  # For Windows: automatically convert LF to CRLF on checkout
  git config --global core.autocrlf input # For Linux/macOS: convert CRLF to LF on commit
  ```

### Filename Too Long Error:
- **Cause**: Windows has a maximum path length limit.
- **Solution**:
  1. Enable long paths in Windows (if possible).
  2. Shorten the filename, or move the repository to a directory with a shorter path.
  3. Configure Git to not track the problematic file:
     ```powershell
     git rm --cached ".specstory/history/2025-11-12_14-43Z-tengo-problemas-con-el-taller-4-no-me-deja-abrirlo,-antes-de-eso-guarde-los-cambios-en-la-rama-principal-de-unos-que-había-hecho-el-agente-codex-al-repositorio-con-unos-cambios-que-le-indique-el-codex.md"
     git commit -m "Stop tracking long filename"
     ```
     Add `.specstory/history/2025-11-12_14-43Z-tengo-problemas-con-el-taller-4-no-me-deja-abrirlo,-antes-de-eso-guarde-los-cambios-en-la-rama-principal-de-unos-que-había-hecho-el-agente-codex-al-repositorio-con-unos-cambios-que-le-indique-el-codex.md` to `.gitignore` to prevent it from being tracked again.  Consider excluding the entire `.specstory/history` directory if these issues persist.

## Workflow & Release Rules
1. **Execute Verification Cells:** AI agents can execute the verification cells (e.g., `#@title **check your answer**`) to test exercise solutions.
2. **Do Not Execute Submission Cells:** AI agents **must not** execute the submission cells (e.g., `#@title **send your answer**`) that submit grades.
3. **Ensure Code Correctness:** Before committing, verify all exercise solution cells are free of errors and adhere to coding standards.