%global tl_name pst-pdgr
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Draw medical pedigrees using PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pedigree/pst-pdgr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdgr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdgr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdgr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a set of macros based on PSTricks to draw medical
pedigrees according to the recommendations for standardized human
pedigree nomenclature. The drawing commands place the symbols on a
pspicture canvas. An interface for making trees is also provided. The
package may be used both with LaTeX and PlainTeX. A separate Perl
program for generating TeX files from spreadsheets is available.

