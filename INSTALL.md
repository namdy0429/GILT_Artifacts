# INSTALL

## GILT (Generation-based Information-support with LLM Technology): [`/GILT_Artifacts/GILT.vsix`](https://github.com/namdy0429/GILT_Artifacts/tree/main/Plugin)
GILT is a prototype in-IDE LLM information support tool.
To install GILT from using the provided `.vsix` file, you can do one of the following:
- Using the `Install from VSIX` command in the Extensions view command dropdown, or the `Extensions: Install from VSIX` command in the Command Palette, point to the .vsix file.
- You can also install using the VS Code `--install-extension` command-line switch providing the path to the `.vsix` file.

    code --install-extension myextension.vsix

You can find more detailed instructions from [Code User Guide](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix).

## User study analysis replication: [`/GILT_Artifacts/Study`](https://github.com/namdy0429/GILT_Artifacts/tree/main/Study)

Our statistical analysis on the user study results were written in R, using Jupyter Notebook.
To run the study analysis script, you need to be able to run R-notebook.
If you have Jupyter Notebook already with R language and r-essentials already, simply load `Study/analysis.ipynb` from your notebook interface. The data is already included in the code.

If not, you can use a ready-to-run Docker image to launch Jupyter Notebook environment (no need to download Jupyter Notebook).
Downloading the jupyter/R-notebook docker image will require ~1G of memory space.

```
$ docker run -p 8888:8888 --name notebook -v [path-to-Artifacts]/Study/:/home/jovyan/work jupyter/r-notebook
```

Then, you will see the following output:

```
    To access the server, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
    Or copy and paste one of these URLs:
        http://a54a3d055112:8888/lab?token=d76cc9282c7ce986cbdf2e1f35a81321a58ae0f773ea7a19
     or http://127.0.0.1:8888/lab?token=d76cc9282c7ce986cbdf2e1f35a81321a58ae0f773ea7a19
```
Click the link to open the Notebook interface. You can find [`analysis.ipynb`](https://github.com/namdy0429/GILT_Artifacts/blob/main/Study/analysis.ipynb) under `/work/` directory.
