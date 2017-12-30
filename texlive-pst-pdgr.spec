# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pedigree/pst-pdgr
# catalog-date 2007-08-14 12:06:32 +0200
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-pst-pdgr
Version:	0.4
Release:	1
Summary:	Draw medical pedigrees using pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pedigree/pst-pdgr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdgr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdgr.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdgr.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of macros based on PSTricks to draw
medical pedigrees according to the recommendations for
standardized human pedigree nomenclature. The drawing commands
place the symbols on a pspicture canvas. An interface for
making trees is also provided. The package may be used both
with LaTeX and PlainTeX. A separate Perl program for generating
TeX files from spreadsheets is available.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-pdgr/pst-pdgr.tex
%{_texmfdistdir}/tex/latex/pst-pdgr/pst-pdgr.cfg
%{_texmfdistdir}/tex/latex/pst-pdgr/pst-pdgr.sty
%doc %{_texmfdistdir}/doc/generic/pst-pdgr/NEWS
%doc %{_texmfdistdir}/doc/generic/pst-pdgr/README
%doc %{_texmfdistdir}/doc/generic/pst-pdgr/pst-pdgr.bib
%doc %{_texmfdistdir}/doc/generic/pst-pdgr/pst-pdgr.pdf
#- source
%doc %{_texmfdistdir}/source/generic/pst-pdgr/Makefile
%doc %{_texmfdistdir}/source/generic/pst-pdgr/pst-pdgr.dtx
%doc %{_texmfdistdir}/source/generic/pst-pdgr/pst-pdgr.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 755397
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 719379
- texlive-pst-pdgr
- texlive-pst-pdgr
- texlive-pst-pdgr
- texlive-pst-pdgr

