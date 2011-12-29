# revision 20060
# category Package
# catalog-ctan /macros/latex/contrib/chletter
# catalog-date 2010-10-11 07:24:02 +0200
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-chletter
Version:	2.0
Release:	1
Summary:	Class for typesetting letters to Swiss rules
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chletter
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chletter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chletter.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chletter.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class enables composition of letters fitting into Swiss C5
& C6/5 windowed envelopes. No assumption is made about the
language used. The class is based on the standard LaTeX classes
and is compatible with the LaTeX letter class. It is not
limited to letters and may be used as a generic document class;
it is used with the chextras package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chletter/chletter.cls
%doc %{_texmfdistdir}/doc/latex/chletter/README
%doc %{_texmfdistdir}/doc/latex/chletter/chletter.pdf
%doc %{_texmfdistdir}/doc/latex/chletter/chlettmp.tex
#- source
%doc %{_texmfdistdir}/source/latex/chletter/chletter.dtx
%doc %{_texmfdistdir}/source/latex/chletter/chletter.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
