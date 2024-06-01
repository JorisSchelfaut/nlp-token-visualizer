# nlp-token-visualizer
Token visualization for NLP tasks.

## HTML example

Here's a simple example using the predefined encoding/decoding methods with a simple string. Assuming `encode` simply maps each character to a number, the following...

```python
text = 'Hello world!'
processed_text = process_text(text, encode, decode, markup='html', colors=tokenviz.visualization.HTML_COLORS)
```

generates...
<br>

```html
<span style="background-color: Khaki;">H</span><span style="background-color: AliceBlue;">e</span><span style="background-color: Aquamarine;">l</span><span style="background-color: Coral;">l</span><span style="background-color: Lavender;">o</span><span style="background-color: Ivory;"> </span><span style="background-color: DarkSalmon;">w</span><span style="background-color: Khaki;">o</span><span style="background-color: AliceBlue;">r</span><span style="background-color: Aquamarine;">l</span><span style="background-color: Coral;">d</span><span style="background-color: Lavender;">!</span>
```


## LaTeX example

Add the following imports and definitions to your LaTeX document.

```latex
\usepackage{listings}
\usepackage{xcolor}

% Define a custom style for listings
\lstdefinestyle{custom}{
    basicstyle=\small\ttfamily, % Small font size and typewriter style
    escapeinside={(*@}{@*)},    % Escape for inline LaTeX
}
```

Then add your generated LaTeX code to the listing:

```latex
\begin{lstlisting}[caption=My title, label=mylabel, style=custom]
% Your LaTeX code goes here
\end{lstlisting}
```

Assuming `encode` simply maps each character to a number, the following...

```python
text = 'Hello world!'
processed_text = process_text(text, encode, decode, markup='latex', colors=tokenviz.visualization.LATEX_COLORS)
```

generates...

```latex
(*@\colorbox{yellow}{H}@*)(*@\colorbox{pink}{e}@*)(*@\colorbox{lightgray}{l}@*)(*@\colorbox{lime}{l}@*)(*@\colorbox{cyan}{o}@*)(*@\colorbox{magenta}{ }@*)(*@\colorbox{yellow}{w}@*)(*@\colorbox{pink}{o}@*)(*@\colorbox{lightgray}{r}@*)(*@\colorbox{lime}{l}@*)(*@\colorbox{cyan}{d}@*)(*@\colorbox{magenta}{!}@*)
```

