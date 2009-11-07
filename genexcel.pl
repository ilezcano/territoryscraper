#!/usr/bin/perl -w
#===============================================================================
#
#         FILE:  genexcel.pl
#
#        USAGE:  ./genexcel.pl  
#
#  DESCRIPTION:  Test script to generate excel files
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:  YOUR NAME (), 
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  10/31/2009 02:19:05 PM
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;
use Spreadsheet::WriteExcel;

my $xls = Spreadsheet::WriteExcel->new('output.xls');
my $sheet = $xls->add_worksheet('Territory Info');
my $metasheet = $xls->add_worksheet('Metadata');
$sheet->set_row(0, undef, $titleformat);
$sheet->write(0, 0, 'Territorio');

$titleformat = $xls->add_format(bg_color=>'yellow', size=>24, font=>'Times New Roman', border=>0);
my $subtitleformat = $xls->add_format(bold=>1, bottom=>6);
my $mainformat = $xls->add_format(bottom=>1, left=>1, right=>1);
$sheet->set_row(0, 24, $titleformat);

$sheet->set_row(2, undef, $subtitleformat);
$sheet->write(0, 0, 'Territorio');
$sheet->write(2, 0, ['Telefono', 'Nombre Completo', 'Dirrecion', 'Fecha 1', 'Fecha 2', 'Fecha3'], $subtitleformat);
$sheet->write(3, 0, ['Telefono', 'Nombre Completo', 'Dirrecion', 'Fecha 1', 'Fecha 2', 'Fecha3'], $mainformat);
$sheet->write(4, 0, ['Telefono', 'Nombre Completo', 'Dirrecion', 'Fecha 1', 'Fecha 2', 'Fecha3'], $mainformat);

$sheet->set_column(0, 0, 14.86);
$sheet->set_column(1, 1, 20.29);
$sheet->set_column(2, 2, 24.43);
$sheet->set_column(3, 5, 8.43);
$xls->close();
