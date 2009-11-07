#!/usr/bin/perl -w

use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Spreadsheet::WriteExcel;
use Net::WhitePages;
use Regexp::Assemble;
#use XML::Dumper;
use strict;

my $q = new CGI;
my $house = $q->param('house');
my $street = $q->param('street');
my $zip = $q->param('zip');
my @phoneduplicates;

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

my $r = my $c = my $rm = my $cm = 0; #Rows and Columns for the spreadsheet

my $wp = new Net::WhitePages(TOKEN=>'INSERTYOURTOKENHERE');

my $res = $wp->reverse_address(house=>$house, zip=>$zip, street=>$street);
my $listingref = $$res{listings};
my $metaref = $$res{meta};
my $resultref = $$res{result};
my $firstrecord = $metaref->{recordrange}->{firstrecord};
my $lastrecord = $metaref->{recordrange}->{lastrecord};
my $totalrecord = $metaref->{recordrange}->{totalavailable};

print $q->header(-attachment => 'dl.xls',
                -type =>'application/vnd.ms-excel',
		-expires => 'now',
                );

my $xls = Spreadsheet::WriteExcel->new('-');
my $sheet = $xls->add_worksheet('Territorio');
my $sheetmeta = $xls->add_worksheet('Metadata');

#
# Title the sheets
#
my $titleformat = $xls->add_format(bg_color=>'yellow', size=>24, font=>'Times New Roman', border=>0);
my $subtitleformat = $xls->add_format(bold=>1, bottom=>6);
my $mainformat = $xls->add_format(bottom=>1, left=>1, right=>1);

$sheet->write($r++, $c, 'Territorio', $titleformat);
$sheet->set_row(0, 30.75, $titleformat);
$r++;
$sheet->write($r++, $c, ['Telefono', 'Nombre Completo', 'Dirrecion', 'Fecha 1', 'Fecha 2', 'Fecha3'], $subtitleformat);
$sheet->set_column(0, 0, 14.86);
$sheet->set_column(1, 1, 20.29);
$sheet->set_column(2, 2, 24.43);
$sheet->set_column(3, 5, 8.43);

$sheetmeta->write($rm++, $cm, ['Full Name', 'Phone Number', 'Last Validated', 'Address', 'Neighbors', 'Details']);


$sheetmeta->write($rm++, $cm, "First record is $firstrecord, Last is $lastrecord, there is a total of $totalrecord addresses.");
$rm++;

# Main loop
foreach my $listing (@$listingref)
	{
	$c = $cm = 0; #Reset Column pointers
	my $lastname = $listing->{people}[0]->{lastname};
	my $fullstreet = $listing->{address}->{fullstreet};
	my $fullphone =  $listing->{phonenumbers}[0]->{fullphone};

	if (exists $listing->{address}->{apttype}) # If there's apartment data, find it and append it.
		{
		$fullstreet .= $listing->{address}->{apttype} . " " . $listing->{address}->{aptnumber};
		}

	# Populate Meta Sheet
	$sheetmeta->write($rm, $cm++, $listing->{displayname});
	$sheetmeta->write($rm, $cm++, $fullphone);
	$sheetmeta->write($rm, $cm++, $listing->{listingmeta}->{lastvalidated});
	$sheetmeta->write($rm, $cm++, $fullstreet);
	$sheetmeta->write_url($rm, $cm++,
			$listing->{listingmeta}->{moreinfolinks}->{findneighbors}->{url},
			$listing->{listingmeta}->{moreinfolinks}->{findneighbors}->{linktext},
			);
	$sheetmeta->write_url($rm++, $cm++,
			$listing->{listingmeta}->{moreinfolinks}->{viewdetails}->{url},
			$listing->{listingmeta}->{moreinfolinks}->{viewdetails}->{linktext},
			);

	# Populate "pretty" sheet
	next if (grep {$_ eq $fullphone} @phoneduplicates); # Don't print if the phone number is already there.
	push (@phoneduplicates, $fullphone);
	
	next unless ($lastname =~ /$spanmatch/); #Make sure it's spanish last name

	$sheet->write($r, $c++, $listing->{phonenumbers}[0]->{fullphone}, $mainformat);
	$sheet->write($r, $c++, $listing->{displayname}, $mainformat);
	$sheet->write($r, $c++, $fullstreet, $mainformat);
	$sheet->write($r++, $c++, [undef, undef, undef], $mainformat);
	}
$xls->close();
