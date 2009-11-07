#!/usr/bin/perl -w

use strict;
use Regexp::Assemble;

my $spanmatch = Regexp::Assemble->new;
$spanmatch->add(qw(os
		ez
		cia
		era
		ano
		ega
		as
		ado
		inos
		illa
		raz
		edo
		jia
		bar
		jas
		elo
		gel
		illo
		)
			)->anchor_line_end; #Last name endings

$spanmatch->add(qw(rr)); 
#print $spanmatch->re;

print "Match!\n" if ($ARGV[0] =~ /$spanmatch/);
