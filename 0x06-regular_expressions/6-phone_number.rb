#!/usr/bin/env ruby
puts ARGV[0].scan(/[0-9]{10}|\d{3,4}/).join
