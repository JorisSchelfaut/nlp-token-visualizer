# ###########################################################################
# 
# Language Model visualization
# Inspired by https://tiktokenizer.vercel.app/
# 
# ###########################################################################


# Create a dictionary of colors
# Note: the order of the colours remains the same and the pattern is repeated
#       (cf. https://www.w3schools.com/cssref/css_colors.php)
HTML_COLORS  = ["Khaki", "AliceBlue", "Aquamarine", "Coral", "Lavender", "Ivory", "DarkSalmon"]

# Note: for LaTeX, consider using another colour set
#       (cf. https://www.overleaf.com/learn/latex/Using_colors_in_LaTeX)
LATEX_COLORS = ["yellow", "pink", "lightgray", "lime", "cyan", "magenta" ]


def process_text(text, encode, decode, markup='html', colors=None):
    """
    Colour codes each token in a text according to the encoding vocabulary
    
    Parameters:
        string:text                     the text to encode
        function(string)->[int]:encode  the encoding method
        function([int])->string:decode  the decoding method
        string:scheme                   html|latex
        [string]:colors                 the sequence of colours
    
    Returns:
        string:                         colour-encoded text
    """
    
    if colors is None:
        if markup == 'html':
            colors = HTML_COLORS
        elif markup == 'latex':
            color = LATEX_COLORS
        else:
            raise Exception("Unknown markup.")
    
    # encode the incoming text with the given encoding method
    encodings = encode(text)
    
    # the colour-coded tokens
    colored_tokens = []
    
    # keep a counter of the words seen so far to map onto the color scheme
    index = 0
    
    # for each encoded token:
    # - decode it
    # - color it according to the given colouring scheme
    # - add it to the colored_tokens list
    for encoding in encodings:
        token = decode([encoding])
        color = colors[index % len(colors)]
        
        # color formatting according to usage
        if markup == 'html':
            # create span with background colour
            colored_word = f'<span style="background-color: {color};">{token}</span>'
            
            # HTML requires different treatment of line breaks
            if '\n' in token:
                colored_word = colored_word + '<br>'
        elif markup == 'latex':
            
            # use background colour instead of text colour
            colored_word = "(*@\\colorbox{" + color + "}{" + token + "}@*)"
            #colored_word = "(*@\\textcolor{" + color + "}{" + token + "}@*)"
            
            # so re-add them again at the end
            if token.endswith('\n'):
                colored_word = colored_word + '\n'
        else:
            raise Exception("Unknown markup.")
        
        index = index + 1
        colored_tokens.append(colored_word)
    return ''.join(colored_tokens)
