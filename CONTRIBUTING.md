# Contributing to xhale

Xeus and xhale are subprojects of Project Jupyter and subject to the [Jupyter governance](https://github.com/jupyter/governance) and [Code of conduct](https://github.com/jupyter/governance/blob/master/conduct/code_of_conduct.md).

## General Guidelines

For general documentation about contributing to Jupyter projects, see the [Project Jupyter Contributor Documentation](https://jupyter.readthedocs.io/en/latest/contributor/content-contributor.html).

## Community

The Xeus team organizes public video meetings. The schedule for future meetings and minutes of past meetings can be found on our [team compass](https://jupyter-xeus.github.io/).

## Setting up a development environment

First, you need to fork the project. Then setup your environment:

```bash
# create a new conda environment
conda create -n xhale -c conda-forge -c defaults sphinx
six
conda activate xhale

# download xhale from your GitHub fork
git clone https://github.com/<your-github-username>/xhale.git
```

