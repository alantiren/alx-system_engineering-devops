#!/usr/bin/env ruby

# Extract the argument passed to the script
string = ARGV[0]

# Apply the regular expression to match capital letters
regex = /[A-Z]/
matches = string.scan(regex)

# Join the matched letters to form the resulting string
result = matches.join

# Print the resulting string in uppercase
puts result.upcase
