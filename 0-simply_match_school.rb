#!/usr/bin/env ruby

# Extract the argument passed to the script
string = ARGV[0]

# Apply the regular expression to match "School"
if string =~ /School/
  puts "School"
else
  puts ""
end
