Summary:	General tool for mathematics
Summary(pl):	Rozbudowane narzêdzie matematyczne
Name:		drgenius
Version:	0.5.10
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://ofset.sourceforge.net/drgenius/index.html
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gmp-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gob >= 0.93.4
BuildRequires:	libstdc++-devel
BuildRequires:	libxml-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
Obsoletes:	genius
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dr. Genius is a general tool for mathematics, including a mathematical
programming language and evaluator, an euclidian geometry tool, a
2D/3D function grapher and a console calculator. The console
calculator handles multiple precision floating point numbers, infinite
precision integers, complex numbers and matrixes.

%description -l pl
Dr. Genius to narzêdzie do rozwi±zywania problemów matematycznych.
Zawiera ono matematyczny jêzyk programowania, narzêdzie do geometrii
euklidesowej, narzêdzie do generowania wykresów 2D/3D oraz konsolowy
kalkulator. Kalkulator obs³uguje liczby zmiennoprzecinkowe wysokiej
precyzji, liczby ca³kowite, zespolone oraz macierze.

%prep
%setup -q
%patch0 -p1

%build
rm missing acinclude.m4
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure \
	--enable-gnome \
	--disable-static \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/Utilities

gzip -9nf AUTHORS NEWS README TODO

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %dir %{_libdir}/genius
%attr(755,root,root) %{_libdir}/genius/*
%{_includedir}/genius
%{_datadir}/drgenius
%{_datadir}/genius
%{_pixmapsdir}/*
%{_applnkdir}/Utilities/*
