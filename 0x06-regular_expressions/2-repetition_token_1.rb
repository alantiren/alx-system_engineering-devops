#!/usr/bin/env ruby

# Extract the argument passed to the script
string = ARGV[0]

# Apply the regular expression to match "hbtn" repeated zero or one time
regex = /hb[t]?n/
matches = string.scan(regex)

# Print the matched substrings
matches.each { |match| puts match }
