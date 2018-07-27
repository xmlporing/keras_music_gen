# README #

## Motivations
Generate music

## How do I get set up?

### Libraries
- Keras==2.2.0
- Tensorflow==1.9.0
- PySynth (install by git clone from https://github.com/mdoege/PySynth and python setup.py)

### To run ###
- Run in a conda environment python=3.6, install notebook and run the notebook in src/
- Run src/splitABC.py <path to abc> to extract all abc notes

## Things I done

- Attempt 1
> Train as raw ABC files
* - Work out badly, unable to synthesis wav file with PySynth

- Attempt 2
> Strip away title, comments, composer, source
* - Have multiple header lines as part of generation, e.g. K: inside as note, still unable to synthesis wav file

- Attempt 3
> Remove all upper char followed by ':' and '&' line and created a script to combine them tgt, using notes only
> Hardcoded some header lines to generate ABC files
* - Able to generate the wav file with PySynth, however the length of wav file is independent of the amount of note

- Attempt 4
> Remove newline from generated ABC notes 
* - Length is dependent of the amount of note generated

- Attempt 5
> Changed the neural network layer, remove one dense layer before 2nd LSTM cell
* - Better results

- Attempt 6
> Changed how y hat is used, using weighted sampling instead of argsmax (always choose the max)
* - Improved in notes being repeated

## Known Bugs
- Illegal ABC notes may be constructed, required some rule-based to ensure the integrity of the notes generated
- - Thus the higher the reduced set (nprobs, to introduce variation into selection), higher chance of illegal ABC notes generated

## Links
- What is ABC music notation? - http://trillian.mit.edu/~jc/doc/abc/ABCprimer.html
- PySynth library - https://github.com/mdoege/PySynth
- List of ABC music notation - http://abcnotation.com/tunes#large
