%define texdir /usr/share/texmf
Summary: LaTeX macros for writing documents following the ABNT norms
Summary(pt_BR): Macros para LaTeX que implementam normas da ABNT
Name: latex-abntex
Version: 0.9
Release: %mkrel -c beta1 1
License: LPPL
Group: Publishing
URL: http://abntex.codigolivre.org.br
Source: abntex-%{version}-beta.tar.gz
Patch0: abntex-0.9-respect-prefix.patch
Requires: tetex
BuildRequires: tetex
BuildRoot: %{_tmppath}/%{name}-%{version}-root
%description
With the abnTeX macros you will be able to write LaTeX
documents which conform to several norms from ABNT
(Brazilian Association for Technical Norms). In addition there
are macros for writing automated lists of abbreviations and
symbols and a style for writing patent applications for INPI.
You can also use these style with LyX.

%description -l pt_BR
As macros abnTeX possibilitam escrever documentos latex
em conformidade com as diversas normas da ABNT (Associação
Brasileira de Normas Técnicas). Além disso estão incluídas
macros para a confeção automatizada de listas de abreviaturas
e símbolos e um estilo para escrever requerimentos de patentes
para o INPI. Você também pode usar esses estilos com LyX.

%prep
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
%setup -n abntex-%{version}
%patch0 -p1 -b .respect-prefix

%build
:

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT/%_datadir/texmf/
install -m 755 -d $RPM_BUILD_ROOT/%_bindir
make install DESTDIR=$RPM_BUILD_ROOT USRLOCAL=$RPM_BUILD_ROOT/usr/bin

%post
texhash

%postun
texhash

%files
%defattr(-, root, root)
%doc LEIAME LEIAME.linux LEIAME.make LEIAME.administracao
%{texdir}/bibtex/bib/abntex
%{texdir}/bibtex/bst/abntex
%{texdir}/doc/bibtex/abntex
%{texdir}/doc/latex/abntex
%{texdir}/makeindex/abntex
%{texdir}/tex/latex/abntex
%{_bindir}/geratss

