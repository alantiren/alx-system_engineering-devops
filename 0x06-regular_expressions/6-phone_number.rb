#!/usr/bin/env ruby

# Extract the argument passed to the script
string = ARGV[0]

# Apply the regular expression to match a 10-digit phone number
regex = /^[0-9]{10}$/
matches = string.scan(regex)

# Print the matched substrings
matches.each { |match| puts match }
