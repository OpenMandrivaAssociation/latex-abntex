%define texdir /usr/share/texmf
Summary: LaTeX macros for writing documents following the ABNT norms
Summary(pt_BR): Macros para LaTeX que implementam normas da ABNT
Name: latex-abntex
Version: 0.9
Release: %mkrel -c beta2 2
License: LPPL
Group: Publishing
URL: http://abntex.codigolivre.org.br
Source: abntex-%{version}-beta2.tar.gz
Patch0: abntex-0.9-respect-prefix.patch
Requires: tetex
BuildArch: noarch
BuildRequires: tetex tetex-latex tetex-dvips
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
make doc-ps

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT/%_datadir/texmf/
install -m 755 -d $RPM_BUILD_ROOT/%_bindir
install -m 755 -d $RPM_BUILD_ROOT/%_docdir
make install DESTDIR=$RPM_BUILD_ROOT USRLOCAL=$RPM_BUILD_ROOT/usr/bin

%post
texhash

%postun
texhash

%files
%defattr(-, root, root)
%doc LEIAME LEIAME.linux LEIAME.make LEIAME.administracao
%doc compiled.docs/*.ps.gz
%{texdir}/bibtex/bib/abntex
%{texdir}/bibtex/bst/abntex
%{texdir}/doc/bibtex/abntex
%{texdir}/doc/latex/abntex
%{texdir}/makeindex/abntex
%{texdir}/tex/latex/abntex
%{_bindir}/geratss



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-0.beta2.2mdv2011.0
+ Revision: 612698
- the mass rebuild of 2010.1 packages

* Tue Mar 23 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0.9-0.beta2.1mdv2010.1
+ Revision: 526933
- new version beta2
- added ps docs in the package
- make it noarch

* Mon Mar 22 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0.9-0.beta1.1mdv2010.1
+ Revision: 526649
- imported package latex-abntex


* Mon Mar 22 2010 Bogdano Arendartchuk <bogdano@mandriva.com.br>
- imported to Mandriva Linux

* Mon Jul 3 2006 Bogdano Arendartchuk <bogdano@mandriva.com.br>
Adapted spec file to Mandriva Linux.

* Fri May 30 2003 Gerald Weber <gweber@codigolivre.org.br>
Corrigido o bug 137.

* Tue Mar 19 2003 Gerald Weber <gweber@codigolivre.org.br>
Adicionado o pacote lyx.

* Tue Nov 27 2002 Gerald Weber <gweber@codigolivre.org.br>
Correção de bug na classe abnt.cls.

* Tue Nov 19 2002 Gerald Weber <gweber@codigolivre.org.br>
First release as rpm package.

