%global tl_name chletter
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Class for typesetting letters to Swiss rules
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chletter
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chletter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chletter.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chletter.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class enables composition of letters fitting into Swiss C5 & C6/5
windowed envelopes. No assumption is made about the language used. The
class is based on the standard LaTeX classes and is compatible with the
LaTeX letter class. It is not limited to letters and may be used as a
generic document class; it is used with the chextras package.

