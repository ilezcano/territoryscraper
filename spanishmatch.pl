#!/usr/bin/perl -w

use strict;
use Regexp::Assemble;

my $spanmatch = Regexp::Assemble->new->add(qw(
		os$
		ez$
		es$
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
		),
		chr(0xF1),
		chr(0xE9),
		chr(0xE1),
		chr(0xED),
		chr(0xF3),
		chr(0xFA),
			)->re; #Last name endings

print "Match!\n" if ($ARGV[0] =~ /$spanmatch/);
