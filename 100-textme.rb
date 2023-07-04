#!/usr/bin/env ruby

# Extract the log message from the command-line argument
log_message = ARGV[0]

# Extract the sender, receiver, and flags using regular expressions
sender = log_message.match(/\[from:(.*?)\]/)[1]
receiver = log_message.match(/\[to:(.*?)\]/)[1]
flags = log_message.match(/\[flags:(.*?)\]/)[1]

# Output the extracted information
puts "#{sender},#{receiver},#{flags}"
