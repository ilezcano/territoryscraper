#!/usr/bin/perl -w

use strict;
use Regexp::Assemble;

my $spanmatch = Regexp::Assemble->new->add(qw(
		os$
		ez$
		cia$
		era$
		ano$
		ega$
		as$
		ado$
		inos$
		illa$
		raz$
		edo$
		jia$
		bar$
		jas$
		elo$
		gel$
		illo$
		rr
		)
			)->re; #Last name endings

#print $spanmatch->re;

print "Match!\n" if ($ARGV[0] =~ /$spanmatch/);
