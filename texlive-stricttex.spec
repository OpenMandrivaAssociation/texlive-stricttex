Name:		texlive-stricttex
Version:	56320
Release:	1
Summary:	Strictly balanced brackets and numbers in command names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stricttex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stricttex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stricttex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a small, LuaLaTeX-only package providing you with
three, sometimes useful features: It allows you to make
brackets [...] "strict", meaning that each [ must be balanced
by a ]. It allows you to use numbers in command names, so that
you can do stuff like \newcommand\pi12{\pi_{12}}. It allows you
to use numbers and primes in command names, so that you can do
stuff like \newcommand\pi'12{\pi '_{12}}.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/stricttex
%doc %{_texmfdistdir}/doc/lualatex/stricttex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
