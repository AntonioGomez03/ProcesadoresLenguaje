#!/bin/bash

LEXER_DIR="src/antlr4"
LEXER_FILE="gec_lexer.g4"
OUTPUT_DIR="src/lexer"

# Create the output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Generate the lexer
antlr4 -Dlanguage=Python3 -o $OUTPUT_DIR $LEXER_DIR/$LEXER_FILE

# Move the lexer file to the correct location
mv $OUTPUT_DIR/$LEXER_DIR/* $OUTPUT_DIR

# Remove the old directory
PARENT_DIR=$(dirname $OUTPUT_DIR/$LEXER_DIR)
rm -rf $PARENT_DIR