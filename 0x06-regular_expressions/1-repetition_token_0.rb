#!/usr/bin/env ruby

# Extract the argument passed to the script
string = ARGV[0]

# Apply the regular expression to match "hbt" followed by 2 to 5 occurrences of "t" and then "n"
regex = /hbt{2,5}n/
match = string.match(regex)

# Output the matched substring if there is a match
puts match[0] if match
