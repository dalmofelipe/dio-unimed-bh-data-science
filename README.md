# DIO Bootcamp Data Science Unimed BH

```bash

python.exe -m pip install --upgrade pip

pip install -r requirements.txt

.\venv\Scripts\activate

jupyter-notebook

```


Jupyter Config Files and Theme

```bash

jupyter --config-dir

```

##### custom.css

Salvar css customizado no diretorio home/.jupyter/custom

```js

/* Change outer background and make the notebook take all available width */
.container {
    width: 99% !important;
    background: #DDC !important;
}   

/* Change inner background (CODE) */
div.input_area {
    background: #F4F4E2 !important;
    font-size: 16px !important;
}

/* Change global font size (CODE) */
.CodeMirror {
    font-size: 16px !important;
}  

/* Prevent the edit cell highlight box from getting clipped;
 * important so that it also works when cell is in edit mode */
div.cell.selected {
    border-left-width: 1px !important;
}

div#notebook {
    background-color: #ccc !important;
}
```