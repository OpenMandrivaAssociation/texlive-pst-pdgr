Name:		texlive-pst-pdgr
Version:	45875
Release:	1
Summary:	Draw medical pedigrees using pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pedigree/pst-pdgr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdgr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdgr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pdgr.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/pst-pdgr
%{_texmfdistdir}/tex/latex/pst-pdgr
%doc %{_texmfdistdir}/doc/generic/pst-pdgr
#- source
%doc %{_texmfdistdir}/source/generic/pst-pdgr

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
