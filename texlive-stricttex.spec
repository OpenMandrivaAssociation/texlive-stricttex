%global tl_name stricttex
%global tl_revision 56320

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2beta
Release:	%{tl_revision}.1
Summary:	Strictly balanced brackets and numbers in command names
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/stricttex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stricttex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stricttex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a small, LuaLaTeX-only package providing you with three,
sometimes useful features: It allows you to make brackets [...]
"strict", meaning that each [ must be balanced by a ]. It allows you to
use numbers in command names, so that you can do stuff like
\newcommand\pi12{\pi_{12}}. It allows you to use numbers and primes in
command names, so that you can do stuff like \newcommand\pi'12{\pi
'_{12}}.

