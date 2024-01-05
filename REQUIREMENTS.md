# REQUIREMENTS

We expect that everyone with reasonable programming experience can open and run the artifacts with standard environments.
Part of the artifacts have some package requirements, but there is no deviation from standard environments for data science.

The artifacts are tested with MacBook Pro (14-inch, 2021, Apple M1 Max, 32 GB Memory).

#### GILT (Generation-based Information-support with LLM Technology): [`/GILT_Artifacts/GILT`](https://github.com/namdy0429/GILT_Artifacts/tree/main/GILT)

There is no requirement to run this plugin other than having a [Visual Studio Code](https://code.visualstudio.com/) installed. 

## User study analysis replication: [`/GILT_Artifacts/Study`](https://github.com/namdy0429/GILT_Artifacts/tree/main/Study)

R Notebook contains the user study result data and scripts to replicate the statistical analysis.
To run this file, R-Notebook should be installed on your machine.
Or, you can run it with a ready-to-run docker image [`jupyter/r-notebook`](https://hub.docker.com/r/jupyter/r-notebook) (see [`INSTALL.md`](https://github.com/namdy0429/SOREL/blob/main/INSTALL.md) for details).

#### R-notebook

- R version 3.6.3 (2020-02-29)
- Platform: aarch64-conda-linux-gnu (64-bit)
- Running under: Ubuntu 22.04.1 LTS

#### R Packages

- MuMIn_1.46.0
- lme4_1.1-31
- lmerTest_3.1-3
- Matrix_1.3-3

A script to install the packages is included in the R-notebook.

## User study task run: [`/GILT_Artifacts/study/design/tasks`](https://github.com/namdy0429/GILT_Artifacts/tree/main/study/design/tasks)

To run python code used in the study, the following Python libraries should be installed:

- pandas (tested with 2.0.3)
- matplotlib (tested with 3.7.2)
- bokeh (tested with 3.3.1)
- open3d (tested with 0.16.1)
