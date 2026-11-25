# Git Version Control – MyShop Performance Engineering

## 1. Objective

Implement Git-based version control to manage application source code, performance test scripts and technical documentation.

## 2. Environment

- Operating System: Windows
- Version Control: Git
- Remote Repository: GitHub
- IDE: Visual Studio Code
- Application: FastAPI and PostgreSQL
- Performance Testing Tool: Apache JMeter 5.6.3

## 3. Git Commands and Practical Usage

| Command | Purpose |
|---|---|
| `git init` | Initialize a local repository |
| `git status` | Identify staged, unstaged and untracked changes |
| `git add` | Stage changes for the next commit |
| `git commit -m "message"` | Save a snapshot locally |
| `git push origin main` | Push local commits to GitHub |
| `git pull --rebase origin main` | Synchronize remote changes with local commits |
| `git log` | Review commit history |
| `git log --oneline -5` | Display the five most recent commits |

## 4. Version Control Workflow

Working Directory → Staging Area → Local Repository → Remote Repository

- Developed and modified FastAPI endpoints locally.
- Reviewed repository status before staging changes.
- Created meaningful commit messages.
- Synchronized application changes with GitHub.
- Organized JMeter scripts in a dedicated performance-tests directory.

## 5. Git Troubleshooting

### Issue: Git push rejected

During application development, a Git push was rejected because the remote repository contained changes.

### Resolution

Used `git pull --rebase origin main` to synchronize the local repository with the remote repository.

Verified the final repository status and commit history.

### Result

The local application repository was successfully synchronized with GitHub.

## 6. Security Best Practices

Configured `.gitignore` to exclude:

- `.env` – Database credentials and environment variables
- `.venv/` – Python virtual environment
- `__pycache__/` – Python cache files
- `*.pyc` – Compiled Python files

## 7. Skills Demonstrated

- Git repository management
- Source code version control
- Remote repository synchronization
- Git troubleshooting
- Performance test script organization
- Secure configuration management
- Technical documentation

## 8. Planned Enhancements

- Feature branch management
- Pull requests and code reviews
- Merge conflict resolution
- GitHub Actions CI/CD integration
- Automated JMeter performance regression testing
- Performance quality gates


Documentation progress
 Create documentation folder

 Create Markdown files

 Save Git documentation

 Document performance troubleshooting

 Update README

 Push documentation to GitHub

