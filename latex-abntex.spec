%define texdir %{_datadir}/texmf-dist

Summary:	LaTeX macros for writing documents following the ABNT norms
Name:		latex-abntex
Version:	0.9
Release:	0.beta2.3
License:	LPPL
Group:		Publishing
Url:		http://abntex.codigolivre.org.br
Source0:	abntex-%{version}-beta2.tar.gz
Patch0:		abntex-0.9-respect-prefix.patch
BuildRequires:	texlive-scheme-full
Requires:	texlive-scheme-full
BuildArch:	noarch

%description
With the abnTeX macros you will be able to write LaTeX documents which
conform to several norms from ABNT (Brazilian Association for Technical
Norms). In addition there are macros for writing automated lists of
abbreviations and symbols and a style for writing patent applications
for INPI. You can also use these style with LyX.

%files
%doc LEIAME LEIAME.linux LEIAME.make LEIAME.administracao
%doc compiled.docs/*.ps.gz
%{texdir}/bibtex/bib/abntex
%{texdir}/bibtex/bst/abntex
%{texdir}/doc/bibtex/abntex
%{texdir}/doc/latex/abntex
%{texdir}/makeindex/abntex
%{texdir}/tex/latex/abntex
%{_bindir}/geratss

%post
texhash

%postun
texhash

#----------------------------------------------------------------------------

%prep
%setup -n abntex-%{version}
%patch0 -p1 -b .respect-prefix

%build
make doc-ps

%install
install -m 755 -d %{buildroot}%{texdir}
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}%{_docdir}
%makeinstall_std USRLOCAL=%{buildroot}%{_bindir}

