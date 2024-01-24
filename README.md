# GILT Artifacts

## Paper

Daye Nam, Brad Myers, Bogdan Vasilescu, and Vincent Hellendoorn, "Using an LLM to Help With Code Understanding," ICSE 2024.

## Artifacts

Up-to-date artifacts are available here: [https://github.com/namdy0429/GILT_Artifacts](https://github.com/namdy0429/GILT_Artifacts)

There are two main components in this repository.

#### GILT (Generation-based Information-support with LLM Technology): [`/GILT_Artifacts/GILT`](https://github.com/namdy0429/GILT_Artifacts/tree/main/GILT)

[`/GILT_Artifacts/GILT/README.md`](https://github.com/namdy0429/GILT_Artifacts/tree/main/GILT), [`/GILT_Artifacts/GILT/overview.png`](https://github.com/namdy0429/GILT_Artifacts/blob/main/GILT/overview.png), and [`GILT_Artifacts/GILT/demo.mov`](https://github.com/namdy0429/GILT_Artifacts/blob/main/GILT/demo.mov) show how to use GILT.

#### Replication package for the user study analysis: [`/GILT_Artifacts/study`](https://github.com/namdy0429/GILT_Artifacts/tree/main/study)

You can replicate the statistical analysis included in the paper by running [`/GILT_Artifacts/study/analysis.ipynb`](https://github.com/namdy0429/GILT_Artifacts/blob/main/study/analysis.ipynb).

User study result data can be found [`/GILT_Artifacts/study/study_data.csv`](https://github.com/namdy0429/GILT_Artifacts/blob/main/study/study_data.csv). 
[`/GILT_Artifacts/Install.md`](https://github.com/namdy0429/GILT_Artifacts/blob/main/INSTALL.md) describes how to set up R-Notebook environment to run this Notebook.
Study protocol and task designs are also included in [`/GILT_Artifacts/study/design/`](https://github.com/namdy0429/GILT_Artifacts/tree/main/study/design) and [`/GILT_Artifacts/study/design/tasks/`](https://github.com/namdy0429/GILT_Artifacts/tree/main/study/design/tasks).

## STATUS
We are applying for **Available** and **Reusable** badges. The artifacts are made public and permanently archived. We also believe that the artifacts are well documented and easily exercisable by other researchers.

## INSTALLATION

#### GILT (Generation-based Information-support with LLM Technology): [`/GILT_Artifacts/GILT.vsix`](https://github.com/namdy0429/GILT_Artifacts/tree/main/Plugin)
GILT is a prototype in-IDE LLM information support tool.
To install GILT from using the provided `.vsix` file, you can do one of the following:
- Using the `Install from VSIX` command in the Extensions view command dropdown, or the `Extensions: Install from VSIX` command in the Command Palette, point to the .vsix file.
- You can also install using the VS Code `--install-extension` command-line switch providing the path to the `.vsix` file.

    code --install-extension myextension.vsix

You can find more detailed instructions from [Code User Guide](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix).

#### User study analysis replication: [`/GILT_Artifacts/study`](https://github.com/namdy0429/GILT_Artifacts/tree/main/study)

Our statistical analysis on the user study results were written in R, using Jupyter Notebook.
To run the study analysis script, you need to be able to run R-notebook.
If you have Jupyter Notebook already with R language and r-essentials already, simply load `Study/analysis.ipynb` from your notebook interface. The data is already included in the code.

If not, you can use a ready-to-run Docker image to launch Jupyter Notebook environment (no need to download Jupyter Notebook).
Downloading the jupyter/R-notebook docker image will require ~1G of memory space.

```
$ docker run -p 8888:8888 --name notebook -v [path-to-Artifacts]/study/:/home/jovyan/work jupyter/r-notebook
```

Then, you will see the following output:

```
    To access the server, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
    Or copy and paste one of these URLs:
        http://a54a3d055112:8888/lab?token=d76cc9282c7ce986cbdf2e1f35a81321a58ae0f773ea7a19
     or http://127.0.0.1:8888/lab?token=d76cc9282c7ce986cbdf2e1f35a81321a58ae0f773ea7a19
```
Click the link to open the Notebook interface. You can find [`analysis.ipynb`](https://github.com/namdy0429/GILT_Artifacts/blob/main/study/analysis.ipynb) under `/work/` directory.

## REQUIREMENTS

We expect that everyone with reasonable programming experience can open and run the artifacts with standard environments.
Part of the artifacts have some package requirements, but there is no deviation from standard environments for data science.

The artifacts are tested with MacBook Pro (14-inch, 2021, Apple M1 Max, 32 GB Memory).

#### GILT (Generation-based Information-support with LLM Technology): [`/GILT_Artifacts/GILT`](https://github.com/namdy0429/GILT_Artifacts/tree/main/GILT)

There is no requirement to run this plugin other than having a [Visual Studio Code](https://code.visualstudio.com/) installed. 

#### User study analysis replication: [`/GILT_Artifacts/study`](https://github.com/namdy0429/GILT_Artifacts/tree/main/study)

R Notebook contains the user study result data and scripts to replicate the statistical analysis.
To run this file, R-Notebook should be installed on your machine.
Or, you can run it with a ready-to-run docker image [`jupyter/r-notebook`](https://hub.docker.com/r/jupyter/r-notebook) (see [`INSTALL.md`](https://github.com/namdy0429/SOREL/blob/main/INSTALL.md) for details).

##### R-notebook

- R version 3.6.3 (2020-02-29)
- Platform: aarch64-conda-linux-gnu (64-bit)
- Running under: Ubuntu 22.04.1 LTS

##### R Packages

- MuMIn_1.46.0
- car_3.1.1
- rsq_2.5

A script to install the packages is included in the R-notebook.

#### User study task run: [`/GILT_Artifacts/study/design/tasks`](https://github.com/namdy0429/GILT_Artifacts/tree/main/study/design/tasks)

To run python code used in the study, the following Python libraries should be installed:

- pandas (tested with 2.0.3)
- matplotlib (tested with 3.7.2)
- bokeh (tested with 3.3.1)
- open3d (tested with 0.16.1)
