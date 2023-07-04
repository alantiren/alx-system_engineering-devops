#!/usr/bin/env ruby

# Extract the argument passed to the script
string = ARGV[0]

# Apply the regular expression to match "hbtn" repeated one or more times, with an "n" at the end
regex = /hb[t]+n/
matches = string.scan(regex)

# Print the matched substrings
matches.each { |match| puts match }
