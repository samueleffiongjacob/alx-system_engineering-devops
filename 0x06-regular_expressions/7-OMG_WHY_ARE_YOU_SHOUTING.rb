#!/usr/bin/env ruby
puts ARGV[0].scan(/[A-Z]*/).join

# The regular expression must be only matching: capital letters