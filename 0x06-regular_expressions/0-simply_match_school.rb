#!/usr/bin/env ruby

# Extract the input string from the command-line argument
input_string = ARGV[0]

# Match the word "School" using a regular expression
match = input_string.match(/School/)

# Output the matched result if found
puts match[0] if match
