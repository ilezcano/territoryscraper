#!/usr/bin/perl -w

use Net::WhitePages;
use XML::Dumper;
use strict;

my $wp = new Net::WhitePages(TOKEN=>'INSERTYOURTOKENHERE');

my $res = $wp->reverse_address(zip=>10573, street=>'oak st.', house=> undef);

my $listingref = $$res{listings};
foreach my $listing (@$listingref)
	{
	local $\ = "\n";
	print $listing->{phonenumbers}[0]->{fullphone} . $listing->{address}->{house} . $listing->{people}[0]->{lastname};
	}
