#!/usr/bin/env ruby

# Extract the argument passed to the script
string = ARGV[0]

# Apply the regular expression to match strings that start with "h", end with "n", and have any single character in between
regex = /^h.n$/
matches = string.scan(regex)

# Print the matched substrings
matches.each { |match| puts match }
