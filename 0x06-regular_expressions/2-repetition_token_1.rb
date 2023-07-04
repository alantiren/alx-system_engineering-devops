#!/usr/bin/env ruby

# Extract the argument passed to the script
string = ARGV[0]

# Apply the regular expression to match "hb" followed by zero or more occurrences of "t" and then "n"
regex = /hbt*n/
match = string.match(regex)

# Output the matched substring if there is a match
puts match[0] if match
