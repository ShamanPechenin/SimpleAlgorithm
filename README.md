# SimpleAlgorithm

This software implements markov chain algorithm for text generation from a source text file.

To generate text you need a source text, starting string, token size and generated text size

Markov chain algorithm is a statistical method of generating text, in short we can look at how often some word or sequence of words appear after another to know what to write next.

This program first divides text into tokens(sequences of words) using function ```parse_text```, then makes a dict of tokens that appear one after the other using ```make_pairs``` and generates a text using ```generate_text_chain```.

Example source text is from https://gist.github.com/blakesanie/dde3a2b7e698f52f389532b4b52bc254