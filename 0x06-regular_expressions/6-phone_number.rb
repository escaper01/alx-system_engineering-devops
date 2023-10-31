#!/usr/bin/env ruby
puts ARGV[0].scan(/\b\d{10}\b|\d{3}.\d{3}.\d{4}\b/).join
